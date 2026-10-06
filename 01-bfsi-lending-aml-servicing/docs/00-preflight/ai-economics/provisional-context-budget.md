---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Provisional Context Budget"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "data/*.csv"
  - "docs/00-preflight/ai-economics/token-flow-scenarios.md"
  - "backend/app/models.py"
---

# Provisional Context Budget

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

| Item | Limit | Tag |
|---|---|---|
| Context window used per call | 8,000 tokens max (S4), 4,000 (S3) | (Assumption) |
| Records included per case | 1 alert, 1 customer, up to 10 transactions, up to 3 applications/repayments | (Assumption; matches token-flow components) |
| Largest observed per-customer fan-out | 10 transactions; 95th percentile 2 alerts | (Measured) |
| Full-entity prompting | Not allowed: customers alone is about 3,500 x 57 = about 200k tokens; transactions about 9,000 x 46 = about 414k tokens | (Estimated) |
| Free-text field | `CaseNote.note` max 2,000 chars | (Verified Fact, `models.py:5`) |

- [Inference] Because whole-entity datasets are 200k+ tokens each, any AI design must retrieve per case rather than pass tables; the current API exposes only full-scan search (`main.py:55-65`).
- Data minimization: names, emails and phone numbers should not enter prompts unless needed (0B data-use constraints, rule 4 in spirit; not yet designed).

## Assumptions

- [Assumption] Row-level retrieval by `customer_id` is feasible; no such endpoint exists today.

## Unresolved Issues

- [Unknown] Retrieval design and index needs (Stage 10/11).

## Residual Risks

- Prompting with PII to an external model conflicts with 0B data constraints unless approved.
