---
id: 23
name: HITL/HOTL & Deterministic Control Boundaries
folder: 23-human-control
mode: read-only
depends_on: [0B, 8, 20]
approval: true
artifacts:
  - autonomy-matrix.md
  - deterministic-control-rules.md
  - hitl-workflow.md
  - hotl-workflow.md
  - approval-gates.md
  - human-override-policy.md
  - confidence-handling.md
  - escalation-matrix.md
  - operating-contract-updates.md
  - human-control-test-results.md
---
## Objective

Classify material decisions/actions by autonomy level and define human-control workflows.

Use evidence from: Stage 0B provisional controls, Stage 8 decision, Stages 20–22 implementation.

## Scope

Define what remains deterministic, what AI may recommend, what AI may execute after validation, what requires explicit human approval and what must **never be delegated**.

## Required Analysis

Autonomy matrix per decision/action; HITL and HOTL workflows; confidence handling; override and escalation; test evidence that controls work (or a plan where not yet testable).

## Constraints / Guardrails

Do not: grant autonomy beyond Stage 8 minimum agency; edit Stage 0B artifacts (record updates in `operating-contract-updates.md`).

## Stage-Specific Completion Gate

- `operating-contract-updates.md` dispositions every 0B item flagged for Stage 23.
- Human approval recorded at completion.

## Lifecycle Linkage

- Reconciles 0B; feeds 24, 25, 37.
