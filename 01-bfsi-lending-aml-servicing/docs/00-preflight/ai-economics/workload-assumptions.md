---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Workload Assumptions"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "data/baseline_metrics.csv"
  - "data/README.md"
  - "data/manifest.json"
  - "docs/00-preflight/discovery/data-flow-overview.md"
  - "docs/00-preflight/discovery/workflow-overview.md"
  - "backend/app/main.py"
---

# Workload Assumptions

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

## Measured workload baseline

[Verified Fact] `data/baseline_metrics.csv` holds 180 daily rows (2026-03-01 to 2026-08-27, all 7 weekdays present), computed with pandas in this stage:

| Metric | Value | Tag |
|---|---|---|
| Total work items | 127,617 | (Measured) |
| Work items per day, mean / min / max | 709 / 412 / 1,000 | (Measured) |
| Manual effort, total / per day | 8,273.5 h / 46.0 h | (Measured) |
| Manual effort per item | 3.89 minutes | (Estimated: total hours / total items) |
| Mean cycle time | 81.5 min (range 47.2-116.4) | (Measured) |
| Error rate, mean | 4.80% | (Measured) |
| Exception rate, mean | 7.29% | (Measured) |
| `estimated_cost_units`, total / per day / per item | 370,024.2 / 2,055.7 / 2.899 | (Measured; unit of measure undefined) |

## Static data volumes

| Entity | Rows | Avg record size (JSON chars) | Approx tokens/record (chars/4) | Tag |
|---|---|---|---|---|
| alerts | 1,800 | 175 | 44 | (Measured rows; Estimated tokens) |
| customers | 3,500 | 230 | 57 | same |
| applications | 5,000 | 244 | 61 | same |
| transactions | 9,000 | 184 | 46 | same |
| repayments | 5,000 | 149 | 37 | same |
| kyc_cases | 1,200 | 151 | 38 | same |
| beneficiaries | 1,200 | 131 | 33 | same |

- [Verified Fact] 923 of 1,800 alerts are OPEN or ESCALATED; 901 are CRITICAL or HIGH. Transactions and applications span 2026-01-01 to 2026-09-28. Max 10 transactions per customer; 95th percentile 2 alerts per customer.
- [Inference] The chars/4 rule is a coarse English-text heuristic; ID-heavy CSV rows may tokenize at a different ratio, so token figures carry roughly ±40% error. No tokenizer was run.

## Workload shape

- [Verified Fact] The API is read-only over cached CSVs with full-scan search (`backend/app/main.py:55-65`); there is no per-request model call today.
- [Verified Fact] Batch jobs are manual CLI scripts printing to stdout (`etl/run_all.py`, `etl/reconcile_loans.py`).
- [Unknown] What a "work item" in the baseline file is (alert, application, exception, repayment?). The daily item count (709) exceeds what the 1,800 alerts could produce daily, so it likely covers more than alert triage.
- [Unknown] Alert arrival rate per day: `alerts.csv` has no timestamp column.

## Assumptions

- [Assumption] Baseline `work_items` is the closest available proxy for daily case volume that a triage or servicing aid might touch.
- [Assumption] Cost units are roughly USD-equivalent for comparison only (see `preliminary-finops-baseline.md`).

## Unresolved Issues

- [Unknown] Definition of work item and cost unit; seasonality; growth rate. Ask the operations lead persona (P7) in Stage 4 (baseline KPIs).

## Residual Risks

- Volume range spans 52 to 709 items/day because the AI-relevant slice is unknown; all later cost figures inherit that spread.
