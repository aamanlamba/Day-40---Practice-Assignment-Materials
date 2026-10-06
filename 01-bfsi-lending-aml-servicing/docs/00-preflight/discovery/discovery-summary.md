---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Discovery Summary"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "docs/00-preflight/discovery/*.md (11 sibling artifacts)"
  - "Commands: self_check.py, pytest (13 passed), ETL runs, pandas profiling, TestClient probes"
---

# Discovery Summary

## What the system is

- [Verified Fact] A small BFSI estate (lending, AML/KYC, repayments) of ~73 tracked files: a read-only FastAPI service over five CSV files, an Angular 17 console, two pandas batch scripts, Postgres DDL and SQLite bootstrap not used by the API, two stub adapters, and starter Prometheus/Grafana assets.
- [Verified Fact] Only `main.py`, `security.py` and `data_access.py` are on the runtime path. Underwriting/AML rule functions, audit helper, amount services, adapters, experimental "AI" heuristic and `CaseNote` model are not referenced by any route, script or test.
- [Verified Fact] Seven tracked-data entities plus `baseline_metrics.csv` hold 32,880 rows of synthetic data; `kyc_cases` and `beneficiaries` are unused by any code.

## What works (observed)

- [Verified Fact] `SELF_CHECK_OK`; 13/13 pytest pass; both ETL scripts run and print results; app exposes 7 GET business/ops routes.

## What stands out

1. Authentication and admin authorization are client-asserted (R-01); PII is served in bulk and unlogged (R-04).
2. Rule code does not explain recorded lending outcomes (R-05); true decision logic is not in the repo.
3. Data anomalies exist (218 customer mismatches, blanks, UNKNOWN sentinels) (R-06).
4. Observability and tests are thin (R-07, R-08); no CI.
5. Ownership is incomplete in `docs/legacy/contact-matrix.csv` (R-10).

## Sufficiency for Stage 1

- [Inference] Orientation is sufficient to conduct engagement qualification: the components, data, integrations and visible risks are mapped with repository citations, and open questions are logged with investigation targets in `assumptions-unknowns.md`. Unknowns U-01, U-02, U-09 and U-11 should be raised with the sponsor before Stage 1 conclusions are relied on.
- Confidence: Medium-High for structure and reachability; Low for business semantics and production reality.

## Constraints observed during the stage

- Read-only: no application code, config, data or dependencies were changed. Commands run (self-check, pytest with `-p no:cacheprovider`, ETL scripts, in-process probes) left no tracked changes. `bootstrap_sqlite.py` and `npm install` were deliberately not run because they write into the repository.

## Assumptions

- See `assumptions-unknowns.md` (A-01 to A-07).

## Unresolved Issues

- See `assumptions-unknowns.md` (U-01 to U-14).

## Residual Risks

- See `initial-risk-register.md` (R-01 to R-17).
