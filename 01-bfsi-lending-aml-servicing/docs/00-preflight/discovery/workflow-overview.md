---
stage: "0A — Pre-Flight Repository & System Orientation"
title: "Workflow Overview"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Draft"
evidence_sources:
  - "backend/app/domain_rules.py, backend/app/main.py, backend/app/experimental_ai.py"
  - "data/applications.csv, data/alerts.csv, data/repayments.csv, data/kyc_cases.csv (status columns)"
  - "CHANGE_REQUEST.md, docs/legacy/business-rules.txt, docs/legacy/operations-runbook.txt"
  - "Command: in-process evaluation of approve() against applications.csv"
---

# Workflow Overview

Workflows are inferred from data vocabularies and un-wired rule code; none is implemented end to end in the repository.

## W1 — Loan application and underwriting

- [Verified Fact] Application lifecycle statuses in data: `NEW`, `UNDER_REVIEW`, `APPROVED`, `DECLINED`, `DISBURSED` (`data/applications.csv`). Products: PERSONAL, SME, AUTO, HOME. Channels: branch, partner, web, mobile. Decision sources: MODEL_V1, MODEL_V2, MANUAL, RULE, or blank.
- [Verified Fact] `approve(score, amount)` returns true if score > 680 and amount < 2,500,000 (`domain_rules.py:2-4`). No code calls it.
- [Verified Fact] Applying `approve()` to the data does not align with recorded status: 190 of 986 APPROVED and 200 of 1,034 DISBURSED rows satisfy the rule, while 176 DECLINED rows also satisfy it (crosstab run in-process).
- [Inference] Recorded decisions were not produced by this rule (or the rule has diverged). Per the code comment "Duplicate underwriting logic also exists in ETL and spreadsheets" (`domain_rules.py:1`), other logic exists elsewhere. [Unknown] where; no underwriting logic was found in `etl/`.

## W2 — AML / fraud / KYC alert triage

- [Verified Fact] Alert types: AML, FRAUD, SANCTIONS, KYC_REFRESH; severities LOW–CRITICAL; statuses OPEN, ESCALATED, CLOSED, FALSE_POSITIVE; owners analyst_a, analyst_b, queue, or blank (104) (`data/alerts.csv`).
- [Verified Fact] `aml_priority(score, pep_flag)` returns HIGH if score > 75 or pep_flag == "Y" (`domain_rules.py:6-8`); no caller. 889 of 3,500 customers have `pep_flag=Y` (25%).
- [Verified Fact] No route creates, updates, assigns or closes alerts; `CaseNote` model exists with no route (`models.py`).
- [Inference] Triage is performed outside this system (analysts, spreadsheets); this is consistent with the change request's "manual fraud/AML triage".

## W3 — Loan servicing and repayment

- [Verified Fact] Repayment statuses PAID, DUE, PARTIAL, BOUNCED; `days_past_due` 0–180 (`data/repayments.csv`). 
- [Verified Fact] Reconciliation job reports 218 repayment/application customer mismatches (`etl/reconcile_loans.py:8`).
- [Unknown] Collections, restructuring and disbursement behaviour; no code.

## W4 — Daily operations and exceptions

- [Verified Fact, documentary] Daily reconciliation expected before 08:00 local; exceptions inspected each morning; spreadsheets used for corrections; CSV exports used during incidents; manual maintenance-window releases (`docs/legacy/business-rules.txt`, `operations-runbook.txt`, `release-notes.md`).
- [Unknown] Whether these practices still apply; documents are labelled "possibly stale".

## W5 — Read-only operational console

- [Verified Fact] The only implemented user workflow: view record counts and search records via the Angular console or `/api/lending/*`; admin export of up to 1,000 rows per entity (`main.py:67-72`).

## W6 — Experimental scoring

- [Verified Fact] `experimental_ai.suggest()` is a keyword counter over free text, returning label "review"/"normal" and a confidence 0.55-0.85 (`experimental_ai.py`). It is not called; its flag defaults to `true` but is unread.

## Assumptions

- [Assumption] Status vocabularies in CSVs reflect the real business states.

## Unresolved Issues

- [Unknown] Authoritative business rules for approval, AML priority and routing. Needs business owner input (Stage 0B/1); no owner named for application decisions beyond "app-team / product-owner".
- [Unknown] Who the users are and their roles; the API has a single `user` role (`security.py:7`).

## Residual Risks

- Behavioural baseline for rules cannot be taken from the code, since the rule functions do not match recorded outcomes; Stage 5/7 must find the true source.
