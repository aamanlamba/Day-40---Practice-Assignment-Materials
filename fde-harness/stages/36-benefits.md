---
id: 36
name: ROI / NPV / Benefits Realisation
folder: 36-benefits
mode: read-only
depends_on: [32, 35]
approval: true
artifacts:
  - benefit-assumptions.md
  - verified-benefits.md
  - cost-model.md
  - roi-model.md
  - npv-model.md
  - payback-analysis.md
  - scenario-analysis.md
  - sensitivity-analysis.md
  - double-counting-check.md
  - benefits-realisation-dashboard-spec.md
  - benefits-signoff.md
---
## Objective

Translate **only verified improvements** into financial value.

Use evidence from: Stages 32 and 35.

## Scope

Adoption, productivity, quality, risk, revenue/cost effects, model/token/infrastructure costs and human oversight. Optimistic, expected and downside scenarios.

## Constraints / Guardrails

Do not: double-count benefits already captured in other metrics; value unverified improvements (list them separately as unverified).

## Stage-Specific Completion Gate

- Every financial figure traces to a verified benefit or a stated assumption with sensitivity.
- Human approval recorded at completion.

## Lifecycle Linkage

- Feeds Stages 40, 42, FINAL.
