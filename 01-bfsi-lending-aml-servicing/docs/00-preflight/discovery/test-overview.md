---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Test Overview"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Draft"
evidence_sources:
  - "tests/*.py (5 modules), tests/conftest.py"
  - "frontend/e2e/smoke.spec.ts, frontend/playwright.config.ts"
  - "scripts/self_check.py, scripts/run_tests.sh, scripts/legacy_release_check.sh"
  - "Command: .venv/bin/python scripts/self_check.py → SELF_CHECK_OK"
  - "Command: .venv/bin/python -m pytest -q -p no:cacheprovider → 13 passed, 1 warning"
---

# Test Overview

## Executed results

- [Verified Fact] `scripts/self_check.py` printed `SELF_CHECK_OK` (checks 5 CSVs exist with ≥10 rows and that `backend.app.main` imports).
- [Verified Fact] `python -m pytest -q` → 13 passed, 1 warning (starlette/anyio deprecation), 0.22s. Run with `-p no:cacheprovider`; `git status` showed no tracked changes caused by the run.

## Inventory

| Module | Tests | What it appears to cover |
|---|---|---|
| `tests/test_health.py` | 4 | `/health`, `/ready`, `/metrics` presence of counter name, `/summary` counts > 0 |
| `tests/test_api_contract.py` | 3 | 404 on unknown entity; 422 on `limit=0`; 422 on 1-char search |
| `tests/test_security_characterization.py` | 3 | 401 without `X-User`; 200 with any user; `ops_admin` can call admin export |
| `tests/test_data_contract_smoke.py` | 1 | 5 CSVs exist, >10 rows, ≥4 columns |
| `tests/test_workshop_baseline.py` | 2 | `baseline_metrics.csv` size >1000 bytes; CORS preflight for 127.0.0.1:4200 |
| `frontend/e2e/smoke.spec.ts` | 1 | Heading "Operations Console" renders (Playwright) |

## Observations

- [Verified Fact] Nothing under test covers `domain_rules.py`, `services.py`, `audit.py`, `legacy_utils.py`, `experimental_ai.py`, adapters, ETL, `bootstrap_sqlite.py`, SQL, or data values/semantics.
- [Verified Fact] The security tests are explicitly "characterization" (`test_security_characterization.py:8,14`) and assert current behaviour, including the permissive admin shortcut.
- [Verified Fact] No test checks `/search` or `/admin/export` success payloads, authorization denial (403) for admin, or CORS rejection.
- [Verified Fact] No coverage tooling or threshold is configured (`coverage.xml` appears only in `.gitignore`). No CI runs the tests.
- [Verified Fact] The Playwright smoke test was not run (frontend dependencies not installed; installing would write to the repo).
- [Verified Fact] `scripts/legacy_release_check.sh` is self-described as "Deliberately incomplete": runs self-check + pytest only.
- [Verified Fact] Tests read the live `data/` files, so they depend on the synthetic data's exact state; `lru_cache` is shared across tests in-process.
- Quality of tests is not judged here (per stage scope).

## Assumptions

- [Assumption] A passing local run in Python 3.13 predicts behaviour on the 3.11 lower bound; untested.

## Unresolved Issues

- [Unknown] Frontend build/e2e status.
- [Unknown] Whether tests exist outside the repo (QA suites, UAT scripts).

## Residual Risks

- Most business logic and all batch paths have zero automated verification, so they cannot yet serve as a regression safety net (R-08).
