---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Open Governance Decisions"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/assumptions-unknowns.md"
  - "docs/legacy/contact-matrix.csv"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
  - "README.md:51"
---

# Open Governance Decisions

Decisions that cannot be made from current evidence. "Plausible confirmer" is a function suggested by `contact-matrix.csv`, not an assigned owner (PROVISIONAL).

## Confirm in Stage 2 (Stakeholders and authority)

| ID | Decision | Plausible confirmer | Evidence gap |
|---|---|---|---|
| G-01 | Named sponsor, engagement lead, approver of this contract | Sponsor | No named people (U-01) |
| G-02 | Product-owner authority over application/underwriting rules, and backups | product-owner (`contact-matrix.csv:2`) | Backup blank |
| G-03 | Data owner and approval authority for data use | data-ops | Authority "unknown", status "unclear" (`contact-matrix.csv:3`) |
| G-04 | ops-lead and business-ops authority over runbook and release | ops-lead / business-ops | Backup blank |
| G-05 | Other consumers of the API | app-team | U-13 |

## Confirm in Stage 23 (Human control)

| ID | Decision | Plausible confirmer | Evidence gap |
|---|---|---|---|
| G-06 | Which analyst/underwriter actions must stay human-decided | Business owner, compliance | `CHANGE_REQUEST.md:3` is general |
| G-07 | Override, escalation and review-evidence requirements for surfaced high-risk cases | Compliance / AML lead | No AML policy in repo |
| G-08 | Approval gates H3-H6 in `provisional-human-approval-rules.md` | Engagement lead and owners | Provisional |

## Confirm in Stage 25 (Governance)

| ID | Decision | Plausible confirmer | Evidence gap |
|---|---|---|---|
| G-09 | AI-model owner and accountability | Executive sponsor | `ai-model` row blank ("not-established") |
| G-10 | Applicable regulation, audit and retention obligations (AML/KYC) | Compliance / ciso-delegate | U-09 |
| G-11 | Data classification, residency and handling for real data | Data owner, security-team | |
| G-12 | Vendor/tool approvals for AI tooling | security-team, procurement | |
| G-13 | Policy on logging and auditing data access (`audit()` is unused) | security-team | |

## Close in Stage 37 (Operating model)

| ID | Decision | Plausible confirmer | Evidence gap |
|---|---|---|---|
| G-14 | Steady-state ownership, RACI and backups per area | Executive sponsor | Backups blank for application, data, operations |
| G-15 | Support model, on-call and incident roles | ops-lead | Runbook labelled possibly stale |
| G-16 | Review cadence of this contract and its successor | Sponsor | |

## Also required before write stages

- G-17: A human transfers approved globs to `docs/_harness/write-boundaries.txt` and records the approver (see `repository-write-boundaries.md`).
- G-18 (Stage 0C): budget and economic envelope (U-11).

## Assumptions

- [Assumption] Stages 2, 23, 25 and 37 are the confirmation points named in the 0B gate.

## Unresolved Issues

- [Unknown] Every item above is open at the close of 0B; none is resolved by evidence.

## Residual Risks

- Entering implementation stages with these open raises the risk of rework or unauthorised change.
