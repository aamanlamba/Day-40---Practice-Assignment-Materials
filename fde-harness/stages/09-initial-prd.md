---
id: 9
name: Initial PRD / Product Intent
folder: 09-initial-prd
mode: read-only
depends_on: [3, 6, 8]
approval: false
artifacts:
  - initial-prd.md
  - capability-map.md
  - functional-requirements.md
  - nfrs.md
  - mvp-scope.md
  - non-goals.md
  - release-hypothesis.md
  - product-risks.md
  - open-product-decisions.md
  - initial-prd-traceability.md
---
## Objective

Create the Initial PRD from validated discovery and qualification.

Use evidence from: Stages 3, 6 and 8 (and earlier stages as cited).

## Scope

Define problem, personas, journeys, capabilities, functional requirements, NFRs, exclusions, constraints, dependencies, success metrics, risks, MVP scope, future scope and unresolved questions.

## Required Analysis

Evaluate:
1. Capabilities derived from confirmed root causes and the Stage 8 decision.
2. Functional requirements (IDs `FR-###`) and NFRs (IDs `NFR-###`), each traced to a Stage 3 business requirement and evidence.
3. MVP scope vs future scope vs non-goals.
4. Product risks and open decisions.

## Constraints / Guardrails

Do not: introduce AI capabilities rejected in Stage 8; include requirements without a traced business problem.

## Stage-Specific Completion Gate

- `initial-prd-traceability.md` maps every FR/NFR to a business problem and evidence; untraced items are flagged.

## Lifecycle Linkage

- Uses Stages 3, 6, 8. Reconciled in Stage 17 (implementation PRD) and FINAL (as-built PRD).
