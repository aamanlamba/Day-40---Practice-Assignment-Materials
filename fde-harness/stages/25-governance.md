---
id: 25
name: Governance + Compliance + Assurance
folder: 25-governance
mode: read-only
depends_on: [0B, 2, 24]
approval: true
artifacts:
  - compliance-obligations.md
  - compliance-control-matrix.md
  - governance-model.md
  - accountability-map.md
  - ai-system-register.md
  - model-card.md
  - system-card.md
  - risk-acceptance-register.md
  - evidence-retention-policy.md
  - audit-evidence-index.md
  - operating-contract-governance-updates.md
  - governance-readiness.md
---
## Objective

Map applicable regulatory, contractual, organizational and AI-governance obligations to controls, owners, evidence and approval points.

Use evidence from: Stages 0B, 2, 23, 24.

## Scope

Accountability, registration, change control, risk acceptance, auditability and evidence retention.

## Constraints / Guardrails

Do not: claim legal compliance — record obligations as identified and controls as mapped; invent owners.

## Stage-Specific Completion Gate

- `operating-contract-governance-updates.md` confirms or updates every 0B item flagged for Stage 25.
- `audit-evidence-index.md` links each obligation to evidence paths.
- Human approval recorded at completion.

## Lifecycle Linkage

- Feeds Stages 26, 37, FINAL.
