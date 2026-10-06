# AI FDE Spine — Stage 0A — Pre-Flight Repository & System Orientation

| Field | Value |
|---|---|
| Target repository | `/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/01-bfsi-lending-aml-servicing` |
| Run date (UTC) | 2026-10-06 |
| Author / agent | Aaman Lamba / Claude Code |
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

Establish a high-level factual orientation of the existing brownfield environment **before changing anything**, so that the engagement can be qualified (Stage 1) without making transformation recommendations.

Use evidence from:
- the repository tree, README/operational notes, manifests and build files;
- source code, configuration, schemas, SQL, data descriptors and scripts;
- existing tests, CI definitions, observability assets and inherited documentation.

## Scope

Analyse across:
- repository structure, technologies, languages, frameworks and dependency manifests;
- applications, services, APIs and their entry points;
- databases, schemas, ETL/data pipelines and batch jobs;
- integrations, adapters and external interfaces;
- tests, security mechanisms, observability, runtime/deployment clues;
- major business workflows the system appears to support.

Include: what is clearly present, what appears operational, what is unknown, and where deeper investigation is required.

Exclude: deep refactoring analysis, code-quality scoring, technical-debt registers and any transformation recommendation (these belong to Stage 7 and later).

## Required Analysis

Evaluate:
1. Repository layout and component boundaries (as observed, not as intended).
2. Technology inventory with versions where declared.
3. Runtime topology: what runs, how it is started, what it talks to.
4. Data stores, data flows and pipeline/batch behaviour.
5. Integration points and protocols.
6. Business workflows inferred from code, data and docs.
7. Test assets: what exists, what they appear to cover (do not judge quality yet).
8. Security and observability mechanisms present or visibly absent.
9. Risks visible at orientation depth.

## Constraints / Guardrails

Do not:
- modify application code, tests, dependencies, configuration, infrastructure, data or workflows;
- install dependencies into the repository, run migrations, or start processes that write to repository data;
- perform deep refactoring analysis or recommend transformations;
- invent owners, purposes or behaviours not supported by evidence.

Only:
- read files, list directories, inspect git history, and run strictly read-only commands;
- write under `docs/00-preflight/discovery/` and the harness report.

Preserve: the repository exactly as found.

## Stage-Specific Completion Gate

- Orientation is sufficient to conduct engagement qualification (Stage 1).
- Every component listed in `system-landscape.md` cites at least one repository path.
- `assumptions-unknowns.md` separates Assumptions from Unknowns, and each Unknown says where deeper investigation is required.
- `initial-risk-register.md` lists risks with likelihood, impact and evidence.
- No transformation recommendations appear in any artifact.

## Lifecycle Linkage

- First stage of the spine; no prior inputs.
- Feeds Stage 0B (boundaries), 0C (economics envelope), Stage 1 (qualification) and Stage 5 (current state).
- Deep repository assessment is intentionally deferred to Stage 7.

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

This is a **READ-ONLY** stage. You may create or modify files only under `docs/00-preflight/discovery/` and `docs/_harness/reports/`. Everything else in the repository must remain byte-for-byte unchanged (running read-only commands and existing tests is allowed if they leave no tracked changes).

Never modify `docs/legacy/` or another stage's `docs/` folder. Earlier evidence is preserved by the harness under `docs/_harness/history/`; do not delete or silently rewrite it. If you are re-running this stage, bump each artifact's `version` and add a `## Change Log` entry that explains what changed and why.

---

## Prior-Stage Inputs

- None (first stage).

Read the prior-stage artifacts and reports before starting. Where they are missing or BLOCKED, record the gap as an Unknown and lower your confidence accordingly.

---

## Required Artifacts

Create the directory `docs/00-preflight/discovery/` and save:

- `repository-overview.md`
- `system-landscape.md`
- `technology-inventory.md`
- `high-level-architecture.md`
- `integration-overview.md`
- `data-flow-overview.md`
- `workflow-overview.md`
- `test-overview.md`
- `security-observability-overview.md`
- `assumptions-unknowns.md`
- `initial-risk-register.md`
- `discovery-summary.md`

Every artifact must start with this header (YAML front matter) and contain the mandatory sections:

```markdown
---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "<artifact title>"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
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

- all required artifacts exist under `docs/00-preflight/discovery/` with valid headers and mandatory sections;
- critical gaps are resolved or explicitly documented as blocking;
- evidence supports the stage conclusion;
- no file outside the write boundaries above has been changed;
- `python3 "/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/fde-harness/bin/fde.py" check 0A --repo "/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/01-bfsi-lending-aml-servicing"` passes.

Do not proceed to Stage 0B if any blocking condition remains. Do not run `fde.py complete` yourself — completion (and any approval) is recorded by a human.

---

## Required Final Response

Write the stage report to `docs/_harness/reports/0a.md` using exactly this template, then run the check command above and fix any failures:

```markdown
---
stage: "0A"
stage_name: "Pre-Flight Repository & System Orientation"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
run: 1
stage_status: "PASS"       # PASS | CONDITIONAL PASS | BLOCKED
---

# Stage 0A Report — Pre-Flight Repository & System Orientation

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
