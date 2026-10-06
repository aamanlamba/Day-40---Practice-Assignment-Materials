---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Quality, Latency and Cost Envelope"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/ai-economics/cost-scenarios.md"
  - "data/baseline_metrics.csv"
  - "docs/legacy/business-rules.txt"
  - "docs/00-preflight/operating-contract/stop-conditions.md"
  - "tests/test_health.py"
---

# Quality, Latency and Cost Envelope

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

**Provisional maximums as design constraints.** Later stages must satisfy or explicitly revise them with a recorded reason.

| Dimension | Provisional maximum | Basis | Tag |
|---|---|---|---|
| Marginal AI cost per case | $0.10 (about 3.4% of baseline 2.90 cost units/item) | keep AI run cost a small fraction of current per-item cost | (Assumption; unit equivalence unverified) |
| Marginal AI cost per day at expected volume | $14.18 | cap x 142 cases | (Estimated) |
| Marginal AI cost per day at high volume | $70.90 | cap x 709 cases | (Estimated) |
| Cost circuit breaker | 2x expected daily cost | runaway protection | (Assumption) |
| Interactive latency p95 | 5 s (S3), 30 s (S4) | analyst waiting at a screen | (Assumption) |
| Batch completion | before 08:00 local; window assumed 4 h | legacy reconciliation expectation | (Verified Fact for 08:00; Assumption for 4 h) |
| Context per call | 4,000 (S3) / 8,000 (S4) tokens | `provisional-context-budget.md` | (Assumption) |
| Agent loop | 6 steps, 8 calls | `provisional-loop-budget.md` | (Assumption) |
| Quality floor | Not worse than the current manual baseline: error rate 4.80% and exception rate 7.29% (mean) | baseline | (Measured baseline; target an Assumption) |
| Existing API latency reference | Unknown; no latency measured | | (Unknown) |

- [Verified Fact] Existing behaviour must be preserved (`CHANGE_REQUEST.md:3`); the 13-test baseline must pass (0B change control rule 4).
- [Inference] Current throughput evidence is only the baseline CSV; no p50/p95 latency data exists for the API, so latency maxima are not anchored to measurements.
- [Inference] Against the $0.10 cap, S3 passes in every modelled mid-tier case; S4 passes at expected mid-tier ($0.064) but breaches it at high mid-tier ($0.171) and at large-tier prices (see `cost-scenarios.md`).
- Deterministic S1/S2 must meet the same quality and latency constraints; they carry no token cost.

## Assumptions

- [Assumption] A cap of $0.10/case is acceptable to the business; no stakeholder has stated a budget (Q-011).

## Unresolved Issues

- [Unknown] Business-stated cost, latency and quality targets (Stage 3/4 with P1, P7).

## Residual Risks

- Constraints built on unverified cost units could be too loose or too tight.
