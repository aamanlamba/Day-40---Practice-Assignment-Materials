#!/usr/bin/env python3
"""AI FDE End-to-End Production Delivery Spine — guided prompt harness.

Stdlib only. The harness folder holds the prompts; each target repository holds
its own evidence (docs/<stage-folder>/) and harness state (docs/_harness/).

    fde.py init     --repo PATH [--author NAME] [--test-cmd CMD]
    fde.py status   --repo PATH
    fde.py next     --repo PATH
    fde.py begin    STAGE|next --repo PATH [--force]
    fde.py prompt   STAGE --repo PATH
    fde.py check    STAGE --repo PATH [--run-tests]
    fde.py complete STAGE --repo PATH [--approved-by NAME] [--commit]
    fde.py run      STAGE --repo PATH [--permission-mode MODE]   (headless `claude -p`)
    fde.py manifest | lint
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HARNESS = Path(__file__).resolve().parents[1]
STAGES_DIR = HARNESS / "stages"
TEMPLATES = HARNESS / "templates"
REGISTRY = Path(os.environ.get("FDE_REGISTRY", HARNESS / "state" / "registry.json"))
FDE = Path(__file__).resolve()

STATE_DIR = "docs/_harness"
REQUIRED_HEADER_KEYS = ["stage", "title", "version", "date", "author", "status", "evidence_sources"]
REQUIRED_SECTIONS = ["Assumptions", "Unresolved Issues", "Residual Risks"]
ARTIFACT_STATUSES = {"draft", "provisional", "in review", "approved", "superseded", "not applicable"}
STAGE_STATUSES = ["PASS", "CONDITIONAL PASS", "BLOCKED"]
DONE = {"PASS", "CONDITIONAL PASS"}
REPORT_SECTIONS = ["1. Stage Status", "2. Key Findings", "3. Major Risks", "4. Assumptions / Unknowns",
                   "5. Artifacts Created", "6. Blocking Issues", "7. Recommended Next Action"]
EVIDENCE_TAGS = re.compile(r"\b(Verified Fact|Inference|Assumption|Unknown)\b")
PLACEHOLDER = re.compile(r"<artifact title>|<body —|<repo path, test|\bTODO\b|\bTBD\b|lorem ipsum", re.I)
MODE_MEANING = {
    "read-only": "do not modify application code, tests, dependencies, configuration, infrastructure, data "
                 "or workflows; write only this stage's docs folder and the harness report",
    "write": "implementation changes are authorized, but only inside the human-approved globs in "
             "docs/_harness/write-boundaries.txt, on the stage branch, one reviewable commit per item",
}


# --------------------------------------------------------------------------- parsing

def _scalar(v: str):
    v = v.strip()
    if v[:1] in "\"'":
        close = v.find(v[0], 1)
        inner = v[1:close] if close != -1 else v[1:]
        return inner.replace("\\\\", "\\") if v[0] == '"' else inner
    v = re.sub(r"\s+#.*$", "", v)
    if v.startswith("[") and v.endswith("]"):
        return [_scalar(x) for x in v[1:-1].split(",") if x.strip()]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v


def parse_front_matter(text: str):
    """Parse the YAML subset used by stage files and artifacts. Returns (meta, body) or (None, text)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    meta: dict = {}
    key = None
    for raw in text[3:end].splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            key, val = m.group(1), m.group(2)
            meta[key] = _scalar(val) if val.strip() else []
        elif line.strip().startswith("- ") and key is not None:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(_scalar(line.strip()[2:]))
    body = text[end + 4:].lstrip("\n")
    return meta, body


def norm_id(s: str) -> str:
    s = str(s).strip().upper()
    if s == "FINAL":
        return s
    m = re.fullmatch(r"0*(\d+)([ABC]?)", s)
    if not m:
        raise SystemExit(f"Unknown stage id: {s}")
    n, suf = m.groups()
    return f"{int(n)}{suf}" if not suf else f"0{suf}"


def load_stages() -> list[dict]:
    stages = []
    for path in sorted(STAGES_DIR.glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        if meta is None:
            raise SystemExit(f"Stage file without front matter: {path}")
        meta["id"] = norm_id(meta["id"])
        meta["depends_on"] = [norm_id(d) for d in meta.get("depends_on") or []]
        for k in ("artifacts", "checks", "globs"):
            meta[k] = meta.get(k) or []
        meta["approval"] = bool(meta.get("approval"))
        meta["na_allowed"] = bool(meta.get("na_allowed"))
        meta["file"] = path.name
        meta["body"] = body
        stages.append(meta)
    order = {"0A": -3, "0B": -2, "0C": -1, "FINAL": 999}
    stages.sort(key=lambda s: order.get(s["id"], int(s["id"]) if s["id"].isdigit() else 0))
    return stages


STAGES = load_stages()
BY_ID = {s["id"]: s for s in STAGES}


def stage(sid: str) -> dict:
    sid = norm_id(sid)
    if sid not in BY_ID:
        raise SystemExit(f"Unknown stage: {sid}")
    return BY_ID[sid]


def slug(s: dict) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s["name"].lower()).strip("-")[:40].rstrip("-")


def stage_key(s: dict) -> str:
    return s["id"].lower() if not s["id"].isdigit() else f"{int(s['id']):02d}"


def branch_name(s: dict) -> str:
    return f"fde/stage-{stage_key(s)}-{slug(s)}"


def next_stage(s: dict):
    i = STAGES.index(s)
    return STAGES[i + 1] if i + 1 < len(STAGES) else None


# --------------------------------------------------------------------------- state

def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")


def state_path(repo: Path) -> Path:
    return repo / STATE_DIR / "state.json"


def load_state(repo: Path) -> dict:
    p = state_path(repo)
    if not p.exists():
        raise SystemExit(f"Harness not initialised in {repo}. Run: fde.py init --repo {repo}")
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(repo: Path, st: dict) -> None:
    st["updated_at"] = now()
    state_path(repo).write_text(json.dumps(st, indent=2) + "\n", encoding="utf-8")
    _update_registry(repo, st)


def _update_registry(repo: Path, st: dict) -> None:
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    reg = json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {"repositories": {}}
    done = [sid for sid, v in st["stages"].items() if v["status"] in DONE]
    nxt = compute_next(st)
    reg["repositories"][str(repo)] = {
        "engagement": st.get("engagement"),
        "updated_at": st["updated_at"],
        "stages_done": len(done),
        "stages_total": len(STAGES),
        "next_stage": nxt["id"] if nxt else None,
        "blocked": [sid for sid, v in st["stages"].items() if v["status"] == "BLOCKED"],
    }
    REGISTRY.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")


def log_event(repo: Path, msg: str) -> None:
    p = repo / STATE_DIR / "run-log.md"
    with p.open("a", encoding="utf-8") as f:
        f.write(f"- {now()} — {msg}\n")


def compute_next(st: dict):
    for s in STAGES:
        if st["stages"][s["id"]]["status"] not in DONE:
            return s
    return None


def deps_unmet(st: dict, s: dict) -> list[str]:
    return [d for d in s["depends_on"] if st["stages"][d]["status"] not in DONE]


# --------------------------------------------------------------------------- git

def git(repo: Path, *args, check=True) -> str:
    r = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout.strip()


def is_git(repo: Path) -> bool:
    return subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=repo,
                          capture_output=True, text=True).returncode == 0


def head(repo: Path):
    if not is_git(repo):
        return None
    r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def changed_files(repo: Path, base: str) -> list[str]:
    files = set(filter(None, git(repo, "diff", "--name-only", base).splitlines()))
    files |= set(filter(None, git(repo, "ls-files", "--others", "--exclude-standard").splitlines()))
    return sorted(files)


# --------------------------------------------------------------------------- commands

def cmd_init(a) -> None:
    repo = Path(a.repo).resolve()
    if not repo.is_dir():
        raise SystemExit(f"Not a directory: {repo}")
    sd = repo / STATE_DIR
    if state_path(repo).exists() and not a.force:
        raise SystemExit(f"Already initialised: {state_path(repo)} (use --force to reinstall commands only)")
    for d in ("reports", "history", "prompts", "checks"):
        (sd / d).mkdir(parents=True, exist_ok=True)
    if not state_path(repo).exists():
        st = {
            "harness_version": "1.0.0",
            "harness_path": str(HARNESS),
            "engagement": a.engagement or repo.name,
            "author": a.author,
            "test_command": a.test_cmd,
            "initialised_at": now(),
            "initial_commit": head(repo),
            "stages": {s["id"]: {"status": "NOT STARTED", "runs": 0, "folder": s["folder"]} for s in STAGES},
        }
        wb = sd / "write-boundaries.txt"
        wb.write_text(
            "# Human-approved repository write boundaries for WRITE-mode stages (15, 19-22, 24, 26-28, 30, 31).\n"
            "# One glob per line, relative to the repository root, e.g.  backend/**   tests/**\n"
            "# Populate ONLY after Stage 0B proposes them in\n"
            "#   docs/00-preflight/operating-contract/repository-write-boundaries.md\n"
            "# and a human approves them (record the approver below). Empty = no implementation writes allowed.\n"
            "# approved-by:\n# approved-at:\n", encoding="utf-8")
        (sd / "run-log.md").write_text(f"# AI FDE Harness Run Log — {st['engagement']}\n\n", encoding="utf-8")
        (sd / "README.md").write_text(
            "# docs/_harness\n\nHarness state for the AI FDE production-delivery spine. Managed by "
            f"`{FDE}`.\n\n- `state.json` — stage statuses, runs, approvals, base commits\n"
            "- `write-boundaries.txt` — human-approved globs for write-mode stages\n"
            "- `reports/` — stage reports (Required Final Response)\n"
            "- `checks/` — machine gate-check results\n- `prompts/` — rendered prompts as executed (audit)\n"
            "- `history/` — snapshots of earlier stage evidence before re-runs (never edit)\n"
            "- `run-log.md` — append-only event log\n", encoding="utf-8")
        save_state(repo, st)
        log_event(repo, f"initialised harness {HARNESS}")
    install_commands(repo)
    print(f"Initialised AI FDE harness in {sd}")
    print(f"Claude Code commands installed in {repo / '.claude/commands'}: /fde-status /fde-next /fde-stage /fde-check")
    if not is_git(repo):
        print("WARNING: target is not a git repository — boundary checks and evidence versioning are disabled. "
              "Run `git init && git add -A && git commit -m baseline` first (recommended).")


def install_commands(repo: Path) -> None:
    dest = repo / ".claude" / "commands"
    dest.mkdir(parents=True, exist_ok=True)
    for src in (TEMPLATES / "claude-commands").glob("*.md"):
        (dest / src.name).write_text(src.read_text(encoding="utf-8").replace("{{FDE}}", str(FDE)), encoding="utf-8")


def cmd_status(a) -> None:
    repo = Path(a.repo).resolve()
    st = load_state(repo)
    print(f"Engagement: {st['engagement']}   repo: {repo}")
    print(f"{'Stage':<6} {'Status':<17} {'Mode':<9} {'Runs':>4}  {'Approved by':<16} Name")
    for s in STAGES:
        v = st["stages"][s["id"]]
        print(f"{s['id']:<6} {v['status']:<17} {s['mode']:<9} {v.get('runs', 0):>4}  "
              f"{(v.get('approved_by') or ('required' if s['approval'] else '-')):<16} {s['name']}")
    n = compute_next(st)
    print(f"\nNext stage: {n['id'] + ' — ' + n['name'] if n else 'none — spine complete'}")


def cmd_next(a) -> None:
    st = load_state(Path(a.repo).resolve())
    n = compute_next(st)
    print(n["id"] if n else "DONE")


def render_prompt(repo: Path, st: dict, s: dict) -> str:
    v = st["stages"][s["id"]]
    tpl = (TEMPLATES / "stage-prompt.md").read_text(encoding="utf-8")
    author = st.get("author") or "AI FDE agent (Claude Code)"
    run = v.get("runs", 0) or 1
    ctx = {"id": s["id"], "name": s["name"], "date": today(), "author": author, "run": str(run),
           "version": f"{run}.0"}

    def fill(t: str) -> str:
        return re.sub(r"\{\{(\w+)\}\}", lambda m: ctx.get(m.group(1), m.group(0)), t)

    # inputs
    inputs = []
    for d in s["depends_on"]:
        ds = BY_ID[d]
        dv = st["stages"][d]
        folder = repo / "docs" / ds["folder"]
        files = sorted(p.relative_to(repo).as_posix() for p in folder.rglob("*.md")) if folder.exists() else []
        inputs.append(f"- **Stage {d} — {ds['name']}** — status `{dv['status']}`; folder `docs/{ds['folder']}/`; "
                      f"report `docs/_harness/reports/{stage_key(ds)}.md`; {len(files)} artifact(s) present.")
    inputs_txt = "\n".join(inputs) or "- None (first stage)."
    inputs_txt += ("\n\nRead the prior-stage artifacts and reports before starting. Where they are missing or "
                   "BLOCKED, record the gap as an Unknown and lower your confidence accordingly.")

    # artifacts
    arts = [f"- `{x}`" for x in s["artifacts"]]
    for g in s["globs"]:
        pat, _, mn = g.partition("::")
        arts.append(f"- `{pat.strip()}` (at least {mn.strip() or 1})")
    if s["na_allowed"]:
        arts.append("\n**Alternatively**, if Stage 8 did not approve this capability, create only "
                    "`not-applicable.md` (standard header, `status: \"Not Applicable\"`, plus a `## Justification` "
                    "section citing `docs/08-ai-qualification/qualification-decision.md`).")

    # boundaries
    if s["mode"] == "write":
        globs = read_write_boundaries(repo)
        b = (f"This is a **WRITE-mode** stage. Work on branch `{v.get('branch') or branch_name(s)}`.\n\n"
             f"You may modify `docs/{s['folder']}/`, `docs/_harness/reports/`, and implementation paths matching "
             "these human-approved globs from `docs/_harness/write-boundaries.txt`:\n\n"
             + ("\n".join(f"- `{g}`" for g in globs) if globs else
                "- **(none approved)** — you must not change implementation files. Record this as a blocking "
                "issue unless the stage can be completed without implementation changes.")
             + "\n\nCommit each reviewable increment separately with a `fde(" + s["id"] + "): <item-id> <summary>` "
             "message. Run the test command after every increment"
             + (f": `{st['test_command']}`." if st.get("test_command") else ".")
             + " Never rewrite history, force-push or amend earlier commits.")
    else:
        b = (f"This is a **READ-ONLY** stage. You may create or modify files only under `docs/{s['folder']}/` and "
             f"`docs/_harness/reports/`. Everything else in the repository must remain byte-for-byte unchanged "
             "(running read-only commands and existing tests is allowed if they leave no tracked changes).")

    nxt = next_stage(s)
    rep = {
        "repo": str(repo), "mode": s["mode"].upper(), "mode_meaning": MODE_MEANING[s["mode"]],
        "branch": v.get("branch") or (git(repo, "branch", "--show-current", check=False) if is_git(repo) else "n/a"),
        "base": v.get("base_commit") or head(repo) or "n/a",
        "contract": (HARNESS / "CONTRACT.md").read_text(encoding="utf-8").strip(),
        "body": s["body"].strip(),
        "boundaries": b, "inputs": inputs_txt, "folder": s["folder"], "artifacts": "\n".join(arts),
        "artifact_header": fill((TEMPLATES / "artifact-header.md").read_text(encoding="utf-8")).strip(),
        "report_template": fill((TEMPLATES / "stage-report.md").read_text(encoding="utf-8")).strip(),
        "report_name": f"{stage_key(s)}.md", "fde": str(FDE), "next": nxt["id"] if nxt else "(end of spine)",
    }
    ctx.update(rep)
    return fill(tpl)


def read_write_boundaries(repo: Path) -> list[str]:
    p = repo / STATE_DIR / "write-boundaries.txt"
    if not p.exists():
        return []
    return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")]


def cmd_prompt(a) -> None:
    repo = Path(a.repo).resolve()
    st = load_state(repo)
    print(render_prompt(repo, st, stage(a.stage)))


def cmd_begin(a) -> None:
    repo = Path(a.repo).resolve()
    st = load_state(repo)
    if a.stage.lower() == "next":
        n = compute_next(st)
        if n is None:
            raise SystemExit("All stages are complete — nothing to begin.")
        a.stage = n["id"]
    s = stage(a.stage)
    v = st["stages"][s["id"]]
    unmet = deps_unmet(st, s)
    if unmet and not a.force:
        raise SystemExit(f"Stage {s['id']} blocked: dependencies not PASS/CONDITIONAL PASS: {', '.join(unmet)}. "
                         "Complete them first or use --force (recorded in the run log).")
    if s["mode"] == "write" and is_git(repo) and git(repo, "status", "--porcelain"):
        raise SystemExit("Working tree is dirty. Commit or stash changes before beginning a WRITE-mode stage.")

    # preserve earlier evidence before a re-run
    folder = repo / "docs" / s["folder"]
    if folder.exists() and any(folder.rglob("*")):
        snap = repo / STATE_DIR / "history" / stage_key(s) / now().replace(":", "")
        shutil.copytree(folder, snap)
        old_report = repo / STATE_DIR / "reports" / f"{stage_key(s)}.md"
        if old_report.exists():
            shutil.copy2(old_report, snap / "_stage-report.md")
        log_event(repo, f"stage {s['id']}: snapshot of previous evidence → {snap.relative_to(repo)}")

    if s["mode"] == "write" and is_git(repo):
        br = branch_name(s)
        existing = git(repo, "branch", "--list", br)
        git(repo, "checkout", br) if existing else git(repo, "checkout", "-b", br)
        v["branch"] = br
    elif is_git(repo):
        v["branch"] = git(repo, "branch", "--show-current", check=False) or "(detached)"

    v["runs"] = v.get("runs", 0) + 1
    v["status"] = "IN PROGRESS"
    v["started_at"] = now()
    v["base_commit"] = head(repo)
    v.pop("approved_by", None)
    v.pop("completed_at", None)
    if unmet:
        v["forced_with_unmet_dependencies"] = unmet
    save_state(repo, st)
    folder.mkdir(parents=True, exist_ok=True)
    prompt = render_prompt(repo, st, s)
    pf = repo / STATE_DIR / "prompts" / f"{stage_key(s)}-run{v['runs']}.md"
    pf.write_text(prompt, encoding="utf-8")
    log_event(repo, f"stage {s['id']}: begin run {v['runs']} (mode={s['mode']}, base={v['base_commit']}, "
                    f"branch={v.get('branch')}){' FORCED unmet deps ' + ','.join(unmet) if unmet else ''}")
    print(prompt)


def check_artifact(path: Path, s: dict) -> tuple[list[str], list[str]]:
    errs, warns = [], []
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_front_matter(text)
    rel = path.name
    if meta is None:
        return [f"{rel}: missing YAML front-matter header"], warns
    for k in REQUIRED_HEADER_KEYS:
        if k not in meta or meta[k] in ("", [], None):
            errs.append(f"{rel}: header field `{k}` missing or empty")
    if str(meta.get("stage", "")).split(" ")[0].upper().lstrip("0") not in (s["id"].lstrip("0") or "0", s["id"]):
        warns.append(f"{rel}: header `stage` ({meta.get('stage')}) does not name stage {s['id']}")
    if str(meta.get("status", "")).lower() not in ARTIFACT_STATUSES:
        errs.append(f"{rel}: header `status` must be one of {sorted(ARTIFACT_STATUSES)}")
    headings = {h.strip().lower() for h in re.findall(r"^#{2,3}\s+(.+?)\s*$", body, re.M)}
    na = str(meta.get("status", "")).lower() == "not applicable"
    for sec in REQUIRED_SECTIONS:
        if sec.lower() not in headings:
            errs.append(f"{rel}: missing section `## {sec}`")
    if not na and not EVIDENCE_TAGS.search(body):
        warns.append(f"{rel}: no Verified Fact / Inference / Assumption / Unknown classification found")
    if PLACEHOLDER.search(text):
        warns.append(f"{rel}: contains template placeholder / TODO / TBD text")
    if len(body.strip()) < 200:
        warns.append(f"{rel}: body is very short ({len(body.strip())} chars)")
    return errs, warns


def run_check(repo: Path, st: dict, s: dict, run_tests: bool = False) -> dict:
    v = st["stages"][s["id"]]
    folder = repo / "docs" / s["folder"]
    errs, warns, info = [], [], []

    # 1. artifacts (or not-applicable alternative)
    na_file = folder / "not-applicable.md"
    if s["na_allowed"] and na_file.exists():
        e, w = check_artifact(na_file, s)
        errs += e
        warns += w
        if "justification" not in na_file.read_text(encoding="utf-8").lower():
            errs.append("not-applicable.md: missing `## Justification` section")
        info.append("not-applicable path taken")
    else:
        for name in s["artifacts"]:
            p = folder / name
            if not p.exists():
                errs.append(f"missing artifact docs/{s['folder']}/{name}")
                continue
            e, w = check_artifact(p, s)
            errs += e
            warns += w
        for g in s["globs"]:
            pat, _, mn = g.partition("::")
            hits = sorted(folder.glob(pat.strip()))
            if len(hits) < int(mn.strip() or 1):
                errs.append(f"expected at least {mn.strip() or 1} file(s) matching docs/{s['folder']}/{pat.strip()}")
            for h in hits:
                e, w = check_artifact(h, s)
                errs += e
                warns += w
        for c in s["checks"]:
            fname, _, rx = c.partition("::")
            p = folder / fname.strip()
            if p.exists() and not re.search(rx.strip(), p.read_text(encoding="utf-8")):
                errs.append(f"{fname.strip()}: stage gate requires content matching /{rx.strip()}/")

    # 2. stage report
    rp = repo / STATE_DIR / "reports" / f"{stage_key(s)}.md"
    report_status = None
    if not rp.exists():
        errs.append(f"missing stage report docs/_harness/reports/{stage_key(s)}.md")
    else:
        meta, body = parse_front_matter(rp.read_text(encoding="utf-8"))
        report_status = str((meta or {}).get("stage_status", "")).upper()
        if report_status not in STAGE_STATUSES:
            errs.append(f"stage report: stage_status must be one of {STAGE_STATUSES}")
        for sec in REPORT_SECTIONS:
            if not re.search(rf"^##\s+{re.escape(sec)}\s*$", body or "", re.M):
                errs.append(f"stage report: missing section `## {sec}`")

    # 3. write boundaries
    if is_git(repo) and v.get("base_commit"):
        allowed_docs = [f"docs/{s['folder']}/*", f"{STATE_DIR}/*"]
        globs = read_write_boundaries(repo) if s["mode"] == "write" else []
        protected = ["docs/legacy/*"] + [f"docs/{o['folder']}/*" for o in STAGES if o["id"] != s["id"]]
        for f in changed_files(repo, v["base_commit"]):
            if any(fnmatch.fnmatch(f, g) for g in allowed_docs):
                continue
            if f.startswith(".claude/commands/fde-"):
                continue
            if any(fnmatch.fnmatch(f, g) for g in protected):
                errs.append(f"boundary: {f} belongs to another stage / legacy docs and must not be changed")
            elif s["mode"] == "write" and any(fnmatch.fnmatch(f, g) for g in globs):
                info.append(f"changed (approved boundary): {f}")
            else:
                errs.append(f"boundary: {f} changed outside {'approved write boundaries' if s['mode'] == 'write' else 'this read-only stage'}")
        if s["mode"] == "write":
            commits = git(repo, "log", "--format=%h %s", f"{v['base_commit']}..HEAD").splitlines()
            bad = [c for c in commits if not re.search(r"\bfde\(", c)]
            if bad:
                warns.append(f"commits without `fde(<stage>):` convention: {bad[:5]}")
            info.append(f"{len(commits)} commit(s) on stage branch since base")
    elif not is_git(repo):
        warns.append("not a git repository — boundary check skipped (evidence is not version-controlled)")

    # 4. tests
    if run_tests:
        cmd = st.get("test_command")
        if not cmd:
            warns.append("--run-tests given but no test_command configured (fde.py config --test-cmd ...)")
        else:
            r = subprocess.run(cmd, shell=True, cwd=repo, capture_output=True, text=True)
            tail = (r.stdout + r.stderr).strip().splitlines()[-15:]
            (errs if r.returncode else info).append(f"test command `{cmd}` exit={r.returncode}: " + " | ".join(tail[-3:]))

    if report_status == "BLOCKED":
        result = "BLOCKED"
    elif errs:
        result = "FAIL"
    else:
        result = report_status or "FAIL"
    out = {"stage": s["id"], "checked_at": now(), "result": result, "report_status": report_status,
           "errors": errs, "warnings": warns, "info": info}
    (repo / STATE_DIR / "checks" / f"{stage_key(s)}.json").write_text(json.dumps(out, indent=2) + "\n")
    return out


def cmd_check(a) -> None:
    repo = Path(a.repo).resolve()
    st = load_state(repo)
    s = stage(a.stage)
    out = run_check(repo, st, s, a.run_tests)
    st["stages"][s["id"]]["last_check"] = {"at": out["checked_at"], "result": out["result"],
                                           "errors": len(out["errors"]), "warnings": len(out["warnings"])}
    save_state(repo, st)
    print(f"Stage {s['id']} gate check: {out['result']}  ({len(out['errors'])} error(s), {len(out['warnings'])} warning(s))")
    for e in out["errors"]:
        print(f"  ERROR   {e}")
    for w in out["warnings"]:
        print(f"  WARN    {w}")
    for i in out["info"]:
        print(f"  INFO    {i}")
    sys.exit(0 if out["result"] in DONE else 1)


def cmd_complete(a) -> None:
    repo = Path(a.repo).resolve()
    st = load_state(repo)
    s = stage(a.stage)
    v = st["stages"][s["id"]]
    out = run_check(repo, st, s)
    if out["result"] == "BLOCKED":
        v["status"] = "BLOCKED"
        save_state(repo, st)
        log_event(repo, f"stage {s['id']}: recorded BLOCKED (stage report)")
        raise SystemExit(f"Stage {s['id']} recorded as BLOCKED per its stage report.")
    if out["result"] not in DONE:
        raise SystemExit(f"Gate check failed for stage {s['id']}; run `fde.py check {s['id']}` for details.")
    if s["approval"] and not a.approved_by:
        raise SystemExit(f"Stage {s['id']} is a human-approval gate: pass --approved-by \"<name/role>\".")
    v["status"] = out["result"]
    v["completed_at"] = now()
    if a.approved_by:
        v["approved_by"] = a.approved_by
    save_state(repo, st)
    log_event(repo, f"stage {s['id']}: completed {v['status']}" + (f", approved by {a.approved_by}" if a.approved_by else ""))
    if a.commit and is_git(repo):
        git(repo, "add", "--", f"docs/{s['folder']}", STATE_DIR)
        msg = f"fde({s['id']}): complete stage {s['id']} — {s['name']} [{v['status']}]"
        if a.approved_by:
            msg += f"\n\nApproved-by: {a.approved_by}"
        if git(repo, "diff", "--cached", "--name-only"):
            git(repo, "commit", "-m", msg)
    n = compute_next(st)
    print(f"Stage {s['id']} → {v['status']}. Next: {n['id'] + ' — ' + n['name'] if n else 'spine complete'}")


def cmd_config(a) -> None:
    repo = Path(a.repo).resolve()
    st = load_state(repo)
    for k in ("author", "test_command", "engagement"):
        val = getattr(a, k, None)
        if val is not None:
            st[k] = val
    save_state(repo, st)
    print(json.dumps({k: st.get(k) for k in ("engagement", "author", "test_command")}, indent=2))


def cmd_run(a) -> None:
    """Headless execution through Claude Code: begin + `claude -p` + check."""
    repo = Path(a.repo).resolve()
    if not shutil.which("claude"):
        raise SystemExit("`claude` CLI not found on PATH.")
    st = load_state(repo)
    s = stage(a.stage)
    import contextlib, io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cmd_begin(a)
    prompt = buf.getvalue()
    print(f"Running stage {s['id']} headless via claude -p (permission mode: {a.permission_mode}) ...", flush=True)
    r = subprocess.run(["claude", "-p", prompt, "--permission-mode", a.permission_mode], cwd=repo)
    if r.returncode != 0:
        raise SystemExit(f"claude exited {r.returncode}")
    out = run_check(repo, load_state(repo), s)
    print(f"Gate check: {out['result']} ({len(out['errors'])} errors). Review, then: "
          f"fde.py complete {s['id']} --repo {repo}{' --approved-by NAME' if s['approval'] else ''} --commit")


def cmd_manifest(a) -> None:
    print(json.dumps([{k: v for k, v in s.items() if k != "body"} for s in STAGES], indent=2))


def cmd_lint(a) -> None:
    problems = []
    ids = [s["id"] for s in STAGES]
    if len(ids) != len(set(ids)):
        problems.append("duplicate stage ids")
    folders = [s["folder"] for s in STAGES]
    if len(folders) != len(set(folders)):
        problems.append("duplicate stage folders")
    for s in STAGES:
        for d in s["depends_on"]:
            if d not in BY_ID:
                problems.append(f"{s['id']}: unknown dependency {d}")
            elif STAGES.index(BY_ID[d]) >= STAGES.index(s):
                problems.append(f"{s['id']}: depends on later stage {d}")
        if s["mode"] not in MODE_MEANING:
            problems.append(f"{s['id']}: bad mode {s['mode']}")
        if not s["artifacts"]:
            problems.append(f"{s['id']}: no artifacts")
        if len(set(s["artifacts"])) != len(s["artifacts"]):
            problems.append(f"{s['id']}: duplicate artifact names")
        for sec in ("## Objective", "## Constraints / Guardrails", "## Stage-Specific Completion Gate",
                    "## Lifecycle Linkage"):
            if sec not in s["body"]:
                problems.append(f"{s['id']}: missing `{sec}`")
        for c in s["checks"]:
            try:
                re.compile(c.partition("::")[2].strip())
            except re.error as e:
                problems.append(f"{s['id']}: bad regex {c}: {e}")
    total = sum(len(s["artifacts"]) for s in STAGES)
    print(f"{len(STAGES)} stages, {total} named artifacts (+ ADRs / feature specs).")
    if problems:
        print("\n".join(f"  PROBLEM {p}" for p in problems))
        sys.exit(1)
    print("Harness lint OK")


def main(argv=None) -> None:
    p = argparse.ArgumentParser(prog="fde.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(name, fn, stage_arg=False, repo=True):
        sp = sub.add_parser(name)
        if stage_arg:
            sp.add_argument("stage")
        if repo:
            sp.add_argument("--repo", default=".")
        sp.set_defaults(fn=fn)
        return sp

    sp = add("init", cmd_init)
    sp.add_argument("--author")
    sp.add_argument("--engagement")
    sp.add_argument("--test-cmd")
    sp.add_argument("--force", action="store_true")
    add("status", cmd_status)
    add("next", cmd_next)
    add("prompt", cmd_prompt, True)
    add("begin", cmd_begin, True).add_argument("--force", action="store_true")
    add("check", cmd_check, True).add_argument("--run-tests", action="store_true")
    sp = add("complete", cmd_complete, True)
    sp.add_argument("--approved-by")
    sp.add_argument("--commit", action="store_true")
    sp = add("config", cmd_config)
    sp.add_argument("--author")
    sp.add_argument("--test-cmd", dest="test_command")
    sp.add_argument("--engagement")
    sp = add("run", cmd_run, True)
    sp.add_argument("--force", action="store_true")
    sp.add_argument("--permission-mode", default="acceptEdits")
    add("manifest", cmd_manifest, repo=False)
    add("lint", cmd_lint, repo=False)
    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
