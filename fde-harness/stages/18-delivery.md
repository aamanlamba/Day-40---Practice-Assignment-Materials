---
id: 18
name: Evidence-Driven Delivery Planning
folder: 18-delivery
mode: read-only
depends_on: [12, 13, 17]
approval: false
artifacts:
  - delivery-backlog.md
  - increment-plan.md
  - ownership-map.md
  - definition-of-done.md
  - acceptance-test-plan.md
  - evaluation-rubric.md
  - evidence-checklist.md
  - delivery-dependencies.md
  - delivery-risk-register.md
---
## Objective

Translate the Implementation PRD and specifications into executable increments where **no work item is complete without its required evidence**.

Use evidence from: Stages 12, 13 and 17.

## Scope

Stories/tasks, dependencies, owners, tests, evaluation datasets, acceptance conditions, Definition of Done and evidence requirements.

## Required Analysis

Each work item (`WI-###`) lists: linked requirement/spec IDs, tests/evaluations, required evidence, owner (or PROVISIONAL), dependencies.

## Constraints / Guardrails

Do not: create work items without traceability; assign owners without evidence.

## Stage-Specific Completion Gate

- Every WI maps to a requirement and declares its required evidence.
- `definition-of-done.md` includes evidence requirements.

## Lifecycle Linkage

- Uses Stages 12, 13, 17. Drives Stages 19–22.
