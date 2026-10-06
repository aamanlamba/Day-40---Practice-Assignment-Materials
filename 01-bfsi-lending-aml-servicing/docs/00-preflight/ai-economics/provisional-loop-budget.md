---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Provisional Loop Budget"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/operating-contract/stop-conditions.md"
  - "docs/00-preflight/ai-economics/token-flow-scenarios.md"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
---

# Provisional Loop Budget

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

Applies to S4 only; S1-S3 have no loops.

| Limit | Value | Tag |
|---|---|---|
| Max reasoning/tool steps per case | 6 | (Assumption; expected 5) |
| Max retries per step | 2 | (Assumption) |
| Hard cap on total model calls per case | 8 | (Assumption) |
| Max wall-clock per case | 30 s interactive; 120 s batch | (Assumption) |
| Max cost per case before forced human hand-off | $0.10 (same cap as `quality-latency-cost-envelope.md`); S4 expected at mid-tier is $0.064, but S4 high at mid-tier is $0.171 and would breach it (see `cost-scenarios.md`) | (Assumption) |
| Loop termination | At a recommendation; no loop may execute a financial action | (0B T6, Verified Fact) |

- [Verified Fact] 0B stop condition S-08 stops work if agent behaviour is introduced before Stage 8 qualification.
- Overrun handling: on any limit breach the case is escalated to a human with the partial evidence (Assumption).

## Assumptions

- [Assumption] Six steps suffice for evidence gathering across at most 4 entity types.

## Unresolved Issues

- [Unknown] Real step counts; only a prototype can measure them (Stage 19/22 if qualified).

## Residual Risks

- Loop caps could truncate legitimate hard cases; need measured step distributions.
