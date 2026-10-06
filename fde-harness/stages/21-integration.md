---
id: 21
name: Enterprise Integration
folder: 21-integration
mode: write
depends_on: [11, 20]
approval: false
artifacts:
  - integration-inventory.md
  - api-contracts.md
  - data-contracts.md
  - event-contracts.md
  - adapter-map.md
  - authentication-map.md
  - failure-semantics.md
  - reconciliation-rules.md
  - integration-test-results.md
  - integration-readiness.md
---
## Objective

Integrate systems of record, legacy applications, APIs, databases, events and enterprise workflows.

Use evidence from: Stage 11 contracts, Stage 20 implementation, existing adapters.

## Scope

Validate authentication, authorization, schemas, contracts, retries, idempotency, reconciliation, timeout behaviour, stale data, duplicates and dependency failures.

## Brownfield Change Protocol

Same as Stage 15; commits `fde(21): WI-### <summary>`. Preserve legacy interface behaviour unless a spec approves a change.

## Constraints / Guardrails

Do not: call real external systems; break existing adapter contracts silently.

## Stage-Specific Completion Gate

- Each integration has documented failure semantics and a test result.

## Lifecycle Linkage

- Uses Stages 11, 20. Feeds Stages 24, 28.
