---
stage: "0C — Provisional Token Efficiency & AI Economics Envelope"
title: "Provisional Model Call Inventory"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "backend/app/experimental_ai.py"
  - "backend/app/models.py"
  - "backend/app/config.py"
  - "docs/00-preflight/discovery/system-landscape.md"
  - "CHANGE_REQUEST.md"
---

# Provisional Model Call Inventory

Tag legend: **(Measured)** computed from repository data/command output; **(Estimated)** derived from measured figures with a stated method; **(Assumption)** taken without evidence; **(Unknown)** not determinable.

## Existing model calls

- [Verified Fact] None. A grep of `backend`, `adapters`, `etl`, `scripts`, `tests` finds no LLM or ML library call; `requirements.txt` lists no model SDK. `experimental_ai.suggest()` is a deterministic keyword counter (`experimental_ai.py:6-12`) and is not wired in.
- [Verified Fact] Flag `ENABLE_EXPERIMENTAL_SCORING` defaults to true but is never read (`config.py:8`).

## Hypothetical call points (contingent on Stage 8; not proposals)

| ID | Possible call point | Scenario | Input (est. tokens) | Output (est. tokens) | Calls/case | Tag |
|---|---|---|---|---|---|---|
| M1 | Evidence summary for one alert (alert + customer + recent transactions) | S3 | 1,700 | 300 | 1 | (Estimated) |
| M2 | Routing explanation (why HIGH/NORMAL) | S3 | 600 | 150 | 1 | (Estimated) |
| M3 | Draft analyst note (`CaseNote` has max 2,000 chars, `models.py:5`) | S3 | 900 | 500 | 1 | (Estimated; output bound by 2,000 chars ~500 tokens) |
| M4 | Retrieval/tool-use planning step | S4 | 3,000 | 250 | 5 | (Assumption) |

- No call point may take or influence an approval, payment or AML disposition without approval H4/H6 (0B).
- Model, vendor and hosting are not selected.

## Assumptions

- [Assumption] A call per case, not per record, is the natural granularity.

## Unresolved Issues

- [Unknown] Whether any call point beats deterministic S1/S2 on quality (Stage 8).

## Residual Risks

- Call points are speculative; they exist to size budgets, not to design.
