---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Environment Access Boundaries"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/technology-inventory.md"
  - "docs/00-preflight/discovery/integration-overview.md"
  - "scripts/run_backend.sh"
  - "backend/app/config.py"
  - "observability/prometheus.yml"
---

# Environment Access Boundaries

## Environments identified

| Environment | Evidence | Status |
|---|---|---|
| Local developer machine (macOS, Python 3.13 `.venv`, Node on host) | [Verified Fact] 0A technology inventory | **Permitted** |
| Local API on `127.0.0.1:8000` | `scripts/run_backend.sh:3` | Permitted; no writes to repo data |
| Local Angular dev server `:4200` | `frontend/playwright.config.ts` | Permitted in a write stage; `node_modules` is gitignored |
| Local SQLite `brownfield.db` | `scripts/bootstrap_sqlite.py` | Only in a stage that permits file creation; file is gitignored |
| PostgreSQL | DDL only (`sql/schema_postgres.sql`) | [Unknown] whether an instance exists; **no access**; no connection details in repo |
| Legacy-core / partner endpoints | `adapters/*` stubs | **Prohibited**: no real calls |
| Production, staging, UAT | none evidenced | **Prohibited**; existence unknown (U-03) |
| Prometheus/Grafana | config only | Not running; may run locally only in Stage 31 |

## Access rules (PROVISIONAL)

1. [Verified Fact] README states no cloud account, Docker, Kubernetes or external service is required (`README.md:53`); none is granted.
2. No credentials are created, requested or stored. The default `PARTNER_SHARED_TOKEN` (`config.py:7`) must never be used against a real endpoint.
3. Network calls are limited to localhost, package registries for approved installs in write stages, and documentation lookups.
4. Read-only stages may run existing tests and local read-only scripts only if they leave no tracked changes (as in 0A).
5. No process binds to a non-loopback interface.

## Assumptions

- [Assumption] No hidden environment configuration exists; `.env` is gitignored and none was observed.

## Unresolved Issues

- [Unknown] The real environment list, promotion path, and who grants access (U-03).
- [Unknown] Whether a shared Prometheus exists to scrape this API.

## Residual Risks

- If a real Postgres or partner endpoint is later supplied, a human, not an agent, must revisit these prohibitions.
