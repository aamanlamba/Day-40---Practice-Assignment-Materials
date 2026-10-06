---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Economics Readiness"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/ai-economics/*.md (12 sibling artifacts)"
  - "docs/00-preflight/operating-contract/operating-contract-readiness.md"
  - "data/baseline_metrics.csv"
---

# Economics Readiness

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

## Verdict

The provisional envelope is sufficient to enter Stage 1 (engagement qualification) and later discovery stages. It is **not** a business case and does not justify AI.

## What is measured vs assumed

- Measured: baseline workload, effort, error/exception rates, cost units per item (2.899), record counts, record sizes.
- Estimated: token counts (chars/4), volume scenarios, per-case and annual model costs.
- Assumption: unit prices, loaded labour rates, effort weeks, caps, latency targets, volume share (20% expected).

## AI-specific portions contingent on Stage 8

| Artifact | AI-specific content | Status |
|---|---|---|
| `provisional-model-call-inventory.md` | All of it | Contingent on Stage 8 |
| `token-flow-scenarios.md`, `provisional-token-budget.md`, `provisional-context-budget.md`, `provisional-loop-budget.md` | S3/S4 rows | Contingent on Stage 8 |
| `cost-scenarios.md`, `preliminary-tco.md` | S3/S4 rows and unit prices | Contingent on Stage 8 |
| `quality-latency-cost-envelope.md` | Token, context, loop, S3/S4 latency rows | Contingent on Stage 8 |
| `workload-assumptions.md`, `volume-assumptions.md`, `preliminary-finops-baseline.md`, S1/S2 rows | Not AI-specific | Remain applicable |

## Gaps

1. Definition of work item and cost unit (Q-023).
2. Business budget and value targets (Q-011).
3. Real unit prices and provider data terms (Q-021).
4. Latency baseline for the existing API.
5. Alert arrival rate and peak profile.

## Confidence

Medium for measured baselines; Low for all price- and effort-dependent figures.

[Verified Fact] Stage 8 reconciles this envelope; Stage 32 measures actual economics against the applicable scenario.

## Assumptions

- [Assumption] Stage 8 will reuse the S1-S4 structure so before/after comparison stays possible.

## Unresolved Issues

- All gaps above; see `docs/_harness/open-questions.md`.

## Residual Risks

- Treating the envelope as a commitment rather than a provisional constraint set.
