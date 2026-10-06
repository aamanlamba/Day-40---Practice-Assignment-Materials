# AI FDE Spine — Stage 0C — Provisional Token Efficiency & AI Economics Envelope

| Field | Value |
|---|---|
| Target repository | `/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/01-bfsi-lending-aml-servicing` |
| Run date (UTC) | 2026-10-06 |
| Author / agent | Engagement Lead / Claude Code |
| Stage mode | **READ-ONLY** — do not modify application code, tests, dependencies, configuration, infrastructure, data or workflows; write only this stage's docs folder and the harness report |
| Git branch | `main` |
| Base commit | `a9c558882ede5efd563ccff83e8c1cda74dca30b` |
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

Establish a provisional economic and resource envelope **without assuming that AI has already been justified**, producing design constraints (cost, latency, context, loop limits) that later stages must respect or explicitly revise.

Use evidence from:
- Stage 0A discovery (workloads, data volumes, workflows) and Stage 0B constraints;
- data volumes, logs, metrics or batch schedules present in the repository.

## Scope

Create scenarios for:
- deterministic software;
- conventional automation;
- GenAI;
- agentic AI (where relevant).

For each, estimate where evidence allows: workload volume, context size, model calls, input/output/retrieval/tool tokens, agent-loop overhead, retries, latency and infrastructure consumption.

Exclude: selecting a solution, selecting a model/vendor, or claiming AI is required.

## Required Analysis

Evaluate:
1. Workload volume and shape (per request, per case, per batch).
2. Token-flow and context-size scenarios per solution type.
3. Agent-loop and retry overhead scenarios.
4. Cost scenarios (low / expected / high) with explicit unit-price assumptions.
5. Maximum acceptable cost/request, cost/case, latency, context size and agent-loop limits as **provisional design constraints**.
6. Preliminary FinOps baseline and TCO including non-AI costs and human effort.

## Constraints / Guardrails

Do not:
- present estimates as measurements — clearly separate measured data from assumptions;
- assume AI is justified; deterministic and conventional scenarios must be costed with the same rigour;
- quote vendor prices without date and source, or mark them Assumption.

Only: estimate where enough evidence exists; otherwise record Unknown.

Preserve: the repository exactly as found.

## Stage-Specific Completion Gate

- Every numeric figure is tagged Measured / Estimated / Assumption with source.
- `quality-latency-cost-envelope.md` states provisional maximums as design constraints.
- `economics-readiness.md` states which AI-specific portions are contingent on Stage 8.

## Lifecycle Linkage

- Uses 0A and 0B.
- Stage 8 determines whether AI-specific portions remain applicable and reconciles this envelope.
- Stage 32 measures actual economics against the applicable 0C scenario.

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

This is a **READ-ONLY** stage. You may create or modify files only under `docs/00-preflight/ai-economics/` and `docs/_harness/reports/`. Everything else in the repository must remain byte-for-byte unchanged (running read-only commands and existing tests is allowed if they leave no tracked changes).

Never modify `docs/legacy/` or another stage's `docs/` folder. Earlier evidence is preserved by the harness under `docs/_harness/history/`; do not delete or silently rewrite it. If you are re-running this stage, bump each artifact's `version` and add a `## Change Log` entry that explains what changed and why.

---

## Prior-Stage Inputs

- **Stage 0A — Pre-Flight Repository & System Orientation** — status `PASS`; folder `docs/00-preflight/discovery/`; report `docs/_harness/reports/0a.md`; 12 artifact(s) present.
- **Stage 0B — Provisional Operating Contract & Engineering Boundaries** — status `PASS`; folder `docs/00-preflight/operating-contract/`; report `docs/_harness/reports/0b.md`; 12 artifact(s) present.

Read the prior-stage artifacts and reports before starting. Where they are missing or BLOCKED, record the gap as an Unknown and lower your confidence accordingly.

---

## Required Artifacts

Create the directory `docs/00-preflight/ai-economics/` and save:

- `workload-assumptions.md`
- `solution-scenarios.md`
- `provisional-model-call-inventory.md`
- `token-flow-scenarios.md`
- `provisional-token-budget.md`
- `provisional-context-budget.md`
- `provisional-loop-budget.md`
- `volume-assumptions.md`
- `cost-scenarios.md`
- `quality-latency-cost-envelope.md`
- `preliminary-finops-baseline.md`
- `preliminary-tco.md`
- `economics-readiness.md`

Every artifact must start with this header (YAML front matter) and contain the mandatory sections:

```markdown
---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
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

- all required artifacts exist under `docs/00-preflight/ai-economics/` with valid headers and mandatory sections;
- critical gaps are resolved or explicitly documented as blocking;
- evidence supports the stage conclusion;
- no file outside the write boundaries above has been changed;
- `python3 "/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/fde-harness/bin/fde.py" check 0C --repo "/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/01-bfsi-lending-aml-servicing"` passes.

Do not proceed to Stage 1 if any blocking condition remains. Do not run `fde.py complete` yourself — completion (and any approval) is recorded by a human.

---

## Required Final Response

Write the stage report to `docs/_harness/reports/0c.md` using exactly this template, then run the check command above and fix any failures:

```markdown
---
stage: "0C"
stage_name: "Provisional Token Efficiency & AI Economics Envelope"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
run: 1
stage_status: "PASS"       # PASS | CONDITIONAL PASS | BLOCKED
---

# Stage 0C Report — Provisional Token Efficiency & AI Economics Envelope

## 1. Stage Status

## 2. Key Findings

## 3. Major Risks

## 4. Assumptions / Unknowns

## 5. Artifacts Created

## 6. Blocking Issues

## 7. Recommended Next Action

## 8. Open Questions

| Question | Ask | Resolve in |
|---|---|---|
```

Then return to the user, in this order:

1. Stage status: **PASS / CONDITIONAL PASS / BLOCKED**
2. Key findings
3. Major risks
4. Assumptions / unknowns
5. Artifacts created
6. Blocking issues
7. Recommended next action
8. Open questions (also listed in the report's `## 8. Open Questions` table, columns Question / Ask / Resolve in; the harness appends them to `docs/_harness/open-questions.md` on completion; write `None` if there are none)
