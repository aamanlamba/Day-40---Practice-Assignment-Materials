---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Scope Boundaries"
version: "1.1"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/system-landscape.md"
  - "docs/00-preflight/discovery/repository-overview.md"
  - "CHANGE_REQUEST.md"
  - "README.md"
---

# Scope Boundaries

## In scope (PROVISIONAL)

- [Verified Fact] The folder `01-bfsi-lending-aml-servicing/` at base commit `863a1f8`: `backend/`, `frontend/`, `etl/`, `adapters/`, `data/`, `sql/`, `scripts/`, `tests/`, `observability/`, and inherited docs in `docs/legacy/`.
- [Inference] Business capability in scope: the triage and servicing problems named in `CHANGE_REQUEST.md` (fraud/AML triage, loan-servicing exceptions), analysed against the 21 components in `system-landscape.md`.

## Out of scope (PROVISIONAL)

| Exclusion | Basis |
|---|---|
| Any production, staging or customer-facing system | None evidenced; [Unknown] whether they exist (U-03) |
| Real partner or legacy-core endpoints | Adapters are stubs (`adapters/legacy_adapter.py`) |
| Real customer/company data | `README.md:50` |
| Sibling folder `fde-harness/` and other content of the parent git repo | Not the system under study |
| Autonomous financial decisions | `CHANGE_REQUEST.md:3` |
| AI/agent capability before Stage 8 qualification | `README.md:51` |
| Cloud accounts, Docker, Kubernetes, external services | `README.md:53` says none required |
| Spreadsheet and upstream-system logic referenced in comments | Not in repo (`backend/app/domain_rules.py:1`) |

## Boundary notes

- [Verified Fact] The change request is "a business pressure statement, not an approved solution design" (`CHANGE_REQUEST.md:7`); no solution scope is approved here.
- [Verified Fact] The frontend has not been built in this engagement (U-08).

## Assumptions

- [Assumption] Scope widens to spreadsheets or upstream systems only if the sponsor supplies them as evidence.

## Unresolved Issues

- [Unknown] Whether the unused datasets `kyc_cases` and `beneficiaries` belong to the intended triage scope (U-06).
- [Unknown] Success criteria and budget bounding scope (U-11; Stage 0C).

## Residual Risks

- Scope creep toward "AI triage" before qualification would contradict T5.
- Excluding out-of-repo systems may hide the real decision logic (R-05).

## Change Log

- v1.1 (2026-10-06, run 2): Version bump for re-run 2 on a new base commit (b2c1f27, 0A evidence committed); content unchanged. Prior version snapshotted under `docs/_harness/history/0b/`.
