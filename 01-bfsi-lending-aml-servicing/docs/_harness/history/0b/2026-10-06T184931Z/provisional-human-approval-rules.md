---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Provisional Human Approval Rules"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "README.md:51-52"
  - "CHANGE_REQUEST.md:3"
  - "docs/legacy/contact-matrix.csv"
  - "docs/_harness/write-boundaries.txt"
  - "backend/app/security.py"
---

# Provisional Human Approval Rules

Approver roles are **PROVISIONAL** function labels; no named approver is evidenced. [Verified Fact] `contact-matrix.csv` shows authorities: product-owner (application), unknown (data), ciso-delegate (security), business-ops (operations), none (ai-model).

## Actions requiring explicit human approval

| # | Action | Approver (PROVISIONAL) | Recorded where |
|---|---|---|---|
| H1 | Completing any stage (`fde.py complete`) | Engagement lead (the human running the harness) | `state.json`, run-log |
| H2 | Populating `write-boundaries.txt` | Engagement lead; security-team consulted | File header `approved-by` |
| H3 | Changing authentication/authorization behaviour or removing the characterized admin shortcut | security-team / ciso-delegate | Stage 24 report |
| H4 | Changing underwriting, AML-priority or repayment logic | product-owner / business-ops | Stage 12/15 specs |
| H5 | Building or enabling any AI/agent capability | AI-model owner (unassigned); engagement lead until assigned | Stages 8, 23 |
| H6 | Any capability affecting an approval, payment or AML disposition, even as a recommendation to an analyst | Business owner and compliance | Stage 23 |
| H7 | Adding a dependency or changing a pin | Engagement lead | Stage commit |
| H8 | Running anything against a non-local environment or real endpoint | Engagement lead and environment owner | Prohibited by default |
| H9 | Release/cutover, schema changes, data migrations | ops-lead / business-ops | Stage 30 |
| H10 | Introducing real data or sharing artifacts outside the engagement | Data owner (unclear); engagement lead until assigned | Stages 0B/25 |
| H11 | Pushing commits or opening PRs | Human, on request only | git |
| H12 | Deleting or rewriting prior evidence | Prohibited; harness history is preserved | `docs/_harness/history/` |

## Principles

1. [Verified Fact] High-impact actions stay bounded by explicit human/deterministic controls (`WORKSHOP_SCENARIO.md:15`). Approval is per action; an earlier approval does not extend to a different action or stage.
2. Approvals are recorded in writing in a repo artifact or harness state, with date and approver identity.
3. Silence is not approval. A missing owner (e.g. ai-model) means the action is blocked or escalated to the engagement lead.

## Assumptions

- [Assumption] The engagement lead can act as approver of last resort for workshop purposes only.

## Unresolved Issues

- [Unknown] Real approvers and delegation (U-01); confirm in Stage 2 (authority), Stage 23 (human control) and Stage 25 (governance).
- [Unknown] Approval turnaround expectations.

## Residual Risks

- Single-person approval across many actions is a segregation-of-duties weakness if carried beyond the workshop.
