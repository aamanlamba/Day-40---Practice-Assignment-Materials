---
id: 34
name: Measure After-Intervention KPIs
folder: 34-after-kpis
mode: read-only
depends_on: [4, 31]
approval: false
artifacts:
  - after-intervention-kpi-sheet.md
  - production-performance-report.md
  - adoption-metrics.md
  - exception-metrics.md
  - human-override-metrics.md
  - measurement-data-quality.md
  - kpi-comparability-check.md
---
## Objective

Measure production performance using the metric definitions **frozen in Stage 4**.

Use evidence from: Stage 4 KPI dictionary, Stage 31 telemetry, production data.

## Scope

Successes, failures, exceptions, overrides and adoption. Confirm measurement-window and population comparability before making claims.

## Constraints / Guardrails

Do not: **change KPI definitions to improve results**; claim improvement before comparability is confirmed.

## Stage-Specific Completion Gate

- Every KPI uses the Stage 4 definition verbatim (cite the KPI ID and version).
- `kpi-comparability-check.md` states comparable / not comparable per KPI.

## Lifecycle Linkage

- Uses Stage 4. Feeds Stage 35.
