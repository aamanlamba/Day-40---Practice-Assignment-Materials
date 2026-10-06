---
stage: "3 — Frame Problem & Value"
title: "User Journeys (Current State)"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/03-problem-value/personas.md"
  - "data/alerts.csv"
  - "docs/legacy/operations-runbook.txt"
  - "docs/legacy/business-rules.txt"
  - "backend/app/main.py"
---

# User Journeys (Current State)

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

Current journeys are reconstructed from data and legacy notes; steps without evidence are marked [Hypothesis].

## J1 Alert review (PE-1)

| Step | What happens today | Evidence | Pain point |
|---|---|---|---|
| 1 | Alert arrives with type, severity, status, source, score, owner | `data/alerts.csv` columns | Four alert sources with similar false-positive shares; owner blank in 104 |
| 2 | Analyst picks an alert (assignment to `analyst_a`, `analyst_b` or a shared `queue`) | owner counts | 54 open/escalated alerts have no owner |
| 3 | Analyst gathers customer, transaction and loan facts | [Hypothesis]; the only system access is full-text search over all record types (`main.py:55-65`) | Evidence is assembled by hand [Inference] |
| 4 | Analyst decides: close, escalate, mark false positive | statuses OPEN, ESCALATED, CLOSED, FALSE_POSITIVE | 23.8% end as false positive |
| 5 | Reasoning recorded | [Hypothesis]; no note storage in use | No visible record of why |

## J2 Loan servicing exception (PE-4, PE-5)

| Step | Today | Evidence | Pain |
|---|---|---|---|
| 1 | Daily reconciliation expected before 08:00 | `business-rules.txt:4` | Manual, no scheduler in repo |
| 2 | Exceptions inspected in the morning; spreadsheets and CSV extracts used to correct | `operations-runbook.txt:2-3`, `business-rules.txt:2` | Corrections live outside the system |
| 3 | Repayment/application mismatches found by a reconciliation script | `etl/reconcile_loans.py`: 218 | Result only printed, not stored |
| 4 | Upstream systems may retry without stable keys | `operations-runbook.txt:4` | Duplicate or inconsistent updates [Inference] |

## J3 Loan application decision (PE-3)

Decision sources MODEL_V1, MODEL_V2, RULE and MANUAL coexist (`data/applications.csv`); how a case is routed to one of them is [Unknown].

## Assumptions

- [Assumption] Legacy notes describe current practice, though they are labelled possibly stale.

## Unresolved Issues

- [Unknown] Real step timings and handoffs; shadow an analyst and an operations lead (Stage 4/5).

## Residual Risks

- A reconstructed journey may omit informal workarounds that carry most of the effort.
