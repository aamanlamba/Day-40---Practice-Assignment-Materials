---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Data Flow Overview"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "data/*.csv, data/manifest.json, data/README.md"
  - "etl/run_all.py, etl/common.py, etl/reconcile_loans.py"
  - "backend/app/data_access.py, scripts/bootstrap_sqlite.py, sql/schema_postgres.sql"
  - "Command: read-only pandas profiling of data/*.csv (no files written)"
  - "Command: cd etl && python run_all.py; python reconcile_loans.py (stdout only)"
---

# Data Flow Overview

## Data stores and volumes

| Dataset | Rows (verified) | Read by API | Read by ETL | Bootstrapped to SQLite |
|---|---|---|---|---|
| customers | 3,500 | Yes | Yes | Yes |
| applications | 5,000 | Yes | Yes | Yes |
| transactions | 9,000 | Yes | Yes | Yes |
| alerts | 1,800 | Yes | Yes | Yes |
| repayments | 5,000 | Yes | Yes (+ reconcile) | Yes |
| kyc_cases | 1,200 | **No** | No | No |
| beneficiaries | 1,200 | **No** | No | No |
| baseline_metrics | 180 (2026-03-01 … 2026-08-27) | No | No | No (only size-checked by `tests/test_workshop_baseline.py:7-9`) |

[Verified Fact] Row counts match `data/manifest.json` and `data/README.md`. All files are TEXT/CSV, UTF-8.

## Flows

1. **Serving path** — `data/*.csv` → `csv.DictReader` → in-memory tuple cache → JSON (`backend/app/data_access.py`, `main.py`). [Verified Fact] All values are returned as strings (no typing); the API exposes full rows including `email`, `phone`, `pep_flag`.
2. **ETL clean** — `etl/run_all.py` reads each CSV, normalises column names, drops any row with any blank field, returns before/after counts to stdout. [Verified Fact] Output when run: customers 3500→3457, applications 5000→4789, transactions 9000→9000, alerts 1800→1696, repayments 5000→5000. Nothing is persisted.
3. **Reconciliation** — `etl/reconcile_loans.py` left-joins repayments to applications on `application_id`, prints count of customer mismatches. [Verified Fact] Result: 218 mismatches.
4. **SQLite bootstrap** — `scripts/bootstrap_sqlite.py` deletes and recreates `brownfield.db` with all-TEXT columns. [Verified Fact] Not executed in this stage (it writes to the repo; the file is gitignored); API does not read it.
5. **Postgres** — `sql/schema_postgres.sql` defines raw JSONB landing tables, `ops.ingestion_log`, `ops.legacy_staging`. [Verified Fact] No code in the repo writes to them; `sql/legacy_reports.sql` queries only `ops.legacy_staging`.

## Data observations (orientation depth, not a quality assessment)

- [Verified Fact] No duplicate primary IDs in any file; no orphan `customer_id` in any child file (applications, transactions, alerts, repayments, kyc, beneficiaries all resolve to customers).
- [Verified Fact] 218 of 5,000 repayments carry a `customer_id` different from their application's `customer_id`.
- [Verified Fact] Blanks: `alerts.owner` 104; `applications.decision_source` 211; `customers.email` 31, `phone` 12; `beneficiaries.risk_flag` 7; `kyc_cases.age_days` 7. Sentinel values: `risk_band=UNKNOWN` 840, `kyc status=UNKNOWN` 264, `beneficiaries.risk_flag=UNKNOWN` 394, `name`/`bank_code`/`document_type` "unknown" in 245/259/257 rows.
- [Verified Fact] 14 customer emails lack "@"; 13 emails are duplicated. Currencies: applications INR/USD; transactions INR/USD/AED. Dates are uniformly `YYYY-MM-DD` in applications and transactions.
- [Verified Fact] Legacy note: "nulls may mean unknown, not-applicable, not-received, or processing-error" (`docs/legacy/business-rules.txt:5`), so blanks are not interchangeable with ETL's drop rule.
- [Verified Fact] `etl/common.py:11-13` drops *any* row with a blank; this removes e.g. 211 applications that lack only `decision_source`.
- [Inference] Mixed `decision_source` values (MODEL_V1, MODEL_V2, MANUAL, RULE) and alert `source` values (`ml-legacy`, `rules-v1`, `rules-v2`, `manual`) suggest earlier scoring systems existed; their logic is not in the repo.

## Assumptions

- [Assumption] CSVs stand in for extracts from a system of record; refresh frequency and lineage are unknown.

## Unresolved Issues

- [Unknown] Source of truth and lineage for each CSV; who produces them and when. Investigate with data-ops (ownership "unclear", `docs/legacy/contact-matrix.csv`).
- [Unknown] Why `kyc_cases` and `beneficiaries` are not served or processed.
- [Unknown] Meaning of `score` fields, `days_past_due` conventions, status code semantics.

## Residual Risks

- Customer PII and PEP flags are returned in bulk; any data-flow change must account for this (R-04).
- Data profiling here covers structure only; semantic validity is untested.
