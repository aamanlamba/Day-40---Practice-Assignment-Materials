---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Repository Overview"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "git ls-files (73 tracked files excluding harness history) at base commit 863a1f8"
  - "README.md, WORKSHOP_SCENARIO.md, CHANGE_REQUEST.md"
  - "git log --oneline (commits 67f610d, 863a1f8)"
  - ".gitignore"
---

# Repository Overview

## Purpose (as stated)

- [Verified Fact] The repository describes itself as "a self-contained workshop repository representing an inherited enterprise system", "deliberately runnable but imperfect" (`README.md:5`). Domain: BFSI digital lending, AML and loan servicing (`WORKSHOP_SCENARIO.md:3`).
- [Verified Fact] All bundled records are declared synthetic (`README.md:50`, `data/README.md:3`).
- [Verified Fact] A business change request asks to "reduce manual fraud/AML triage and loan-servicing exceptions while preserving existing lending and payment behavior", explicitly framed as a pressure statement, not an approved design (`CHANGE_REQUEST.md:3-7`).

## Top-level layout (observed)

| Path | Contents (observed) | Evidence |
|---|---|---|
| `backend/app/` | FastAPI app (`main.py`) plus 9 supporting modules | `backend/app/*.py` |
| `frontend/` | Angular 17 standalone-component client, Playwright e2e config | `frontend/package.json`, `frontend/src/app/*.ts` |
| `etl/` | Two pandas batch scripts + shared helpers | `etl/run_all.py`, `etl/reconcile_loans.py`, `etl/common.py` |
| `adapters/` | Simulated legacy-core adapter and partner header builder | `adapters/legacy_adapter.py`, `adapters/partner_adapter.py` |
| `data/` | 8 synthetic CSVs (32,880 rows total), `manifest.json`, catalog README | `data/manifest.json` |
| `sql/` | PostgreSQL `ops` schema DDL and two legacy report queries | `sql/schema_postgres.sql`, `sql/legacy_reports.sql` |
| `scripts/` | Self-check, SQLite bootstrap, run/test/release shell wrappers | `scripts/*` |
| `tests/` | 5 pytest modules, 13 tests | `tests/*.py` |
| `observability/` | Prometheus scrape config, skeletal Grafana dashboard | `observability/*` |
| `docs/legacy/` | 6 inherited notes (architecture, rules, contacts, interface codes, runbook, release notes) | `docs/legacy/*` |
| `docs/_harness/`, `.claude/commands/` | AI FDE harness state and slash commands (not part of the system under study) | `docs/_harness/README.md` |

## Repository facts

- [Verified Fact] Two commits touch this folder: `67f610d` (baseline extraction) and `863a1f8` (harness install). There is no deeper history, so authorship/evolution of the code cannot be reconstructed from git.
- [Verified Fact] The repository is nested inside a larger git repository (`Day-40---Practice-Assignment-Materials`); sibling folder `fde-harness/` is outside the target.
- [Verified Fact] `.gitignore` excludes `.venv/`, `*.db`, `.env`, `node_modules/`, `dist/`, `coverage.xml`. A local `.venv` (Python 3.13.15) exists but is untracked; no `node_modules` exists.
- [Verified Fact] No CI definition exists (no `.github/`, no other pipeline file found). No Dockerfile, compose, Helm or IaC files exist.
- [Verified Fact] Self-declared versions: backend API `0.9.1` (`backend/app/main.py:8`), frontend `0.6.2` (`frontend/package.json:3`), Python project `0.1.0` (`pyproject.toml:7`).

## Observed component boundary vs. code reachability

- [Verified Fact] Only `backend/app/main.py`, `security.py` and `data_access.py` are imported on the runtime path (grep of all symbol usages). `domain_rules.py`, `services.py`, `audit.py`, `legacy_utils.py`, `models.py`, `experimental_ai.py`, and both adapters are not imported by any route, script or test.
- [Inference] A large share of the "business logic" files are dormant or orphaned code whose operational relevance is unknown; based on the grep above plus the code comments ("Partial migration", "abandoned spike").

## Assumptions

- [Assumption] The folder as checked out at `863a1f8` is the complete system scope for this engagement; no other repositories, services or spreadsheets referenced in comments (`backend/app/domain_rules.py:1`) are in scope unless supplied later.
- [Assumption] The harness-installed files (`docs/_harness/`, `.claude/commands/`) are tooling, not part of the system.

## Unresolved Issues

- [Unknown] Who owns each component — `docs/legacy/contact-matrix.csv` names team aliases only, with data ownership "unclear" and AI ownership "not-established". Requires stakeholder input (Stage 0B / 1).
- [Unknown] Whether a production deployment of this estate exists anywhere and what version it runs.

## Residual Risks

- Lack of meaningful git history removes a source of evidence about why rules diverge (see `initial-risk-register.md` R-12).
- Dormant modules may still be invoked by out-of-repo callers we cannot see.
