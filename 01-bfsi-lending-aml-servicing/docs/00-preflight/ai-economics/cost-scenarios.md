---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Cost Scenarios"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/ai-economics/token-flow-scenarios.md"
  - "docs/00-preflight/ai-economics/volume-assumptions.md"
  - "data/baseline_metrics.csv"
---

# Cost Scenarios

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

## Unit prices (Assumption, not vendor quotes)

| Tier | Input $/M tokens | Output $/M tokens |
|---|---|---|
| Small tier | 0.80 | 4.00 |
| Mid tier | 3.00 | 15.00 |
| Large tier | 15.00 | 75.00 |

These are illustrative placeholders dated 2026-10-06 with no source; they must be replaced by quoted prices in Stage 8/32. No vendor or model is named or selected.

## Model usage cost (Estimated = tokens x assumed prices x volume; volume per case level: Low 52/day, Expected 142/day, High 709/day)

| Scenario | Case level | Price tier | $/case | $/day | $/year |
|---|---|---|---|---|---|
| GenAI single-shot | Low | Small tier | 0.0018 | 0.09 | 33 |
| GenAI single-shot | Low | Mid tier | 0.0066 | 0.34 | 125 |
| GenAI single-shot | Low | Large tier | 0.0330 | 1.71 | 623 |
| GenAI single-shot | Expected | Small tier | 0.0026 | 0.36 | 132 |
| GenAI single-shot | Expected | Mid tier | 0.0096 | 1.36 | 497 |
| GenAI single-shot | Expected | Large tier | 0.0480 | 6.81 | 2,484 |
| GenAI single-shot | High | Small tier | 0.0041 | 2.89 | 1,056 |
| GenAI single-shot | High | Mid tier | 0.0153 | 10.85 | 3,959 |
| GenAI single-shot | High | Large tier | 0.0765 | 54.24 | 19,797 |
| Agentic loop | Low | Small tier | 0.0104 | 0.54 | 196 |
| Agentic loop | Low | Mid tier | 0.0390 | 2.02 | 736 |
| Agentic loop | Low | Large tier | 0.1950 | 10.08 | 3,679 |
| Agentic loop | Expected | Small tier | 0.0170 | 2.41 | 880 |
| Agentic loop | Expected | Mid tier | 0.0638 | 9.04 | 3,299 |
| Agentic loop | Expected | Large tier | 0.3187 | 45.20 | 16,497 |
| Agentic loop | High | Small tier | 0.0456 | 32.33 | 11,800 |
| Agentic loop | High | Mid tier | 0.1710 | 121.24 | 44,251 |
| Agentic loop | High | Large tier | 0.8550 | 606.18 | 221,256 |
| S1 Deterministic | any | n/a | 0.0000 | 0.00 | 0 |
| S2 Conventional | any | n/a | 0.0000 | 0.00 | 0 |

(Each row pairs a token scenario with the volume scenario of the same name, e.g. "Expected" tokens with "Expected" volume.)

## Reading the table

- Mid-tier S3 at expected tokens and volume: $0.0096/case, about $497/year (Estimated).
- Mid-tier S4 at expected: $0.0638/case, about $3,299/year (Estimated).
- Worst row (S4 High tokens, Large tier, High volume): $0.85/case and about $221,256/year (Estimated).
- [Inference] Token cost for S3 is small relative to the measured baseline (about 2.90 cost units per work item); S4 at large-tier prices is not. Non-token costs (people, evaluation, review time) are in `preliminary-tco.md` and likely dominate.
- Excluded: embeddings, vector stores, evaluation runs, fine-tuning, safety tooling, caching discounts.

## Assumptions

- [Assumption] Prices above; no volume discounts; USD; no taxes.

## Unresolved Issues

- [Unknown] Actual vendor pricing, data-residency premium, committed-use discounts.

## Residual Risks

- Price volatility and model changes can move the S3/S4 figures by an order of magnitude.
