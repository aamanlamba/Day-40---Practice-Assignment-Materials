---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Assumptions and Unknowns Register"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Draft"
evidence_sources:
  - "All 0A discovery artifacts in docs/00-preflight/discovery/"
  - "docs/legacy/contact-matrix.csv, docs/legacy/*.txt, docs/legacy/*.md"
---

# Assumptions and Unknowns Register

## Assumptions

Taken as true without direct evidence. Each should be confirmed or retired.

| ID | Assumption | Basis | Confirm via |
|---|---|---|---|
| A-01 | This folder is the entire system in scope | [Assumption] README framing as "self-contained" | Stage 0B scope confirmation |
| A-02 | All data is synthetic and contains no real personal data | [Assumption] Stated in `README.md:50` and `data/README.md:3`; not independently verifiable | Sponsor confirmation |
| A-03 | Unreferenced modules are inactive but may be used outside this repo | [Assumption] reachability grep only | Stage 5/7 with owners |
| A-04 | Local `.venv` faithfully reflects `requirements.txt` | [Assumption] Not built by this stage | Stage 7 clean install |
| A-05 | Legacy notes in `docs/legacy/` are partially stale | [Assumption] They say so themselves | Stage 5 validation |
| A-06 | Localhost bindings and CORS reflect dev use only | [Assumption] | Stage 0B |
| A-07 | CSV status vocabularies mirror real business states | [Assumption] | Business owner |

## Unknowns

Not determinable from the evidence. Each states where deeper investigation is required.

| ID | Unknown | Where to investigate |
|---|---|---|
| U-01 | Owners/approvers: data ownership "unclear", AI model "not-established", backups blank (`contact-matrix.csv`) | Stage 0B (operating contract) with sponsor |
| U-02 | Authoritative underwriting and AML priority rules (code rules disagree with recorded decisions: see `workflow-overview.md`) | Stage 5 (current state), Stage 7 (assessment) with product owner/compliance |
| U-03 | Production deployment topology, environments, release process | Stage 0B; Stage 5 with ops-lead |
| U-04 | Real partner and legacy-core interfaces, error semantics beyond `00`/`91`, idempotency | Stage 5 (integration), partner owner |
| U-05 | Data lineage, refresh cadence and system of record for each CSV | Stage 5 with data-ops |
| U-06 | Why `kyc_cases.csv` and `beneficiaries.csv` are unused | Stage 5 with data-ops / AML team |
| U-07 | Whether the Postgres schema is deployed and what populates `ops.*` | Stage 5 / 7 DB assessment |
| U-08 | Whether the Angular app builds and its e2e test passes | Stage 7 (needs `npm install` in a write-capable stage) |
| U-09 | Regulatory/compliance constraints (AML retention, audit, data residency) | Stage 0B with compliance / CISO delegate |
| U-10 | Business meaning of null/blank, `UNKNOWN`, `score` fields and `days_past_due` | Stage 5 with business owners |
| U-11 | Budget, timeline, value expectations behind the change request | Stage 0C (economics) |
| U-12 | Non-functional baselines: latency, load, availability | Stage 5/6 measurement |
| U-13 | Who consumes the API besides the Angular app | Stage 5 with ops/app-team |
| U-14 | Behaviour on Python 3.11 (declared minimum) | Stage 7 |

## Assumptions

(Section header required by the artifact contract; the assumptions are the table above.)

## Unresolved Issues

- All Unknowns above remain open; U-01, U-02, U-09 and U-11 most influence Stage 1 qualification and should be put to the sponsor first.

## Residual Risks

- Decisions taken on assumptions A-01 to A-07 could be invalidated by stakeholder answers; confidence in findings is Medium overall.
