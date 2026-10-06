---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Volume Assumptions"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "data/baseline_metrics.csv"
  - "docs/00-preflight/ai-economics/workload-assumptions.md"
  - "docs/legacy/business-rules.txt"
---

# Volume Assumptions

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

Three provisional volume scenarios for the slice of work a GenAI or agentic aid could touch. Nothing here selects AI; deterministic scenarios use the same volumes.

| Scenario | Share of daily work items | Cases/day | Cases/year (x365) | Basis | Tag |
|---|---|---|---|---|---|
| Low | 7.29% (mean exception rate) | 52 | 18,865 | exception items only | (Estimated from Measured) |
| Expected | 20% | 142 | 51,756 | arbitrary mid-point | (Assumption) |
| High | 100% | 709 | 258,779 | every baseline item touched | (Estimated; upper bound) |

- [Verified Fact] Work happens 7 days a week in the baseline (26/26/26/26/25/25/26 rows by weekday).
- [Verified Fact] Legacy note: daily reconciliation is expected before 08:00 local (`docs/legacy/business-rules.txt:4`). Window length is not stated.
- Batch assumption: cases processed in one overnight batch within an assumed 4-hour window (Assumption).
- Peak assumption: peak hour carries 3x average hourly volume if processed interactively (Assumption).

## Assumptions

- [Assumption] No growth over the first year; sensitivity above 709/day is not modelled.

## Unresolved Issues

- [Unknown] True alert/exception arrival rate and peak profile (Stage 4/5, P7).

## Residual Risks

- If real volume is below the Low case, fixed costs dominate per-case economics.
