---
id: 20
name: Application & Services Engineering
folder: 20-application
mode: write
depends_on: [12, 18]
approval: false
artifacts:
  - application-component-map.md
  - api-implementation-map.md
  - state-model.md
  - business-logic-map.md
  - deterministic-ai-boundary.md
  - error-handling-implementation.md
  - access-control-implementation.md
  - application-test-summary.md
  - application-readiness.md
---
## Objective

Implement UI, APIs, business logic, persistence and application services according to specifications.

Use evidence from: Stage 12 specs, Stage 18 delivery plan.

## Scope

Validation, errors, authentication, authorization, idempotency, accessibility, auditability and observability hooks. Keep deterministic business logic separate from probabilistic AI behaviour.

## Brownfield Change Protocol

Same as Stage 15: paths in `write-boundaries.txt`; tests first for changed behaviour; one work item per commit (`fde(20): WI-### <summary>`); run the suite; log results in `application-test-summary.md`.

## Constraints / Guardrails

Do not: implement beyond the specs; embed AI calls inside deterministic business rules; weaken existing authorization.

## Stage-Specific Completion Gate

- Every implemented API maps to a Stage 12 contract in `api-implementation-map.md`.
- `deterministic-ai-boundary.md` shows where the boundary is enforced in code (file paths).

## Lifecycle Linkage

- Implements Stage 12. Feeds Stages 21, 23, 24.
