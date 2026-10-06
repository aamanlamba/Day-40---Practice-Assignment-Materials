---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Initial Risk Register"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "backend/app/security.py, backend/app/config.py, backend/app/main.py"
  - "etl/common.py, etl/reconcile_loans.py, etl/run_all.py"
  - "tests/*.py, observability/*, docs/legacy/contact-matrix.csv"
  - "Commands: in-process TestClient calls, pandas profiling, pytest run"
---

# Initial Risk Register

Risks visible at orientation depth. Likelihood/Impact: H/M/L. Confidence is in the finding, not the mitigation. This register records risks only; it makes no remediation recommendations.

| ID | Risk | Likelihood | Impact | Evidence | Confidence |
|---|---|---|---|---|---|
| R-01 | Identity is client-asserted: any value in `X-User` authenticates; any name ending in "admin" gets admin export | H | H | `security.py:4-11`; `notanadmin`→200, `superuser`→200 on `/admin/export` [Verified Fact] | High |
| R-02 | Unauthenticated endpoints expose counts, metrics and API docs | H | L | `/summary` 200 without header; `/metrics`, `/docs` open [Verified Fact] | High |
| R-03 | Hard-coded default partner secret `dev-shared-token-123` and customer id forwarded in header | M | H | `config.py:7`; `partner_adapter.py:3-5` [Verified Fact]; actual use in prod [Unknown] | Medium |
| R-04 | Bulk unmasked PII/AML data (email, phone, PEP flag) returned to any caller; admin export 1,000 rows × 5 entities; no access audit | H | H | `main.py:49-72`; `audit()` unused [Verified Fact] | High |
| R-05 | Business-rule code does not reproduce recorded decisions (e.g. 176 DECLINED rows satisfy `approve()`); true rule source unknown | H | H | `domain_rules.py`; crosstab [Verified Fact]; cause [Unknown] | Medium |
| R-06 | Data integrity anomalies: 218 repayments reference a different customer than their application; 211 apps lack decision source; 104 alerts lack owner | H | M | `reconcile_loans.py` output; profiling [Verified Fact] | High |
| R-07 | Weak observability: metrics lack status labels, dashboard has no queries, no logging config, no alerts; `/ready` checks one file | H | M | `main.py:17-27`; `grafana-dashboard.json` [Verified Fact] | High |
| R-08 | Thin regression net: 13 tests, none for rules, ETL, adapters, search/export payloads; no CI | H | M | `test-overview.md` [Verified Fact] | High |
| R-09 | ETL drops any row with a blank field (e.g. 211 applications, 43 customers, 104 alerts) while blanks have multiple meanings; output not persisted | M | M | `etl/common.py:11-13`; run output [Verified Fact]; downstream use [Unknown] | Medium |
| R-10 | Ownership gaps: data owner "unclear", no backups for 3 areas, AI model ownership not established | H | M | `contact-matrix.csv` [Verified Fact] | High |
| R-11 | Non-reproducible builds: no Python lock file, no npm lock, caret ranges; two pytest config files | M | M | `requirements.txt`, `frontend/package.json` [Verified Fact] | High |
| R-12 | Evidence gap: only two commits, so rationale and authorship of legacy behaviour are unrecoverable | H | L | `git log` [Verified Fact] | High |
| R-13 | Parallel, unintegrated data stores (CSV, SQLite, Postgres DDL) and partial migrations risk divergent truths | M | M | `system-landscape.md`; `architecture-notes.md:8` [Inference] | Medium |
| R-14 | Process-lifetime cache and full-scan search: stale data and unmeasured scale behaviour | M | M | `data_access.py:8`; `main.py:57-65` [Verified Fact] | Medium |
| R-15 | Experimental scoring flag defaults to `true` though the code is a keyword heuristic labelled "AI"; risk of mislabelled capability if wired later | L | M | `config.py:8`; `experimental_ai.py` [Verified Fact] | Medium |
| R-16 | Duplicate money handling (float rounding vs Decimal) and mixed-currency data (INR/USD/AED) without conversion logic | M | M | `services.py`; `data/*.csv` [Verified Fact]; usage [Unknown] | Medium |
| R-17 | Regulatory exposure unknown for an AML/KYC domain: no compliance artifacts | M | H | absence in repo [Unknown] | Low |

## Assumptions

- [Assumption] Ratings use orientation-depth evidence only; they will be refined in Stage 7 and Stage 17.

## Unresolved Issues

- [Unknown] Whether any risk is already mitigated outside the repository (network controls, IdP gateway, WAF).
- [Unknown] Real exposure of the API (internal vs. internet) which governs R-01/R-04 likelihood.

## Residual Risks

- Register is incomplete by design; deeper categories (performance, resilience, licence, supply chain) are not assessed.
