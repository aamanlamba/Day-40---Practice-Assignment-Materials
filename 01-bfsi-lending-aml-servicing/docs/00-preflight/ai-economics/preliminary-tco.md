---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Preliminary TCO"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/ai-economics/cost-scenarios.md"
  - "docs/00-preflight/ai-economics/preliminary-finops-baseline.md"
  - "data/baseline_metrics.csv"
---

# Preliminary TCO

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

Three-year view for each scenario at expected volume (142 cases/day). Effort figures are placeholders, not estimates from evidence; they exist so non-AI and human costs are visible alongside token cost.

## Assumed unit costs

- Loaded engineering cost $1,500 per person-week (Assumption); loaded analyst cost $30/hour (Assumption).
- No time saving per case is assumed in the totals below; savings are shown only as a reference value pool (Assumption).

## Scenario build and run assumptions

| Scenario | Build (person-weeks) | Annual run: tokens (mid tier) | Annual run: people/infra | Evaluation/review per year |
|---|---|---|---|---|
| S1 Deterministic | 6 | $0 | 4 weeks maintenance | 2 weeks |
| S2 Conventional | 12 | $0 | 8 weeks + hosting | 3 weeks |
| S3 GenAI single-shot | 14 | $497 | 8 weeks + hosting | 8 weeks (evals, prompt upkeep, human review) |
| S4 Agentic | 24 | $3,299 | 12 weeks + hosting | 12 weeks (evals, guardrails, red-teaming) |

(All build/maintenance/evaluation weeks are Assumption; token figures are Estimated from `cost-scenarios.md`.)

## Three-year totals (Estimated from the assumptions above; excluding hosting)

| Scenario | Build $ | 3-yr run people $ | 3-yr tokens $ | Total $ |
|---|---|---|---|---|
| S1 | 9,000 | 27,000 | 0 | 36,000 |
| S2 | 18,000 | 49,500 | 0 | 67,500 |
| S3 | 21,000 | 72,000 | 1,491 | 94,491 |
| S4 | 36,000 | 108,000 | 9,898 | 153,898 |

## Reference: value pool (not a benefit claim)

- Baseline manual effort is about 16,777 hours/year (Estimated), about $503,305 at the assumed $30/hour. A 10% saving would be about $50,330/year (Assumption on 10%); no evidence of achievable savings exists yet.

## Observations

- [Inference] Under these placeholders, people and evaluation effort exceed token spend for S3; S4 token spend is materially larger but still smaller than the effort lines. This ordering depends on the effort assumptions and should not be trusted until measured.
- Not included: compliance review, security testing, training, change management, incident cost, decommissioning of legacy parts.

## Assumptions

- [Assumption] All effort weeks, labour rates and the 10% saving; 3-year horizon; no discounting or inflation.

## Unresolved Issues

- [Unknown] Real engineering capacity and rates, procurement terms, benefit realisation (Stages 3, 34, 36).

## Residual Risks

- TCO totals are scenario placeholders. They must not be used as a business case.
