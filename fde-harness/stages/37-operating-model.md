---
id: 37
name: Target Operating Model + RACI + Ownership
folder: 37-operating-model
mode: read-only
depends_on: [0B, 2, 23, 25]
approval: true
artifacts:
  - target-operating-model.md
  - raci.md
  - service-ownership-map.md
  - model-ownership.md
  - data-ownership.md
  - agent-tool-ownership.md
  - security-ownership.md
  - finops-ownership.md
  - support-model.md
  - change-governance.md
  - decision-rights.md
  - escalation-model.md
  - operating-contract-closure.md
---
## Objective

Convert the temporary Stage 0B engagement contract into steady-state production ownership.

Use evidence from: Stages 0B, 2, 23, 25.

## Scope

Responsibility for application, data, models, prompts, retrieval, agents/tools where applicable, security, incidents, observability, costs, vendors, governance and business outcomes. Support tiers, change approval, service ownership, escalation and decision rights.

## Constraints / Guardrails

Do not: assign named owners without evidence of acceptance — unaccepted assignments remain open items.

## Stage-Specific Completion Gate

- `operating-contract-closure.md` closes or transfers every 0B item, including those flagged for Stage 37.
- Human approval recorded at completion.

## Lifecycle Linkage

- Closes 0B. Feeds Stages 38, FINAL.
