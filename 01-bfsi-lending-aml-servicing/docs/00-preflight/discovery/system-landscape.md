---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "System Landscape"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "backend/app/*.py, adapters/*.py, etl/*.py, scripts/*, sql/*.sql, frontend/src/**, observability/*"
  - "grep of symbol usage across backend, adapters, etl, scripts, tests, frontend/src, sql"
  - "In-process TestClient enumeration of app.routes"
---

# System Landscape

Every component cites at least one repository path. "Reachable" means imported/invoked by a route, script, test or entry point found in this repository.

| # | Component | Kind | Repository path(s) | Reachable? | Classification |
|---|---|---|---|---|---|
| C1 | Lending API (FastAPI app, v0.9.1) | HTTP service | `backend/app/main.py` | Yes — `scripts/run_backend.sh:3`, tests | [Verified Fact] |
| C2 | Header-based auth dependency | Library | `backend/app/security.py` | Yes — `main.py:5,50,56,68` | [Verified Fact] |
| C3 | CSV data access layer (LRU-cached) | Library | `backend/app/data_access.py` | Yes — `main.py:6` | [Verified Fact] |
| C4 | Configuration (env-var defaults) | Library | `backend/app/config.py` | Only via C11 (`adapters/partner_adapter.py:1`) | [Verified Fact] |
| C5 | Underwriting / AML-priority rules | Library | `backend/app/domain_rules.py` | No callers | [Verified Fact] |
| C6 | Amount normalisation (float vs Decimal) | Library | `backend/app/services.py` | No callers | [Verified Fact] |
| C7 | Structured audit logger | Library | `backend/app/audit.py` | No callers | [Verified Fact] |
| C8 | Legacy utilities (date parse, global cache, admin list) | Library | `backend/app/legacy_utils.py` | No callers | [Verified Fact] |
| C9 | `CaseNote` Pydantic model | Model | `backend/app/models.py` | No callers / no route | [Verified Fact] |
| C10 | Experimental "AI" keyword heuristic | Library | `backend/app/experimental_ai.py` | No callers (`ENABLE_EXPERIMENTAL_SCORING` flag defined in `config.py:8` but unread) | [Verified Fact] |
| C11 | Partner adapter (bearer header builder) | Integration | `adapters/partner_adapter.py` | No callers | [Verified Fact] |
| C12 | Legacy-core adapter (simulated) | Integration | `adapters/legacy_adapter.py` | No callers | [Verified Fact] |
| C13 | ETL clean/drop job | Batch | `etl/run_all.py`, `etl/common.py` | Manual CLI only | [Verified Fact] |
| C14 | Loan reconciliation job | Batch | `etl/reconcile_loans.py` | Manual CLI only | [Verified Fact] |
| C15 | SQLite bootstrap | Script | `scripts/bootstrap_sqlite.py` | Manual CLI (README step) | [Verified Fact] |
| C16 | PostgreSQL `ops` schema + legacy reports | DDL / SQL | `sql/schema_postgres.sql`, `sql/legacy_reports.sql` | No loader or caller in repo | [Verified Fact] |
| C17 | Synthetic data store (8 CSVs) | Data | `data/*.csv`, `data/manifest.json` | 5 of 8 files read by C3/C13/C15 | [Verified Fact] |
| C18 | Angular operations console | Web client | `frontend/src/**`, `frontend/angular.json` | `npm start` (not installed) | [Verified Fact] |
| C19 | Observability starter assets | Config | `observability/prometheus.yml`, `observability/grafana-dashboard.json` | External tools not present | [Verified Fact] |
| C20 | Self-check / release check | Script | `scripts/self_check.py`, `scripts/legacy_release_check.sh`, `scripts/run_tests.sh` | Manual | [Verified Fact] |
| C21 | Test suite | Tests | `tests/*.py`, `frontend/e2e/smoke.spec.ts` | `python -m pytest` | [Verified Fact] |

## Landscape observations

- [Verified Fact] The live system surface is C1–C3 reading C17; all business-rule modules (C5–C10) and both adapters (C11–C12) are disconnected from that surface.
- [Verified Fact] `data/beneficiaries.csv` and `data/kyc_cases.csv` are not read by any code (not in `ALLOWED_ENTITIES`, `backend/app/data_access.py:6`, nor in ETL/bootstrap lists).
- [Inference] The repository represents several engineering generations (CSV/LRU API, pandas ETL, Postgres DDL, SQLite bootstrap) that do not share a single system of record — based on C3, C13, C15, C16 each addressing different stores.
- [Unknown] External systems implied but absent: "legacy-core" (`docs/legacy/interface-codes.csv`), partner API, "spreadsheets" (`backend/app/domain_rules.py:1`), upstream status-code systems (`docs/legacy/business-rules.txt:2`).

## Assumptions

- [Assumption] Unreferenced modules are treated as present-but-inactive; they may be used by out-of-repo processes.

## Unresolved Issues

- [Unknown] Whether C16 (Postgres) is deployed anywhere; `DATABASE_URL` (`config.py:4`) is defined but never read.
- [Unknown] Real counterparts of C11/C12 (endpoint `http://legacy-host.local/api` in `adapters/legacy_adapter.py:4`).

## Residual Risks

- Landscape is code-derived only; runtime/infra outside the repo is invisible at this depth.
