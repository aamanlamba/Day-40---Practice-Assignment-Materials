---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Preliminary FinOps Baseline"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "data/baseline_metrics.csv"
  - "observability/prometheus.yml"
  - "docs/00-preflight/discovery/technology-inventory.md"
  - "scripts/run_backend.sh"
---

# Preliminary FinOps Baseline

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

## What is known

- [Verified Fact] Current operating cost evidence is only `estimated_cost_units` in `data/baseline_metrics.csv`: 370,024.2 over 180 days, 2,055.7/day, 2.899/item (Measured). The unit and what it includes are undefined.
- [Verified Fact] Manual effort 8,273.5 h over 180 days, 46.0 h/day (Measured).
- [Inference] If a loaded analyst hour costs $30 (Assumption), manual effort is about $248,205 over the period, or $1.94/item; this is the same order as the 2.90 cost units/item, so cost units may be roughly dollar-like (unverified).
- [Verified Fact] No cloud account, hosting spend, licences or AI spend appear in the repository; the system runs locally (`README.md:53`, `scripts/run_backend.sh`).
- [Verified Fact] No cost-allocation tags, budgets or billing data exist.

## Annualised reference (Estimated)

| Item | Per year | Basis |
|---|---|---|
| Work items | 258,779 | 709/day x 365 |
| Manual hours | 16,777 | 46.0/day x 365 |
| Baseline cost units | 750,327 | 2,056/day x 365 |

## FinOps gaps

- No unit-cost telemetry; Prometheus metrics count requests only (`observability/prometheus.yml`, `main.py:17-18`).
- No tagging or owner for spend; cost owner unassigned (contact matrix).

## Assumptions

- [Assumption] $30/hour loaded analyst cost (placeholder, no source).

## Unresolved Issues

- [Unknown] Real hosting, licence and support costs of the estate; the cost-unit definition (Stage 4, P7/P1).

## Residual Risks

- A wrong cost-unit interpretation would distort every ratio against it.
