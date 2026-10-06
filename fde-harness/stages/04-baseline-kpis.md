---
id: 4
name: Capture Before-AI / Before-Intervention KPIs
folder: 04-baseline-kpis
mode: read-only
depends_on: [3]
approval: true
artifacts:
  - kpi-dictionary.md
  - baseline-kpi-sheet.md
  - measurement-methodology.md
  - data-source-map.md
  - baseline-data-quality.md
  - proxy-metrics.md
  - baseline-evidence.md
  - kpi-baseline-signoff.md
checks:
  - "kpi-dictionary.md :: (?i)formula"
  - "kpi-baseline-signoff.md :: (?i)frozen"
---
## Objective

Establish the current-state measurement baseline **before any intervention** and freeze metric definitions for later comparison (Stages 34–35).

Use evidence from: Stage 3 success criteria; data files, metrics, logs and reports in the repository.

## Scope

For each KPI define: name, meaning, formula, unit, owner, source, measurement period, segmentation and current value. Cover cycle time, effort, error, rework, quality, throughput, leakage, compliance, cost, adoption and relevant domain metrics.

## Required Analysis

Evaluate:
1. KPI definitions traced to Stage 3 success criteria.
2. Current values computed from repository data where possible (record the exact query/script/command used in `baseline-evidence.md`).
3. Measurement quality (completeness, accuracy, bias, period coverage).
4. Proxies where evidence is weak, with their limitations.

## Constraints / Guardrails

Do not: modify data to compute KPIs (compute read-only, e.g. in a scratch location outside the repo); fabricate current values — mark them Unknown; assign KPI owners without evidence (mark PROVISIONAL).

## Stage-Specific Completion Gate

- Every KPI has a formula, unit, source and either a measured value (with reproducible evidence) or Unknown.
- `kpi-baseline-signoff.md` declares the definitions **frozen** and lists the version.
- Human approval recorded at completion.

## Lifecycle Linkage

- Uses Stage 3. Frozen definitions are reused unchanged in Stage 34 and compared in Stage 35.
