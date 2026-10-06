---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Solution Scenarios"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "docs/00-preflight/discovery/workflow-overview.md"
  - "docs/00-preflight/operating-contract/provisional-operating-contract.md"
  - "backend/app/domain_rules.py"
  - "backend/app/experimental_ai.py"
---

# Solution Scenarios

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

These are cost-modelling scenarios only. [Verified Fact] No solution, model or vendor is selected, and AI is not assumed justified (Stage 8 decides; `README.md:51`). All scenarios stop at a recommendation to a human analyst (`CHANGE_REQUEST.md:3`, 0B term T6).

| ID | Scenario | What it would be (illustrative) | Model calls | Tokens | Main cost drivers |
|---|---|---|---|---|---|
| S1 | Deterministic software | Explicit thresholds/rules (similar in kind to `aml_priority`: score > 75 or PEP) with evidence listing and routing reasons | 0 | 0 | Build/test effort, rule maintenance, compute (negligible) |
| S2 | Conventional automation | S1 plus ETL fixes, queues, dashboards, optionally classical (non-LLM) scoring | 0 | 0 | Build effort, data work, hosting |
| S3 | GenAI single-shot | One model call per case to summarise evidence and explain routing | ~1 | ~1.7k in / 0.3k out expected | Tokens, evaluation, prompt upkeep, human review |
| S4 | Agentic loop | Multi-step retrieval and tool calls per case (e.g. fetch customer, transactions, repayments) | ~5 expected | ~15k in / 1.25k out expected | Tokens (context re-sent per step), retries, guardrails, observability |

- [Verified Fact] `backend/app/experimental_ai.py` is a keyword counter, not a model call, and nothing calls it; it is not a basis for S3/S4 costs.
- [Inference] S1 and S2 can reuse the existing API and data access (`backend/app/data_access.py`), so their marginal run cost is close to zero; their cost is mostly people and time.
- [Inference] S3/S4 add per-case variable cost that scales with the volumes in `volume-assumptions.md`.

## Assumptions

- [Assumption] A human analyst remains in the loop in all scenarios (0B).

## Unresolved Issues

- [Unknown] Whether S1/S2 would meet the business need; that is a Stage 8 qualification question.

## Residual Risks

- Presenting S3/S4 alongside S1/S2 could be read as a recommendation; it is not.
