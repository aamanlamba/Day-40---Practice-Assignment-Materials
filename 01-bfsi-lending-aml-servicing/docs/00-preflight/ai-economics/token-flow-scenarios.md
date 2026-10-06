---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Token Flow Scenarios"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/ai-economics/workload-assumptions.md"
  - "docs/00-preflight/ai-economics/provisional-model-call-inventory.md"
  - "data/*.csv (record sizes, Measured in this stage)"
---

# Token Flow Scenarios

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

## Per-case token components (Estimated, chars/4)

| Component | Tokens | Basis |
|---|---|---|
| System/instruction prompt | 800 | (Assumption) |
| Alert record | 44 | (Estimated from 175 chars) |
| Customer record | 57 | (Estimated) |
| Last 10 transactions | 460 | (Estimated, 10 x 46) |
| Related application + repayments (about 3 records) | ~300 | (Estimated) |
| Retrieval/tool result overhead | 0-400 | (Assumption) |
| Expected output | 300 | (Assumption) |

Sum of expected single-shot input: 800 + 44 + 57 + 460 + 300 = 1,661, rounded to 1,700 (Estimated).

## Scenarios per case

| Scenario | Case | Input tokens | Output tokens | Calls | Total tokens |
|---|---|---|---|---|---|
| GenAI single-shot | Low | 1,200 | 200 | 1 | 1,400 |
| GenAI single-shot | Expected | 1,700 | 300 | 1 | 2,000 |
| GenAI single-shot | High | 2,600 | 500 | 1.2 | 3,100 |
| Agentic loop | Low | 9,000 | 800 | 3 | 9,800 |
| Agentic loop | Expected | 15,000 | 1,250 | 5 | 16,250 |
| Agentic loop | High | 42,000 | 3,000 | 10 | 45,000 |

- Agentic input is larger because each step re-sends accumulated context: expected 5 steps with input growing from about 1.7k to about 4k, averaging about 3k, so 5 x 3k = 15k (Estimated).
- Retries: High cases include a 20% retry factor for single-shot and extra steps for agentic (Assumption).
- Deterministic S1/S2: 0 tokens (by construction).
- Prompt caching, retrieval compaction and smaller contexts could reduce input; not modelled (Unknown).

## Assumptions

- [Assumption] English-like tokenization at about 4 characters per token.

## Unresolved Issues

- [Unknown] Real tokenizer counts; real context assembled by any future design.

## Residual Risks

- Agentic token growth is superlinear in step count; underestimating steps is the main error source.
