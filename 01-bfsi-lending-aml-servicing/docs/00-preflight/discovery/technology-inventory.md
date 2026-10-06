---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Technology Inventory"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Draft"
evidence_sources:
  - "requirements.txt, pyproject.toml, pytest.ini"
  - "frontend/package.json, frontend/angular.json, frontend/tsconfig.json, frontend/playwright.config.ts"
  - "Command: .venv/bin/python --version; .venv/bin/pip list"
  - "Command: which node npm"
---

# Technology Inventory

## Backend / batch (Python)

| Technology | Declared version | Installed in local `.venv` | Evidence |
|---|---|---|---|
| Python | `>=3.11` (`pyproject.toml:8`; README says 3.11+) | 3.13.15 | [Verified Fact] |
| FastAPI | `==0.115.0` | 0.115.0 | `requirements.txt:1` [Verified Fact] |
| Starlette | transitive | 0.38.6 | pip list [Verified Fact] |
| Uvicorn | `==0.30.6` | 0.30.6 | `requirements.txt:2` [Verified Fact] |
| Pydantic | `==2.9.2` | 2.9.2 | `requirements.txt:3` [Verified Fact] |
| pandas | `==2.2.3` | 2.2.3 | `requirements.txt:4` [Verified Fact] |
| numpy | transitive (unpinned) | 2.5.3 | pip list [Verified Fact] |
| pytest | `==8.3.3` | 8.3.3 | `requirements.txt:5` [Verified Fact] |
| httpx | `==0.27.2` | 0.27.2 | `requirements.txt:6` [Verified Fact] |
| prometheus-client | `==0.21.0` | 0.21.0 | `requirements.txt:7` [Verified Fact] |
| sqlite3 (stdlib) | — | — | `scripts/bootstrap_sqlite.py:1` [Verified Fact] |

- [Verified Fact] Direct deps are pinned; transitive deps (numpy, starlette, anyio) are not locked — no lock file exists.
- [Verified Fact] Test run emits a `DeprecationWarning` from starlette's TestClient about `anyio.abc.BlockingPortal` (pytest output, 13 passed, 1 warning).
- [Verified Fact] Build backend is setuptools>=68 (`pyproject.toml:2`), but no package discovery config; pytest config is duplicated in `pyproject.toml:10-13` and `pytest.ini` (pytest uses `pytest.ini` when both exist).

## Frontend (TypeScript)

| Technology | Declared version | Evidence |
|---|---|---|
| Angular (core, common, router, forms, …) | `^17.3.0` | `frontend/package.json:10-17` [Verified Fact] |
| RxJS | `^7.8.1` | `frontend/package.json:18` [Verified Fact] |
| zone.js | `^0.14.4` | `frontend/package.json:19` [Verified Fact] |
| TypeScript | `~5.4.0`, `strict: true`, `strictTemplates: true` | `frontend/package.json:25`, `frontend/tsconfig.json` [Verified Fact] |
| Playwright | `^1.47.2` | `frontend/package.json:26` [Verified Fact] |
| Angular builder | `@angular-devkit/build-angular:browser` (webpack-based, not the esbuild `application` builder) | `frontend/angular.json` [Verified Fact] |

- [Verified Fact] No `package-lock.json`; caret ranges mean resolved versions will float. `node_modules` absent; Node and npm are available on the host (`/opt/homebrew/bin/node`).
- [Verified Fact] `frontend/tsconfig.app.json` is referenced; the frontend has not been built during this stage.

## Data / infra / observability

| Technology | Evidence |
|---|---|
| PostgreSQL (DDL dialect: `BIGSERIAL`, `JSONB`, `TIMESTAMPTZ`) | `sql/schema_postgres.sql` [Verified Fact] |
| CSV flat files as primary runtime store | `backend/app/data_access.py:12-14` [Verified Fact] |
| Prometheus (scrape `localhost:8000` every 15s) | `observability/prometheus.yml` [Verified Fact] |
| Grafana dashboard schemaVersion 38 (no targets) | `observability/grafana-dashboard.json` [Verified Fact] |
| POSIX `sh` scripts | `scripts/*.sh` [Verified Fact] |

- [Verified Fact] No container, orchestration, IaC, secrets manager or CI technology is present.

## Assumptions

- [Assumption] The local `.venv` reflects a faithful `pip install -r requirements.txt`; it was not created during this stage.

## Unresolved Issues

- [Unknown] Target runtime Python version in any real environment (only a lower bound is declared).
- [Unknown] Whether the frontend builds cleanly with current npm resolution; not attempted (would write `node_modules`). Deeper check belongs in Stage 7.

## Residual Risks

- Unlocked transitive dependencies (Python and npm) make builds non-reproducible.
- Pinned FastAPI/Starlette/pydantic versions are from 2024; currency/CVE status not assessed at this depth.
