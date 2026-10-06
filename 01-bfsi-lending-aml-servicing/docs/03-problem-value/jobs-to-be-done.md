---
stage: "3 — Frame Problem & Value"
title: "Jobs To Be Done"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/03-problem-value/personas.md"
  - "CHANGE_REQUEST.md"
  - "data/alerts.csv"
  - "docs/legacy/operations-runbook.txt"
---

# Jobs To Be Done

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

Format: *When [situation], I want to [job], so I can [outcome].* Jobs are neutral about means.

| ID | Persona | Job | Evidence / source |
|---|---|---|---|
| JTBD-01 | PE-1 | When I start my shift with a queue of open alerts, I want to know which need attention first and why, so I can spend time where risk is highest | *Claim* `CHANGE_REQUEST.md:3` ("surface high-risk cases ... explain routing"); *Evidence* 923 open/escalated alerts |
| JTBD-02 | PE-1 | When I open an alert, I want the customer, transaction and loan facts that bear on it in one place, so I can decide without hunting | *Evidence* data is held in separate files (customers, transactions, applications, repayments); *Hypothesis* |
| JTBD-03 | PE-1 | When I close or escalate an alert, I want to record my reasoning, so I and others can defend it later | *Hypothesis*; note model exists but is unused (`models.py`) |
| JTBD-04 | PE-2 | When a regulator or auditor asks why a case was handled as it was, I want a complete record, so I can answer within the required time | *Hypothesis*; no audit trail in use (0A) |
| JTBD-05 | PE-3 | When a loan application arrives, I want one consistent set of decision rules, so outcomes do not depend on which mechanism ran | *Evidence* four decision sources and a rule/outcome mismatch (0A R-05) |
| JTBD-06 | PE-4 | When a repayment does not match its loan, I want the exception flagged with its cause, so I can fix it the same day | *Evidence* 218 mismatches (`etl/reconcile_loans.py`) |
| JTBD-07 | PE-5 | When the morning reconciliation runs, I want a trustworthy list of exceptions, so I can finish before 08:00 | *Evidence* `business-rules.txt:4` |
| JTBD-08 | PE-6 | When anything changes, I want proof that lending and payment results are unchanged, so I can approve it | *Claim* `CHANGE_REQUEST.md:3` ("preserving existing ... behavior") |
| JTBD-09 | PE-7 | When someone requests customer data, I want access limited to what they need and recorded, so exposure is controlled | *Evidence* unmasked rows to any caller (0A R-04) |
| JTBD-10 | PE-8 | When I review the programme, I want measured improvement against a baseline, so I can decide on further funding | *Hypothesis*; baseline exists (`data/baseline_metrics.csv`) |

## Assumptions

- [Assumption] Jobs are stated at the right level of abstraction for requirements in this stage.

## Unresolved Issues

- [Unknown] Importance and frequency of each job; to be ranked in interviews (Stage 4/5).

## Residual Risks

- Jobs from the change request text only may not cover jobs analysts care about most.
