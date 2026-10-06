---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Data Use Constraints"
version: "1.1"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/data-flow-overview.md"
  - "data/README.md"
  - "data/manifest.json"
  - "backend/app/main.py"
  - "README.md:50"
---

# Data Use Constraints

## Data classes present

| Class | Datasets / fields | Evidence | Handling (PROVISIONAL) |
|---|---|---|---|
| Customer identity and contact (synthetic) | `customers.csv`: name, email, phone, age, city | `data/README.md:21-23` | Treat as real PII: no copying outside the repo, no external services |
| AML/compliance indicators | `customers.pep_flag`, `risk_band`; `alerts`; `beneficiaries.risk_flag`; `kyc_cases` | `data/README.md` | Regulated-sensitive; no external transmission |
| Financial and credit | `applications`, `transactions`, `repayments` | `data/README.md` | Confidential |
| Operational baselines | `baseline_metrics.csv` | `data/README.md:13-15` | Internal; feeds Stage 4 |
| Legacy documentation | `docs/legacy/*` | | Internal |

## Constraints

1. [Verified Fact] All bundled records are declared synthetic (`README.md:50`). [Assumption] Not independently verified (A-02). Handle as if real to avoid habit risk.
2. No real customer or company data may enter the repo, prompts, logs or artifacts. If real-looking data appears, stop (`stop-conditions.md` S-04).
3. Data files are not modified; derived datasets are written only under an approved stage folder and labelled synthetic-derived.
4. Artifacts quote counts and aggregates, not full records. Names, emails and phone numbers are not reproduced.
5. Application code sends no data to external AI/LLM services. [Unknown] whether the tool provider retains inputs; acceptable only because data is assumed synthetic (A-02).
6. [Verified Fact] The API returns unmasked rows to any caller with an `X-User` header (`main.py:49-72`); local runs bind to loopback only.
7. Data anomalies (218 customer mismatches, blanks, `UNKNOWN` sentinels) are evidence and are documented, not repaired in source data.
8. Anything committed to git persists, so no secrets or real identifiers are committed.

## Assumptions

- [Assumption] Synthetic status removes legal data-protection obligations for the workshop, not the professional-handling rules above.

## Unresolved Issues

- [Unknown] Regulatory classification, retention and residency rules for the real estate (U-09).
- [Unknown] Data owner and approver for any use beyond local analysis (U-01; `contact-matrix.csv` data row is "unclear").

## Residual Risks

- Without proven synthetic provenance, a real-data leak would not be caught by repository checks.

## Change Log

- v1.1 (2026-10-06, run 2): Version bump for re-run 2 on a new base commit (b2c1f27, 0A evidence committed); content unchanged. Prior version snapshotted under `docs/_harness/history/0b/`.
