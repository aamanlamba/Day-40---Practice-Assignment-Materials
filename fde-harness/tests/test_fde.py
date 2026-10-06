"""End-to-end tests for the AI FDE harness using throwaway git repositories.

Run:  python3 -m unittest discover -s fde-harness/tests -v
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HARNESS = Path(__file__).resolve().parents[1]
FDE = HARNESS / "bin" / "fde.py"
sys.path.insert(0, str(HARNESS / "bin"))
import fde  # noqa: E402


def sh(cwd, *cmd, ok=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       env={**os.environ, "FDE_REGISTRY": str(Path(cwd) / ".." / "registry.json")})
    if ok and r.returncode != 0:
        raise AssertionError(f"{cmd} failed:\n{r.stdout}\n{r.stderr}")
    return r


def fake_artifact(stage_id, title, extra=""):
    return f"""---
stage: "{stage_id} — test"
title: "{title}"
version: "1.0"
date: "2026-01-01"
author: "test-agent"
status: "Draft"
evidence_sources:
  - "app/main.py"
---

# {title}

[Verified Fact] The application entry point is `app/main.py` (line 1). [Inference] It is a small service.
[Assumption] It runs locally. [Unknown] Production topology. {extra}
{"Filler sentence for length. " * 8}

## Assumptions

- Runs locally.

## Unresolved Issues

- None.

## Residual Risks

- Low.
"""


def report(stage_id, status="PASS"):
    secs = "\n\n".join(f"## {s}\n\ntext" for s in fde.REPORT_SECTIONS)
    return f'---\nstage: "{stage_id}"\nstage_status: "{status}"\n---\n\n# Report\n\n{secs}\n'


class HarnessTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name) / "repo"
        (self.repo / "app").mkdir(parents=True)
        (self.repo / "app" / "main.py").write_text("print('hi')\n")
        (self.repo / "docs" / "legacy").mkdir(parents=True)
        (self.repo / "docs" / "legacy" / "notes.md").write_text("legacy\n")
        sh(self.repo, "git", "init", "-q", "-b", "main")
        sh(self.repo, "git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qam", "x", "--allow-empty")
        sh(self.repo, "git", "add", "-A")
        sh(self.repo, "git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "baseline")
        sh(self.repo, sys.executable, FDE, "init", "--repo", ".", "--author", "tester")
        sh(self.repo, "git", "add", "-A")
        sh(self.repo, "git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "harness")

    def tearDown(self):
        self.tmp.cleanup()

    def fde(self, *args, ok=True):
        return sh(self.repo, sys.executable, FDE, *args, "--repo", ".", ok=ok)

    def fill(self, sid, extra=None):
        s = fde.stage(sid)
        folder = self.repo / "docs" / s["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        for a in s["artifacts"]:
            (folder / a).write_text(fake_artifact(s["id"], a, (extra or {}).get(a, "")))
        (self.repo / "docs/_harness/reports" / f"{fde.stage_key(s)}.md").write_text(report(s["id"]))

    def state(self):
        return json.loads((self.repo / "docs/_harness/state.json").read_text())

    # ------------------------------------------------------------------ tests
    def test_lint(self):
        self.assertEqual(sh(HARNESS, sys.executable, FDE, "lint").returncode, 0)

    def test_init_installs_commands_and_state(self):
        self.assertTrue((self.repo / ".claude/commands/fde-stage.md").exists())
        self.assertIn(str(FDE), (self.repo / ".claude/commands/fde-stage.md").read_text())
        self.assertEqual(self.state()["stages"]["0A"]["status"], "NOT STARTED")
        self.assertEqual(self.fde("next").stdout.strip(), "0A")

    def test_full_cycle_0a(self):
        out = self.fde("begin", "0A").stdout
        for needle in ("Global Workshop Execution Contract", "repository-overview.md", "READ-ONLY",
                       "Required Final Response", "docs/00-preflight/discovery/"):
            self.assertIn(needle, out)
        self.assertNotRegex(out, r"\{\{\w+\}\}")
        self.assertEqual(self.fde("check", "0A", ok=False).returncode, 1)
        self.fill("0A")
        r = self.fde("check", "0A")
        self.assertIn("PASS", r.stdout)
        self.fde("complete", "0A", "--commit")
        self.assertEqual(self.state()["stages"]["0A"]["status"], "PASS")
        self.assertEqual(self.fde("next").stdout.strip(), "0B")
        self.assertIn("fde(0A)", sh(self.repo, "git", "log", "-1", "--format=%s").stdout)

    def test_read_only_boundary_violation(self):
        self.fde("begin", "0A")
        self.fill("0A")
        (self.repo / "app" / "main.py").write_text("print('changed')\n")
        r = self.fde("check", "0A", ok=False)
        self.assertIn("boundary: app/main.py", r.stdout)
        (self.repo / "app" / "main.py").write_text("print('hi')\n")
        (self.repo / "docs/legacy/notes.md").write_text("tampered\n")
        self.assertIn("docs/legacy/notes.md", self.fde("check", "0A", ok=False).stdout)

    def test_dependency_gate_and_force(self):
        r = self.fde("begin", "1", ok=False)
        self.assertIn("dependencies not PASS", r.stderr)
        self.fde("begin", "1", "--force")
        self.assertEqual(self.state()["stages"]["1"]["forced_with_unmet_dependencies"], ["0A", "0B", "0C"])

    def test_header_and_section_validation(self):
        self.fde("begin", "0A")
        self.fill("0A")
        p = self.repo / "docs/00-preflight/discovery/repository-overview.md"
        p.write_text(p.read_text().replace("## Residual Risks", "## Something").replace('author: "test-agent"\n', ""))
        out = self.fde("check", "0A", ok=False).stdout
        self.assertIn("header field `author`", out)
        self.assertIn("missing section `## Residual Risks`", out)

    def test_stage_specific_content_check(self):
        """Stage 1 requires an explicit Go / Conditional Go / No-Go classification line."""
        self.fde("begin", "1", "--force")
        self.fill("1")
        out = self.fde("check", "1", ok=False).stdout
        self.assertIn("engagement-go-no-go.md: stage gate requires", out)
        p = self.repo / "docs/01-engagement/engagement-go-no-go.md"
        p.write_text(p.read_text().replace("# engagement-go-no-go.md", "# Decision\n\n**Classification:** Conditional Go"))
        self.assertEqual(self.fde("check", "1").returncode, 0)

    def test_approval_required(self):
        self.fde("begin", "0A"); self.fill("0A"); self.fde("complete", "0A", "--commit")
        self.fde("begin", "0B")
        self.fill("0B", {"provisional-operating-contract.md": "PROVISIONAL",
                         "open-governance-decisions.md": "Stage 2, Stage 23, Stage 25, Stage 37"})
        r = self.fde("complete", "0B", ok=False)
        self.assertIn("--approved-by", r.stderr)
        self.fde("complete", "0B", "--approved-by", "Engagement Lead", "--commit")
        self.assertEqual(self.state()["stages"]["0B"]["approved_by"], "Engagement Lead")

    def test_rerun_snapshots_history(self):
        self.fde("begin", "0A"); self.fill("0A"); self.fde("complete", "0A", "--commit")
        self.fde("begin", "0A")
        hist = list((self.repo / "docs/_harness/history/0a").iterdir())
        self.assertEqual(len(hist), 1)
        self.assertTrue((hist[0] / "repository-overview.md").exists())
        self.assertTrue((hist[0] / "_stage-report.md").exists())
        self.assertEqual(self.state()["stages"]["0A"]["runs"], 2)

    def test_write_stage_branch_and_boundaries(self):
        r = self.fde("begin", "15", "--force")
        self.assertIn("(none approved)", r.stdout)
        self.assertEqual(sh(self.repo, "git", "branch", "--show-current").stdout.strip(),
                         "fde/stage-15-transform-bad-repo-good-repo")
        self.fill("15")
        (self.repo / "app" / "main.py").write_text("print('refactored')\n")
        sh(self.repo, "git", "add", "-A")
        sh(self.repo, "git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "fde(15): TX-001 refactor")
        self.assertIn("outside approved write boundaries", self.fde("check", "15", ok=False).stdout)
        wb = self.repo / "docs/_harness/write-boundaries.txt"
        wb.write_text(wb.read_text() + "app/*\n")
        out = self.fde("check", "15").stdout
        self.assertIn("changed (approved boundary): app/main.py", out)

    def test_write_stage_requires_clean_tree(self):
        (self.repo / "app" / "scratch.py").write_text("x=1\n")
        self.assertIn("dirty", self.fde("begin", "15", "--force", ok=False).stderr)

    def test_not_applicable_path(self):
        self.fde("begin", "22", "--force")
        d = self.repo / "docs/22-agentic-engineering"
        (d / "not-applicable.md").write_text(fake_artifact("22", "Not applicable").replace(
            'status: "Draft"', 'status: "Not Applicable"').replace(
            "## Assumptions", "## Justification\n\nStage 8 rejected agentic AI.\n\n## Assumptions"))
        (self.repo / "docs/_harness/reports/22.md").write_text(report("22", "PASS"))
        out = self.fde("check", "22").stdout
        self.assertIn("not-applicable path taken", out)

    def test_blocked_report(self):
        self.fde("begin", "0A"); self.fill("0A")
        (self.repo / "docs/_harness/reports/0a.md").write_text(report("0A", "BLOCKED"))
        self.fde("complete", "0A", ok=False)
        self.assertEqual(self.state()["stages"]["0A"]["status"], "BLOCKED")

    def test_adr_glob_required(self):
        self.fde("begin", "10", "--force"); self.fill("10")
        self.assertIn("adrs/ADR-*.md", self.fde("check", "10", ok=False).stdout)
        (self.repo / "docs/10-architecture/adrs").mkdir()
        (self.repo / "docs/10-architecture/adrs/ADR-001-x.md").write_text(fake_artifact("10", "ADR-001"))
        self.assertEqual(self.fde("check", "10").returncode, 0)


if __name__ == "__main__":
    unittest.main()
