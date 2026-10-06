---
stage: "1 — Engage & Qualify"
title: "Open Qualification Questions"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/_harness/open-questions.md"
  - "docs/legacy/contact-matrix.csv"
  - "CHANGE_REQUEST.md"
  - "docs/00-preflight/operating-contract/open-governance-decisions.md"
---

# Open Qualification Questions

Questions that must be answered to firm up the qualification. IDs refer to `docs/_harness/open-questions.md`; new questions raised in Stage 1 are listed in the stage report and will be logged by the harness on completion.

| Priority | Question | Log ID | Ask | Needed by |
|---|---|---|---|---|
| 1 | Who is the named sponsor, business owner and technical owner? | Q-001, Q-015 | P1 | Stage 2 |
| 2 | What are the measurable targets and the trigger/deadline for this change? | Q-011 | P1, P3 | Stage 3 |
| 3 | Where do the authoritative approval and AML-priority rules live? | Q-002 | P3, P4 | Stage 5 |
| 4 | Which regulations and audit/retention rules apply? | Q-009 | P4, P5, P10 | Stage 25 (needed earlier for scope) |
| 5 | What is a work item, and what is a cost unit? | Q-023, Q-024 | P7 | Stage 4 |
| 6 | What alert volume and arrival profile does triage handle? | Q-025 | P7 | Stage 4 |
| 7 | Which environments exist and who may grant access? | Q-003 | P7, P8 | Stage 5 |
| 8 | Is the AI-model owner role needed, and who holds it? | Q-018 | P1, P9 | Stage 8/25 |
| 9 | Are `kyc_cases` and `beneficiaries` in scope? | Q-006 | P4, P6 | Stage 5 |
| 10 | May the engagement use the tool provider with this data? | Q-021 | P5, P10 | Stage 2 |

## Questions still without a log entry (to be logged at completion)

- Is there a hard deadline or business event driving urgency?
- Who accepts residual risk if the engagement proceeds with the security gaps in place?
- Is any regulator or auditor already aware of or involved in this change?

## Assumptions

- [Assumption] Answers can come from stakeholders in Stage 2 interviews or documents.

## Unresolved Issues

- All questions above are open.

## Residual Risks

- Unanswered priority-1 and priority-3 questions are the main threat to a firm Go.
