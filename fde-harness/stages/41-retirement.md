---
id: 41
name: Retirement / Decommissioning
folder: 41-retirement
mode: read-only
depends_on: [33, 40]
approval: false
artifacts:
  - retirement-criteria.md
  - dependency-clearance.md
  - data-retention-plan.md
  - archive-plan.md
  - legal-hold-check.md
  - access-revocation-plan.md
  - secret-key-revocation.md
  - vendor-termination-plan.md
  - decommission-checklist.md
  - retirement-evidence.md
---
## Objective

Define safe retirement criteria for models, prompts, indexes, APIs, agents/tools, applications, databases, infrastructure and vendors.

## Scope

Retention, legal hold, archival, dependency removal, access/key revocation, migration, contracts and audit evidence.

## Constraints / Guardrails

Do not: delete anything in this stage; **confirm no live dependency remains before any deletion** is planned.

## Stage-Specific Completion Gate

- Every retirement candidate has a dependency-clearance result.

## Lifecycle Linkage

- Feeds Stage 42, FINAL.
