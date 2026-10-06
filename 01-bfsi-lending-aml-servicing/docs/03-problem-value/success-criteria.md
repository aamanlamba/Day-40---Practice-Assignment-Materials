---
stage: "3 — Frame Problem & Value"
title: "Success and Failure Criteria"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "data/baseline_metrics.csv"
  - "data/alerts.csv"
  - "data/repayments.csv"
  - "docs/00-preflight/ai-economics/quality-latency-cost-envelope.md"
  - "CHANGE_REQUEST.md"
---

# Success and Failure Criteria

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

Baselines are Measured from repository data in this or earlier stages. **Thresholds are proposals (Assumption)**: no stakeholder has set a target (Q-011). They exist so Stage 4 can refine them and the sponsor can accept or change them.

## Success criteria

| ID | Metric | Baseline | Threshold | Timeframe | Status | Requirement |
|---|---|---|---|---|---|---|
| SC-01 | Manual effort per work item | 3.89 min (Measured, baseline) | <= 3.50 min (-10%) | 6 months after release, 30-day mean | Proposed | BR-001, BR-002 |
| SC-02 | False-positive share of closed alerts | 23.8% (Measured) | <= 19% (-20% relative) | 6 months, quarterly | Proposed | BR-001 |
| SC-03 | Open/escalated alerts with no owner | 54 of 923 (5.9%) (Measured) | 0 | Within 1 month of release, then weekly | Proposed | BR-004 |
| SC-04 | Mean exception rate | 7.29% (Measured) | <= 6.5% | 6 months, 30-day mean | Proposed | BR-008 |
| SC-05 | Mean error rate | 4.80% (Measured) | <= 4.80% (must not worsen); target <= 4.0% | 6 months, 30-day mean | Proposed | BR-007 |
| SC-06 | Mean cycle time per item | 81.5 min (Measured) | <= 73 min (-10%) | 6 months, 30-day mean | Proposed | BR-001 |
| SC-07 | Repayment/application customer mismatches | 218 of 5,000 (4.4%) (Measured) | All flagged with cause within 1 business day | Within 3 months | Proposed | BR-008 |
| SC-08 | Alerts with a recorded disposition reason | Not measured (no record in use) | 100% of closed alerts | From go-live | Proposed | BR-005 |
| SC-09 | Regression on lending/payment outputs | Baseline test suite: 13 passing | 0 unexplained differences on the baseline dataset | Every release | Proposed | BR-007, NFR-001 |
| SC-10 | Autonomous financial decisions executed | 0 (no such capability) | 0 | Always | Proposed | BR-006 |

## Failure criteria (stop or reconsider)

| ID | Condition |
|---|---|
| FC-01 | Any lending or payment result changes without approval |
| FC-02 | Error rate rises above 4.80% baseline for two consecutive months |
| FC-03 | Any financial decision is executed without a human decision-maker |
| FC-04 | Personal data is exposed beyond a role's need or an access cannot be traced |
| FC-05 | After 6 months, manual effort per item is not at least 5% lower and no learning plan exists |
| FC-06 | Cost of added automation exceeds the sponsor-approved cap for 2 consecutive months |

## Notes

- [Verified Fact] Baseline file covers 2026-03-01 to 2026-08-27; seasonality is unknown, so a 30-day mean is proposed to smooth variation (daily std dev of items is about 106).
- [Inference] SC-01, SC-04, SC-05 and SC-06 depend on the baseline hours belonging to the targeted workflow (Q-023); until confirmed they are indicative.
- SC-02 depends on a true "not suspicious" label; it does not capture missed cases, for which no data exists.

## Assumptions

- [Assumption] A 10% improvement on effort is a plausible, non-evidenced starting target; the false-positive target similarly.

## Unresolved Issues

- [Unknown] Business-set targets, acceptable miss rate, seasonality (Stage 4).

## Residual Risks

- Proposed thresholds may be read as commitments; they are placeholders.
