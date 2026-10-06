# AI FDE Spine — Stage 0B — Provisional Operating Contract & Engineering Boundaries

| Field | Value |
|---|---|
| Target repository | `/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/01-bfsi-lending-aml-servicing` |
| Run date (UTC) | 2026-10-06 |
| Author / agent | Engagement Lead / Claude Code |
| Stage mode | **READ-ONLY** — do not modify application code, tests, dependencies, configuration, infrastructure, data or workflows; write only this stage's docs folder and the harness report |
| Git branch | `main` |
| Base commit | `863a1f807781d2c19b49b27fb2ad182a574ab1df` |
| Run number | 1 |

## Global Workshop Execution Contract

Apply this to every stage:

**Analyse / Execute → Generate Required Artifacts → Save to Defined Repository Path → Cite Evidence → Record Assumptions & Unknowns → Validate Completion Gate → Proceed**

Every generated artifact must:

- state stage, date/version, author/agent, status and evidence source;
- distinguish **Verified Fact / Inference / Assumption / Unknown** where relevant;
- reference actual repository paths, tests, schemas, logs, configurations or approved stakeholder evidence where applicable;
- include unresolved issues and residual risks;
- never claim completion when required evidence is missing;
- be version-controlled;
- not overwrite prior evidence silently;
- preserve earlier baselines so before/after comparison remains possible.

Discovery stages are read-only unless the prompt explicitly authorizes modification.

---

## Objective

Create a **provisional** engagement operating contract from currently available evidence, defining what the engagement may and may not do, so that later stages act inside explicit, reviewable boundaries.

Use evidence from:
- Stage 0A discovery artifacts (`docs/00-preflight/discovery/`);
- repository configuration, environments, data descriptors and inherited documentation.

## Scope

Define:
- current scope and exclusions; repositories and environments in play;
- data boundaries and data-use constraints (including synthetic vs real data, PII handling);
- permitted and prohibited actions; repository write restrictions; production-access restrictions;
- security/privacy constraints;
- provisional tool and agent permissions;
- evidence requirements and change-control expectations;
- human-approval triggers, stop conditions and escalation assumptions.

Exclude: final governance authority, final ownership assignments and the steady-state operating model (Stage 37).

## Required Analysis

Evaluate:
1. Which repository paths are safe to modify later and under which stage (write boundaries).
2. Which environments exist or are implied, and what access is permissible.
3. Data classes present and constraints on their use.
4. Which actions require explicit human approval.
5. Conditions under which work must stop and escalate.
6. Governance decisions that cannot be made yet and who would plausibly confirm them.

## Constraints / Guardrails

Do not:
- invent owners, approvers or decision rights — mark unresolved ownership or decision rights as **PROVISIONAL**;
- treat any provisional decision as final authority;
- modify anything outside `docs/00-preflight/operating-contract/`.

Only:
- derive boundaries from evidence and record their basis.

Preserve: the repository exactly as found.

`repository-write-boundaries.md` must list concrete path globs that later write stages (15, 19–22, 24, 26–28, 30, 31) may change. These are **proposals**: a human transfers approved globs into `docs/_harness/write-boundaries.txt`, which is what the harness enforces.

## Stage-Specific Completion Gate

- Every ownership/decision-right statement without evidence is labelled PROVISIONAL.
- `open-governance-decisions.md` explicitly flags items requiring confirmation during Stages 2, 23, 25 and 37.
- `stop-conditions.md` lists concrete, testable stop conditions.
- `operating-contract-readiness.md` states whether the contract is sufficient to proceed, with gaps.
- Human approval recorded at completion (`fde.py complete 0B --approved-by ...`).

## Lifecycle Linkage

- Uses Stage 0A evidence.
- Confirmed or updated in Stage 2 (authority), Stage 23 (human control), Stage 25 (governance) and closed in Stage 37 (operating model).
- Stage 15 may modify implementation only within approved 0B boundaries.

---

## Evidence Rules

Classify every material statement as one of:

- **Verified Fact** — directly observed in the repository, a command output, a test result or approved stakeholder evidence. Cite it.
- **Inference** — reasoned from verified facts. Name the facts it rests on.
- **Assumption** — taken as true without evidence. Record it in the artifact's Assumptions section.
- **Unknown** — not determinable from available evidence. Record it; do not invent an answer.

Inline tags such as `[Verified Fact]`, `[Inference]`, `[Assumption]` and `[Unknown]` are preferred.

Where repository/system evidence exists, reference file paths (with line numbers where useful), configuration, APIs, schemas, tests, logs, database objects, architecture artifacts and approved stakeholder evidence. Do not present assumptions as facts.

For every material finding: state the finding; provide evidence; identify impact; identify risk; identify confidence (High / Medium / Low); identify unresolved questions.

---

## Write Boundaries (enforced by `fde.py check`)

This is a **READ-ONLY** stage. You may create or modify files only under `docs/00-preflight/operating-contract/` and `docs/_harness/reports/`. Everything else in the repository must remain byte-for-byte unchanged (running read-only commands and existing tests is allowed if they leave no tracked changes).

Never modify `docs/legacy/` or another stage's `docs/` folder. Earlier evidence is preserved by the harness under `docs/_harness/history/`; do not delete or silently rewrite it. If you are re-running this stage, bump each artifact's `version` and add a `## Change Log` entry that explains what changed and why.

---

## Prior-Stage Inputs

- **Stage 0A — Pre-Flight Repository & System Orientation** — status `PASS`; folder `docs/00-preflight/discovery/`; report `docs/_harness/reports/0a.md`; 12 artifact(s) present.

Read the prior-stage artifacts and reports before starting. Where they are missing or BLOCKED, record the gap as an Unknown and lower your confidence accordingly.

---

## Required Artifacts

Create the directory `docs/00-preflight/operating-contract/` and save:

- `provisional-operating-contract.md`
- `scope-boundaries.md`
- `repository-write-boundaries.md`
- `environment-access-boundaries.md`
- `data-use-constraints.md`
- `provisional-tool-agent-permissions.md`
- `provisional-human-approval-rules.md`
- `evidence-contract.md`
- `change-control-rules.md`
- `stop-conditions.md`
- `open-governance-decisions.md`
- `operating-contract-readiness.md`

Every artifact must start with this header (YAML front matter) and contain the mandatory sections:

```markdown
---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "<artifact title>"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"            # Draft | Provisional | In Review | Approved | Superseded | Not Applicable
evidence_sources:
  - "<repo path, test, command output or approved stakeholder evidence>"
---

# <Artifact title>

<body — tag statements as [Verified Fact] / [Inference] / [Assumption] / [Unknown] and cite evidence>

## Assumptions

## Unresolved Issues

## Residual Risks
```

---

## Completion Gate (generic — applies in addition to the stage-specific gate above)

The stage is complete only when:

- all required artifacts exist under `docs/00-preflight/operating-contract/` with valid headers and mandatory sections;
- critical gaps are resolved or explicitly documented as blocking;
- evidence supports the stage conclusion;
- no file outside the write boundaries above has been changed;
- `python3 "/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/fde-harness/bin/fde.py" check 0B --repo "/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/01-bfsi-lending-aml-servicing"` passes.

Do not proceed to Stage 0C if any blocking condition remains. Do not run `fde.py complete` yourself — completion (and any approval) is recorded by a human.

---

## Required Final Response

Write the stage report to `docs/_harness/reports/0b.md` using exactly this template, then run the check command above and fix any failures:

```markdown
---
stage: "0B"
stage_name: "Provisional Operating Contract & Engineering Boundaries"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
run: 1
stage_status: "PASS"       # PASS | CONDITIONAL PASS | BLOCKED
---

# Stage 0B Report — Provisional Operating Contract & Engineering Boundaries

## 1. Stage Status

## 2. Key Findings

## 3. Major Risks

## 4. Assumptions / Unknowns

## 5. Artifacts Created

## 6. Blocking Issues

## 7. Recommended Next Action
```

Then return to the user, in this order:

1. Stage status: **PASS / CONDITIONAL PASS / BLOCKED**
2. Key findings
3. Major risks
4. Assumptions / unknowns
5. Artifacts created
6. Blocking issues
7. Recommended next action
