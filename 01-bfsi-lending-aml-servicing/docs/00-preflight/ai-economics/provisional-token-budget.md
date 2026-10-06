---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Provisional Token Budget"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/ai-economics/token-flow-scenarios.md"
  - "docs/00-preflight/ai-economics/volume-assumptions.md"
---

# Provisional Token Budget

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

Provisional maximums as design constraints; later stages must meet or explicitly revise them.

| Budget | Single-shot (S3) | Agentic (S4) | Tag |
|---|---|---|---|
| Max input tokens per call | 4,000 | 8,000 | (Assumption) |
| Max output tokens per call | 600 | 600 | (Assumption) |
| Max total tokens per case | 5,000 | 20,000 | (Assumption; about 1.2x expected for S3; about 1.2x expected for S4) |
| Daily tokens at expected volume (142 cases) | 708,983 | 2,835,933 | (Estimated: cases x cap) |
| Daily tokens at high volume (709 cases) | 3,544,917 | 14,179,667 | (Estimated) |

- Hard stop: a call that would exceed the per-case cap is refused and the case routes to a human (Assumption; enforcement design is later).
- Daily circuit breaker at 2x expected daily tokens (Assumption).

## Assumptions

- [Assumption] Caps are set about 20-25% above expected usage to leave headroom without inviting waste.

## Unresolved Issues

- [Unknown] Provider rate limits and quotas.

## Residual Risks

- Caps set before design may be wrong in either direction; Stage 8 reconciles.
