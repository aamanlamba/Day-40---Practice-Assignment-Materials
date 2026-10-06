---
id: 30
name: Release / Cutover / Rollback
folder: 30-release
mode: write
depends_on: [14, 26, 27, 29]
approval: true
artifacts:
  - release-plan.md
  - environment-promotion-plan.md
  - deployment-strategy.md
  - feature-flag-plan.md
  - cutover-checklist.md
  - go-no-go-criteria.md
  - rollback-plan.md
  - backup-validation.md
  - release-approvals.md
  - deployment-evidence.md
  - release-outcome.md
---
## Objective

Prepare a controlled production release.

Use evidence from: Stage 14 cutover/rollback strategy, Stages 26–29.

## Scope

Environment promotion, approvals, deployment method, feature flags, canary/phased release where appropriate, migration, validation, monitoring, go/no-go criteria and rollback triggers.

## Brownfield Change Protocol

Release configuration (e.g. deployment manifests, flags) follows the Stage 15 protocol (`fde(30): <summary>`). Tag the release commit locally (`fde-release-<version>`) only after human approval.

## Constraints / Guardrails

Do not: deploy to any real environment without explicit human approval recorded in `release-approvals.md`; skip **backup and rollback verification before cutover**.

## Stage-Specific Completion Gate

- `backup-validation.md` shows a verified backup and rollback rehearsal (or BLOCKED).
- Human approval recorded at completion.

## Lifecycle Linkage

- Feeds Stages 31, 34.
