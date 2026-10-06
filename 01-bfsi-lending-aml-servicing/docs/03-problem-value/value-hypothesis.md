---
stage: "3 — Frame Problem & Value"
title: "Value Hypothesis"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "data/baseline_metrics.csv"
  - "data/alerts.csv"
  - "docs/00-preflight/ai-economics/preliminary-tco.md"
  - "docs/00-preflight/ai-economics/preliminary-finops-baseline.md"
  - "CHANGE_REQUEST.md"
---

# Value Hypothesis

Value is a **hypothesis**, not a claim. No benefit is asserted.

## Hypothesis

If reviewers see a ranked, explained view of each case and ownership gaps are closed, then manual effort and false-positive handling fall, with unchanged lending and payment results and with every decision still made by a person.

## Value pool and sensitivity (Estimated; labour rate is an Assumption)

- [Verified Fact] Baseline manual effort is 8,273.5 h over 180 days.
- [Estimated] Annualised: about 16,777 hours/year; at an assumed $30/h loaded rate (0C Assumption) about $503,305/year.

| Hypothetical effort reduction | Hours/year | Value at $30/h (Assumption) |
|---|---|---|
| 5% | 839 | $25,165 |
| 10% | 1,678 | $50,330 |
| 15% | 2,517 | $75,496 |

- [Inference] The 0C placeholder 3-year totals range from about $36,000 (deterministic scenario) to about $154,000 (agentic scenario). Over 3 years a 5% reduction is worth about $75,000 (covers the two non-AI scenarios, about $36,000 and $67,500, but not the GenAI ones), 10% about $151,000 (covers all but roughly the agentic one) and 15% about $226,000 (covers all). This is a sensitivity illustration, not a business case; effort weeks and rates are assumptions.
- Other possible value, unquantified: fewer errors (4.80%), fewer exceptions (7.29%), audit readiness, faster cycle (81.5 min), reduced regulatory exposure.

## Assumptions the hypothesis depends on

See `assumptions-register.md` (A3-01 to A3-10). The decisive ones: baseline hours belong to the targeted workflow; reviewers adopt the view; false positives drop without more misses.

## What would falsify it

Failure criteria FC-01 to FC-06 in `success-criteria.md`; and measured baseline for the specific workflow showing a much smaller share of effort than assumed.

## Assumptions

- [Assumption] $30/h loaded labour rate; reductions of 5-15% are achievable.
- [Assumption] Effort saved converts to real value (redeployment or avoided cost).

## Unresolved Issues

- [Unknown] Whether freed time has a financial value to the business; sponsor's own value measures (Stage 4, Q-026).

## Residual Risks

- Treating the table as forecasts would overstate certainty.
