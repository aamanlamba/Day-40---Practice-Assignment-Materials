---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Approval Authority Map"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/legacy/contact-matrix.csv"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
  - "docs/_harness/state.json"
  - "docs/_harness/write-boundaries.txt"
  - "docs/_harness/run-log.md"
---

# Approval Authority Map

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

Maps each 0B approval trigger (H1-H12) to the approver now evidenced, and what is still a gap.

| Trigger | Action | 0B approver (provisional) | Evidenced approver now | Gap |
|---|---|---|---|---|
| H1 | Complete a stage | Engagement lead | Role "Engagement Lead" recorded on 0B, 0C, 1 (`state.json`) | Role holder and authority not independently confirmed |
| H2 | Populate write boundaries | Engagement lead; security consulted | Done by Engagement Lead role; security consultation not recorded | Security consultation missing |
| H3 | Change authN/authZ | security-team / ciso-delegate | Alias evidenced (`contact-matrix.csv:4`) | No named person |
| H4 | Change underwriting/AML/repayment logic | product-owner / business-ops | `product-owner` alias for application only | AML owner missing (GG-02) |
| H5 | Build or enable AI/agent capability | AI-model owner | None | GG-05; falls back to Engagement Lead per 0B |
| H6 | Capability affecting approval, payment or AML disposition | Business owner + compliance | `product-owner` alias only | GG-02 |
| H7 | Add dependency / change pin | Engagement lead | Same as H1 | Same as H1 |
| H8 | Non-local environment or real endpoint | Engagement lead + environment owner | None for environment | Environment owner unknown (Q-003) |
| H9 | Release, cutover, schema or data migration | ops-lead / business-ops | Aliases evidenced | No backups |
| H10 | Real data or sharing outside the engagement | Data owner | `data-ops`, authority `unknown` | GG-06 |
| H11 | Push commits / open PRs | Human on request | Human | None |
| H12 | Delete or rewrite prior evidence | Prohibited | n/a | None |

## Observations

- [Verified Fact] Only H1, H2, H7 and H11 have an acting approver recorded; the rest rest on aliases or gaps.
- [Inference] While GG-02, GG-05 and GG-06 remain open, H4, H5, H6 and H10 cannot be approved by any evidenced authority, so those actions stay blocked (0B stop condition S-11).
- Single-person approval across H1-H2-H7 remains a segregation-of-duties weakness.

## Assumptions

- [Assumption] The engagement approver acts for the workshop only.

## Unresolved Issues

- [Unknown] Whether any approver has delegates or thresholds; whether security was consulted on write boundaries (Q-016 was answered by the Engagement Lead only).

## Residual Risks

- Approvals recorded by a role, not a person, are weak audit evidence.
