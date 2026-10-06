---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Integration Overview"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Draft"
evidence_sources:
  - "adapters/legacy_adapter.py, adapters/partner_adapter.py"
  - "backend/app/config.py, backend/app/main.py (CORS block)"
  - "docs/legacy/interface-codes.csv, docs/legacy/operations-runbook.txt, docs/legacy/contact-matrix.csv"
  - "observability/prometheus.yml, frontend/src/app/legacy-api.service.ts"
---

# Integration Overview

## Inventory of interfaces

| # | Interface | Direction | Protocol / mechanism | Repository evidence | Status |
|---|---|---|---|---|---|
| I1 | Angular console → Lending API | Inbound to API | HTTP GET, JSON, `X-User` header | `frontend/src/app/legacy-api.service.ts:6-10` | [Verified Fact] Wired in code |
| I2 | Prometheus → API `/metrics` | Inbound to API | HTTP scrape every 15s | `observability/prometheus.yml`, `backend/app/main.py:41` | [Verified Fact] Config exists; Prometheus itself not present |
| I3 | Partner API headers | Outbound | `Authorization: Bearer <shared token>` + `X-Customer` | `adapters/partner_adapter.py:3-5` | [Verified Fact] Builds headers only; no HTTP call, no caller |
| I4 | Legacy-core adapter | Outbound | Simulated; returns `legacyCode` randomly "00" (75%) or "91" (25%) | `adapters/legacy_adapter.py:10-15` | [Verified Fact] Simulation only, no caller |
| I5 | CSV extracts for support/ops | Manual / file | Human-driven | `docs/legacy/operations-runbook.txt:3`, `docs/legacy/release-notes.md:6` | [Inference] Only documented, not implemented as an export job; closest code is `/api/lending/admin/export` |
| I6 | Postgres `ops.*` tables | Data | SQL | `sql/schema_postgres.sql` | [Verified Fact] DDL only; no loader or connection code |

## Observations

- [Verified Fact] CORS allows only `GET` and headers `X-User`, `Content-Type`, from `http://localhost:4200` and `http://127.0.0.1:4200`; credentials off (`backend/app/main.py:9-15`). Covered by `tests/test_workshop_baseline.py:11-14`.
- [Verified Fact] Interface code table defines only legacy-core `00` success and `91` upstream unavailable; partner codes are `UNKNOWN / not documented` (`docs/legacy/interface-codes.csv`).
- [Verified Fact] `LEGACY_TIMEOUT_SECONDS` (30) is defined (`config.py:5`) but neither adapter uses it; `LegacyAdapter.fetch` has no timeout, retry or error handling.
- [Verified Fact] Partner token default is the literal `dev-shared-token-123` (`config.py:7`) and the customer id is propagated in a header.
- [Verified Fact] Runbook states upstream systems "retry without stable idempotency keys" and "A successful HTTP response does not always mean downstream processing completed" (`docs/legacy/operations-runbook.txt:4-5`). [Unknown] whether any such upstream exists; this API has no write endpoints.

## Assumptions

- [Assumption] The adapters are intended, not actual, integration points; real endpoints and contracts exist elsewhere.

## Unresolved Issues

- [Unknown] Partner identity, contract, rate limits, and token rotation. Investigate at Stage 5 with the integration owner (none named: `docs/legacy/contact-matrix.csv`).
- [Unknown] Real `legacy-core` interface and semantics of codes other than `00`/`91`.
- [Unknown] Whether any external consumers call this API besides the Angular client.

## Residual Risks

- Integration behaviour cannot be verified from code alone; all adapters are stubs.
- Shared static token in config is a credential-handling risk (see `initial-risk-register.md` R-03).
