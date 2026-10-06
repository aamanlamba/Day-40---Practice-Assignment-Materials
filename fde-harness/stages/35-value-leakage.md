---
id: 35
name: Before-vs-After Variance + Value Leakage
folder: 35-value-leakage
mode: read-only
depends_on: [4, 34]
approval: false
artifacts:
  - before-after-analysis.md
  - kpi-variance-table.md
  - benefit-variance.md
  - value-leakage-analysis.md
  - confounder-analysis.md
  - causal-findings.md
  - adoption-leakage.md
  - cost-leakage.md
  - corrective-action-backlog.md
---
## Objective

Compare Stage 4 and Stage 34 using frozen definitions and comparable populations.

## Scope

Quantify improvement, deterioration and deviation from expected benefit. Identify leakage from low adoption, overrides, errors, rework, latency, control friction, AI/infrastructure cost or workflow displacement.

## Constraints / Guardrails

Do not: attribute all change to the intervention where confounders exist; compare non-comparable KPIs.

## Stage-Specific Completion Gate

- Each variance is accompanied by a confounder assessment.

## Lifecycle Linkage

- Uses Stages 4 and 34. Feeds Stage 36.
