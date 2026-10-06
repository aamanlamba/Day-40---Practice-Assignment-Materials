---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "High-Level Architecture"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "backend/app/main.py, backend/app/security.py, backend/app/data_access.py"
  - "frontend/src/app/legacy-api.service.ts, frontend/src/main.ts"
  - "scripts/run_backend.sh, scripts/bootstrap_sqlite.py, etl/*.py"
  - "In-process route enumeration (app.routes) and TestClient calls"
---

# High-Level Architecture (as observed)

## Runtime topology

```
                    (browser, :4200, ng serve)
   frontend/src/app/legacy-api.service.ts  ── X-User: workshop_user ──┐
                                                                      ▼
   scripts/run_backend.sh → uvicorn backend.app.main:app  (127.0.0.1:8000)
        │  CORS: GET only, origins localhost/127.0.0.1:4200
        │  timing middleware → Prometheus Counter/Histogram
        │  Depends(current_user)  ← backend/app/security.py
        ▼
   backend/app/data_access.py  ── lru_cache ──►  data/{customers,applications,
                                                  transactions,alerts,repayments}.csv
   observability/prometheus.yml ── scrape :8000/metrics (external Prometheus, not present)

   Offline / manual (no scheduler found):
     etl/run_all.py, etl/reconcile_loans.py ──pandas──► data/*.csv  → stdout only
     scripts/bootstrap_sqlite.py ──► ./brownfield.db (gitignored; not read by the API)
     sql/schema_postgres.sql      ──► (no loader in repo)
```

## Observed facts

- [Verified Fact] Single process: FastAPI app at `backend/app/main.py:8`, started by `scripts/run_backend.sh:3` on `127.0.0.1:8000`.
- [Verified Fact] Routes (enumerated in-process): `/health`, `/ready`, `/metrics`, `/api/lending/summary`, `/api/lending/records/{entity}`, `/api/lending/search`, `/api/lending/admin/export`, plus FastAPI `/docs`, `/redoc`, `/openapi.json`. All are `GET`; there are no write endpoints.
- [Verified Fact] The API is read-only over CSV files; data is cached for the process lifetime via `lru_cache(maxsize=32)` (`backend/app/data_access.py:8`), with a `clear_cache()` helper that nothing calls.
- [Verified Fact] The `DATABASE_URL` default `sqlite:///./brownfield.db` (`backend/app/config.py:4`) is never read; the SQLite file produced by `scripts/bootstrap_sqlite.py` is therefore not used by the API.
- [Verified Fact] The frontend's API base URL is hard-coded to `http://127.0.0.1:8000/api/lending` (`frontend/src/app/legacy-api.service.ts:6`), and it sends a fixed `X-User: workshop_user` header on search only.
- [Verified Fact] No scheduler, queue, cron, or message broker exists in the repository.

## Inferences

- [Inference] Architecture is a thin read-model API over flat files; the domain behaviours named in the README (underwriting, AML prioritisation) exist only as un-wired functions — based on the reachability evidence in `system-landscape.md`.
- [Inference] There are three parallel, non-integrated data paths (CSV→API, CSV→SQLite, Postgres DDL), suggesting incomplete migrations — consistent with `docs/legacy/architecture-notes.md:8` ("Several migration activities were started but not completed").

## Assumptions

- [Assumption] Localhost-only binding in `run_backend.sh` reflects dev use; real deployment topology is not represented.

## Unresolved Issues

- [Unknown] Production topology, scaling, TLS termination, identity provider — no evidence in repo. Investigate in Stage 0B/5 with stakeholders.
- [Unknown] How batch outputs (stdout only) reach operations ("daily reconciliation is expected before 08:00", `docs/legacy/business-rules.txt:4`).

## Residual Risks

- In-memory caching means data file changes are invisible until restart; correctness of "readiness" depends on this.
- Search performs full scans across ~24k rows per request (`backend/app/main.py:57-65`); behaviour under load is unmeasured.
