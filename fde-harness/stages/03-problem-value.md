---
id: 3
name: Frame Problem & Value
folder: 03-problem-value
mode: read-only
depends_on: [1, 2]
approval: false
artifacts:
  - problem-framing-canvas.md
  - problem-statement.md
  - personas.md
  - jobs-to-be-done.md
  - user-journeys.md
  - scope-exclusions.md
  - business-requirements.md
  - nfrs.md
  - success-criteria.md
  - value-hypothesis.md
  - assumptions-register.md
---
## Objective

Translate stakeholder pain into a precise business problem **independent of any preferred technology**.

Use evidence from: Stages 1–2; business change requests, workflows and data in the repository.

## Scope

Separate symptom, root problem, proposed solution and assumed AI need. Define personas, jobs-to-be-done, journeys, scope, exclusions, requirements, NFRs and measurable success/failure criteria.

## Required Analysis

Evaluate:
1. Symptom vs root problem vs proposed solution vs assumed AI need.
2. Personas and JTBD grounded in evidence.
3. Current journeys and pain points.
4. Business requirements and NFRs (each with a stable ID, e.g. `BR-001`, `NFR-001`).
5. Measurable success and failure criteria.
6. Value hypothesis and its assumptions.

## Constraints / Guardrails

Do not: name technologies, models or AI techniques in the problem statement; treat a proposed solution as a requirement.

## Stage-Specific Completion Gate

- `problem-statement.md` is technology-neutral.
- Every requirement has an ID and a source (stakeholder or evidence).
- Success criteria are measurable (metric, threshold, timeframe).

## Lifecycle Linkage

- Uses Stages 1–2. Feeds Stage 4 (KPIs), Stage 8 (qualification) and Stage 9 (PRD).
