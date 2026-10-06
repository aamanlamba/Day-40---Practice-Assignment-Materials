---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Security and Observability Overview"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "backend/app/security.py, backend/app/main.py, backend/app/config.py, backend/app/legacy_utils.py, backend/app/audit.py"
  - "adapters/partner_adapter.py, frontend/src/app/legacy-api.service.ts, frontend/src/app/legacy-widget.component.ts"
  - "observability/prometheus.yml, observability/grafana-dashboard.json"
  - "Command: in-process TestClient calls to /api/lending/admin/export and /summary"
---

# Security and Observability Overview

## Security mechanisms present

| Control | Observation | Evidence |
|---|---|---|
| Authentication | `X-User` header presence only; no verification, token or session | `security.py:4-7` [Verified Fact] |
| Authorization | Single role `["user"]`; admin = username ends with "admin" or equals "superuser" | `security.py:9-11` [Verified Fact] |
| Entity allow-list | Records/summary limited to 5 entities; path param validated | `data_access.py:6`, `main.py:51` [Verified Fact] |
| Input validation | `limit` 1–5000; `q` 2–120 chars | `main.py:50,56` [Verified Fact] |
| CORS | GET only, two localhost origins, no credentials | `main.py:9-15` [Verified Fact] |
| Secrets | Partner token default `dev-shared-token-123` in source | `config.py:7` [Verified Fact] |

## Security observations (orientation depth, not a security review)

- [Verified Fact] `/api/lending/summary`, `/health`, `/ready`, `/metrics`, `/docs` need no header (summary returned 200 unauthenticated).
- [Verified Fact] Any caller can claim any identity: `X-User: notanadmin` and `superuser` returned 200 from admin export; `support` and `analyst1` returned 403. The unused `ADMIN_USERS` list (`legacy_utils.py:4`) disagrees with `weak_admin_check` (it includes `support`).
- [Verified Fact] `/records/{entity}` and `/search` return full unmasked rows including email, phone, and PEP flag to any header-bearing caller; search matches against the whole serialised row.
- [Verified Fact] The frontend ships a fixed `X-User: workshop_user` value and a `[innerHTML]` binding in an unused `LegacyWidgetComponent` (`legacy-widget.component.ts:2`) — Angular sanitises by default.
- [Verified Fact] The frontend `summary()` call omits the header (`legacy-api.service.ts:9`); summary is open so it works.
- [Verified Fact] No rate limiting, TLS config, audit trail on data access, or secrets management is present.
- [Verified Fact] Admin export is unlogged: `audit()` has no callers (grep).

## Observability present

- [Verified Fact] Prometheus metrics `brownfield_http_requests_total{route}` and `brownfield_request_latency_seconds{route}` via middleware (`main.py:17-27`). Route label is the first path segment only, so `/api/...` endpoints collapse into `api`.
- [Verified Fact] No status-code label, so error rates cannot be derived from these metrics. The Grafana dashboard has two panels ("HTTP Requests", "Errors") with empty `targets` (`grafana-dashboard.json`).
- [Verified Fact] `/health` is static; `/ready` checks only that customers.csv can be read.
- [Verified Fact] A logger named "audit" exists but no `logging` configuration (`basicConfig`) is present; no application logging elsewhere; no tracing; no alert rules.
- [Verified Fact] Batch jobs print to stdout; there is no run record (`ops.ingestion_log` unused).

## Assumptions

- [Assumption] Intended deployment sits behind some network boundary; none is described.

## Unresolved Issues

- [Unknown] Identity provider, roles, and data-classification policy for the real estate; the CISO delegate is listed (`contact-matrix.csv`) but unnamed. Raise in Stage 0B.
- [Unknown] Regulatory obligations (AML/KYC retention, audit) — no compliance documents in the repo.

## Residual Risks

- Identity is client-asserted; PII and AML indicators are exposed accordingly (R-01, R-02, R-04).
- Without status-aware metrics and logs, incidents in this API would be hard to detect (R-07).
