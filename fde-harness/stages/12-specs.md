---
id: 12
name: Spec-Driven Design
folder: 12-specs
mode: read-only
depends_on: [9, 10, 11]
approval: false
artifacts:
  - system-spec.md
  - api-contracts.md
  - event-contracts.md
  - schema-specifications.md
  - interface-contracts.md
  - business-rules.md
  - error-handling-spec.md
  - security-spec.md
  - observability-spec.md
  - nfr-spec.md
  - acceptance-criteria.md
  - spec-readiness.md
globs:
  - "features/*.md :: 1"
---
## Objective

Convert approved product intent and architecture into implementation-ready specifications **before coding**.

Use evidence from: Stages 9–11 and existing code/contracts in the repository.

## Scope

Feature/system behaviour, APIs, events, schemas, state transitions, business rules, errors, constraints, security, observability, NFRs and acceptance criteria. Feature-specific specs go in `docs/12-specs/features/<feature-slug>.md` (standard header required).

## Required Analysis

Evaluate:
1. System behaviour and state transitions.
2. API, event, schema and interface contracts (state which existing contracts are preserved vs changed).
3. Business rules (each with an ID `RULE-###`, its source and whether it is current behaviour or an intended change).
4. Error handling, security and observability specifications.
5. Acceptance criteria (Given/When/Then, IDs `AC-###`).

## Constraints / Guardrails

Do not: implement anything; **do not specify around material ambiguity** — record it in `spec-readiness.md` as blocking.

## Stage-Specific Completion Gate

- At least one feature spec exists under `features/`.
- Every FR from Stage 9 is covered by a spec or explicitly deferred.
- `spec-readiness.md` lists material ambiguities; any unresolved material ambiguity makes the stage BLOCKED or CONDITIONAL PASS.

## Lifecycle Linkage

- Uses Stages 9–11. Feeds Stage 13 (traceability), 14, 18, 20.
