# AI FDE Production Delivery Spine — Guided Prompt Harness

A repository-agnostic harness that walks an AI agent (Claude Code) through every stage of the **AI FDE End-to-End Production Delivery Spine** against an input brownfield repository. It:

- renders each stage as a full prompt in the **Prompt Template** structure (Objective → Scope → Required Analysis → Evidence Rules → Constraints → Required Artifacts → Completion Gate → Required Final Response) with the **Global Workshop Execution Contract** prepended and the eight **Prompt Anatomy** elements present;
- stores results in the target repo's `docs/` spine exactly as the Spine defines (`docs/00-preflight/discovery/` … `docs/final-prd/`);
- tracks harness state per repository (`docs/_harness/`) and across repositories (`state/registry.json`);
- enforces **completion gates** mechanically: required artifacts, artifact headers, mandatory sections, stage-specific content rules, stage report, and dependency order;
- makes **brownfield updates in a structured manner**: read-only stages may only write their own docs folder; write stages run on a dedicated branch, may only touch human-approved paths, one `fde(<stage>): <item>` commit per increment, tests after each increment;
- **never overwrites prior evidence silently**: re-running a stage snapshots the previous evidence into `docs/_harness/history/` first.

Python 3.9+ standard library only. No dependencies.

## Layout

```
fde-harness/
├── CONTRACT.md                 Global Workshop Execution Contract (prepended to every prompt)
├── stages/                     46 stage prompts (0A, 0B, 0C, 1–42, FINAL)
│   └── NN-<folder>.md          front matter = machine-readable stage spec; body = stage-specific prompt
├── templates/
│   ├── stage-prompt.md         Prompt Template wrapper (evidence rules, boundaries, artifacts, gate, final response)
│   ├── artifact-header.md      mandatory header + sections for every artifact
│   ├── stage-report.md         Required Final Response, saved as docs/_harness/reports/<stage>.md
│   └── claude-commands/        /fde-status /fde-next /fde-stage /fde-check (installed into the target repo)
├── bin/fde.py                  runner: init · status · next · begin · prompt · check · complete · config · run · manifest · lint
├── state/registry.json         cross-repository progress registry
└── tests/test_fde.py           end-to-end tests on throwaway git repos
```

### Stage file front matter

```yaml
id: 15
name: Transform Bad Repo → Good Repo
folder: 15-modernization           # → docs/15-modernization/
mode: write                        # read-only | write
depends_on: [0B, 7, 14]            # lifecycle linkage; gates `begin`
approval: true                     # `complete` requires --approved-by
na_allowed: false                  # true → not-applicable.md may replace the artifact set (Stages 19, 22)
artifacts: [...]                   # exact file names from the Spine
globs:  ["adrs/ADR-*.md :: 1"]     # additional pattern-based artifacts with a minimum count
checks: ["file.md :: <regex>"]     # stage-specific gate content rules
```

Edit a stage by editing its file; `python3 bin/fde.py lint` validates the whole harness.

## Quick start

```bash
H=/path/to/fde-harness/bin/fde.py
cd /path/to/target-repo
git status                              # target must be a git repo with a clean baseline commit

python3 $H init --repo . --author "Your Name / Claude Code" --test-cmd "python -m pytest"
git add -A && git commit -m "chore: install AI FDE harness"

# Interactive (recommended) — inside Claude Code in the target repo:
/fde-next            # begins the next pending stage and executes its prompt
/fde-stage 0A        # or a specific stage
/fde-check 0A        # re-run the gate check and fix failures
/fde-status

# Human records completion (and approval where required):
python3 $H complete 0A --repo . --commit
python3 $H complete 0B --repo . --approved-by "Engagement Lead" --commit
```

Headless alternative (one stage per `claude -p` call; review before `complete`):

```bash
python3 $H run 0A --repo . --permission-mode acceptEdits
```

Manual alternative (any agent): `python3 $H begin 0A --repo . > prompt.md`, paste the prompt into the agent, then `check` and `complete`.

## Stage lifecycle

```
NOT STARTED ──begin──▶ IN PROGRESS ──agent writes artifacts + report──▶ check ──▶ complete ──▶ PASS / CONDITIONAL PASS
                          │                                                         │
                          └── re-run: begin again → previous evidence snapshotted    └── report says BLOCKED → BLOCKED
```

| Command | What it does |
|---|---|
| `init` | Creates `docs/_harness/` (state, write-boundaries, reports, checks, prompts, history, run log) and installs the Claude Code commands. |
| `begin <id\|next>` | Refuses if dependencies are not PASS/CONDITIONAL PASS (`--force` overrides and is recorded). Snapshots existing stage evidence to `history/`. For write stages: requires a clean tree and creates/checks out `fde/stage-<NN>-<slug>`. Records base commit, increments run, prints and saves the rendered prompt. |
| `prompt <id>` | Renders the prompt without changing state (preview). |
| `check <id> [--run-tests]` | Gate check → `docs/_harness/checks/<id>.json`. Exit 0 only on PASS/CONDITIONAL PASS. |
| `complete <id> [--approved-by] [--commit]` | Re-runs the check, records status/approval, optionally commits stage docs + state as `fde(<id>): complete stage …`. |
| `status` / `next` | Progress table / next pending stage id. |
| `config` | Set `--author`, `--test-cmd`, `--engagement`. |
| `manifest` / `lint` | Dump the parsed stage specs as JSON / validate the harness. |

## What the gate check enforces

1. **Artifacts** — every Spine-named file exists in `docs/<folder>/` (plus ADR / feature-spec globs; or a justified `not-applicable.md` for Stages 19 and 22).
2. **Artifact header** — YAML front matter with `stage, title, version, date, author, status, evidence_sources`; status in `Draft | Provisional | In Review | Approved | Superseded | Not Applicable`.
3. **Mandatory sections** — `## Assumptions`, `## Unresolved Issues`, `## Residual Risks`.
4. **Stage-specific rules** — e.g. Stage 0B uses `PROVISIONAL` and flags Stages 2/23/25/37; Stage 1 states `Classification: Go | Conditional Go | No-Go`; Stage 4 declares definitions frozen; Stage 10 has ≥1 ADR; FINAL dispositions requirements as Delivered/Changed/Deferred/Rejected/Superseded.
5. **Stage report** — `docs/_harness/reports/<id>.md` with `stage_status` and the seven Required Final Response sections. A `BLOCKED` report blocks the stage.
6. **Write boundaries** (git diff from the stage's base commit, including untracked files):
   - read-only stages → only `docs/<own folder>/` and `docs/_harness/`;
   - write stages → additionally the globs in `docs/_harness/write-boundaries.txt` (empty until a human approves Stage 0B's proposal);
   - always protected → `docs/legacy/` and every other stage's folder (prior evidence cannot be rewritten from a later stage).
7. **Commit convention** (write stages) — warns on commits without `fde(<stage>):`.
8. **Warnings** (non-blocking) — no Verified Fact/Inference/Assumption/Unknown classification, leftover placeholders/TODO/TBD, very short artifacts.

The check validates *structure and boundaries*; it cannot judge whether the analysis is correct. Human review at `complete` — mandatory at approval stages — is the quality gate for content.

## Human approval gates

`complete` requires `--approved-by` at: 0B, 1, 4, 8, 14, 15, 17, 23, 25, 30, 36, 37, 38, FINAL — the points where the Spine freezes baselines, authorises change, grants autonomy, releases, or transfers ownership. Approving 0B/14 is also when a human populates `docs/_harness/write-boundaries.txt`.

## Brownfield change protocol (write stages)

Write stages (15, 19, 20, 21, 22, 24, 26, 27, 28, 30, 31) embed this protocol in their prompts:

1. `begin` → clean tree required → branch `fde/stage-<NN>-<slug>` from current HEAD; base commit recorded.
2. Work one backlog item (`TX-###` / `WI-###`) at a time; paths must be in `write-boundaries.txt`.
3. Characterize behaviour first (tests pass on unchanged code) → smallest change → run tests.
4. One commit per item: `fde(<stage>): <item-id> <summary>`; log commit SHA, files, tests, rollback step in the stage's log artifact.
5. Any behaviour change must cite an approved spec ID, otherwise revert.
6. `check` proves every changed file is inside the boundary; a human reviews and merges the stage branch.

## Stage index

| Stage | Name | Mode | Approval | Depends on | Output folder | Artifacts |
|---|---|---|---|---|---|---|
| 0A | Pre-Flight Repository & System Orientation | read-only | — | — | `docs/00-preflight/discovery/` | 12 |
| 0B | Provisional Operating Contract & Engineering Boundaries | read-only | yes | 0A | `docs/00-preflight/operating-contract/` | 12 |
| 0C | Provisional Token Efficiency & AI Economics Envelope | read-only | — | 0A, 0B | `docs/00-preflight/ai-economics/` | 13 |
| 1 | Engage & Qualify | read-only | yes | 0A, 0B, 0C | `docs/01-engagement/` | 7 |
| 2 | Stakeholder Discovery & Authority Confirmation | read-only | — | 0B, 1 | `docs/02-stakeholders/` | 7 |
| 3 | Frame Problem & Value | read-only | — | 1, 2 | `docs/03-problem-value/` | 11 |
| 4 | Capture Before-AI / Before-Intervention KPIs | read-only | yes | 3 | `docs/04-baseline-kpis/` | 8 |
| 5 | Discover Current Process & Brownfield Landscape | read-only | — | 0A, 3, 4 | `docs/05-current-state/` | 10 |
| 6 | Root-Cause Analysis | read-only | — | 4, 5 | `docs/06-root-cause/` | 8 |
| 7 | Deep Brownfield Repository Assessment & Behaviour Baseline | read-only | — | 0A, 5, 6 | `docs/07-repo-assessment/` | 13 |
| 8 | AI-vs-No-AI Qualification | read-only | yes | 0C, 3, 6, 7 | `docs/08-ai-qualification/` | 8 |
| 9 | Initial PRD / Product Intent | read-only | — | 3, 6, 8 | `docs/09-initial-prd/` | 10 |
| 10 | Target Architecture + ADRs | read-only | — | 7, 8, 9 | `docs/10-architecture/` | 9 + ADRs |
| 11 | Data, Knowledge & Context Strategy | read-only | — | 9, 10 | `docs/11-data-context/` | 12 |
| 12 | Spec-Driven Design | read-only | — | 9, 10, 11 | `docs/12-specs/` | 12 + feature specs |
| 13 | Requirements → Specs → Tests → Evidence Traceability | read-only | — | 9, 12 | `docs/13-traceability/` | 10 |
| 14 | Transformation / Migration Plan | read-only | yes | 7, 10, 13 | `docs/14-transformation/` | 11 |
| 15 | Transform Bad Repo → Good Repo | write | yes | 0B, 7, 14 | `docs/15-modernization/` | 9 |
| 16 | Validate the Good Repo | read-only | — | 7, 10, 12, 15 | `docs/16-repo-validation/` | 10 |
| 17 | Finalise Implementation PRD | read-only | yes | 9, 10, 16 | `docs/17-implementation-prd/` | 8 |
| 18 | Evidence-Driven Delivery Planning | read-only | — | 12, 13, 17 | `docs/18-delivery/` | 9 |
| 19 | Intelligence Core — Prompt, Retrieval & Model Engineering | write | — | 8, 11, 18 | `docs/19-intelligence/` | 12 or N/A |
| 20 | Application & Services Engineering | write | — | 12, 18 | `docs/20-application/` | 9 |
| 21 | Enterprise Integration | write | — | 11, 20 | `docs/21-integration/` | 10 |
| 22 | Agent, Tool, Harness, Loop & Graph Engineering | write | — | 8, 19, 20 | `docs/22-agentic-engineering/` | 15 or N/A |
| 23 | HITL/HOTL & Deterministic Control Boundaries | read-only | yes | 0B, 8, 20 | `docs/23-human-control/` | 10 |
| 24 | Security + Privacy + Responsible AI by Design | write | — | 10, 21, 23 | `docs/24-security-privacy/` | 12 |
| 25 | Governance + Compliance + Assurance | read-only | yes | 0B, 2, 24 | `docs/25-governance/` | 12 |
| 26 | TEVV + AI Red Teaming | write | — | 13, 19, 22, 24, 25 | `docs/26-tevv/` | 13 |
| 27 | Production Hardening | write | — | 24, 26 | `docs/27-hardening/` | 11 |
| 28 | Reliability & Resilience Engineering | write | — | 21, 27 | `docs/28-resilience/` | 11 |
| 29 | AI Incident Response + BC/DR | read-only | — | 28 | `docs/29-incident-bcdr/` | 13 |
| 30 | Release / Cutover / Rollback | write | yes | 14, 26, 27, 29 | `docs/30-release/` | 11 |
| 31 | Observability + SLO/SLA Engineering | write | — | 30 | `docs/31-observability/` | 12 |
| 32 | Token Efficiency + AI FinOps + TCO | read-only | — | 0C, 8, 31 | `docs/32-finops/` | 13 |
| 33 | Vendor / Third-Party / Concentration Risk | read-only | — | 10, 32 | `docs/33-vendor-risk/` | 10 |
| 34 | Measure After-Intervention KPIs | read-only | — | 4, 31 | `docs/34-after-kpis/` | 7 |
| 35 | Before-vs-After Variance + Value Leakage | read-only | — | 4, 34 | `docs/35-value-leakage/` | 9 |
| 36 | ROI / NPV / Benefits Realisation | read-only | yes | 32, 35 | `docs/36-benefits/` | 11 |
| 37 | Target Operating Model + RACI + Ownership | read-only | yes | 0B, 2, 23, 25 | `docs/37-operating-model/` | 13 |
| 38 | Handover + Knowledge Transfer | read-only | yes | 29, 31, 37 | `docs/38-handover/` | 11 |
| 39 | Drift + Continuous Improvement | read-only | — | 31, 38 | `docs/39-continuous-improvement/` | 11 |
| 40 | Scale / 90-Day Transformation Roadmap | read-only | — | 36, 39 | `docs/40-scale/` | 9 |
| 41 | Retirement / Decommissioning | read-only | — | 33, 40 | `docs/41-retirement/` | 10 |
| 42 | Executive Defence & Final Value Story | read-only | — | 26, 36, 40, 41 | `docs/42-executive/` | 14 |
| FINAL | Authoritative Final As-Built PRD | read-only | yes | 9, 17, 42 | `docs/final-prd/` | 19 |

## Harness decisions beyond the Spine text

These are choices the harness makes where the Spine is silent; they are easy to change in the stage files or `fde.py`:

- **Stage 19 N/A path** — the Spine only defines `not-applicable.md` for Stage 22; the harness also allows it for Stage 19 when Stage 8 approved no GenAI/ML capability, to avoid inventing intelligence artifacts.
- **Dependencies** are explicit lifecycle links (not strict sequential order); `next` still proposes stages in Spine order.
- **Approval stages** and **write/read-only modes** are inferred from the Spine's wording ("Do not refactor during this stage", "Modify implementation only within approved Stage 0B boundaries", sign-off artifacts).
- **IDs** (`BR-`, `FR-`, `NFR-`, `RULE-`, `AC-`, `TX-`, `WI-`, `ADR-`) are introduced so traceability (Stage 13) and disposition (FINAL) can be checked.

## Tests

```bash
python3 -m unittest discover -s fde-harness/tests -v
```
