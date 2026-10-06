---
stage: "3 — Frame Problem & Value"
title: "Personas"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/02-stakeholders/stakeholder-map.md"
  - "docs/02-stakeholders/stakeholder-needs-matrix.md"
  - "data/alerts.csv"
  - "data/applications.csv"
  - "docs/legacy/operations-runbook.txt"
  - "docs/legacy/contact-matrix.csv"
---

# Personas

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

Working personas grounded in evidence visible in the repository. They are not interview-based.

| ID | Persona | Evidence of existence | Goals | Pain points ([Inference]) | Authority |
|---|---|---|---|---|---|
| PE-1 | Alert analyst | `alerts.owner`: `analyst_a` 553, `analyst_b` 590, `queue` 553 | Clear a prioritised queue; close with confidence | Many false positives (23.8%); mixed alert sources; missing owners (104) | Recommends disposition; final authority unconfirmed (GG-02) |
| PE-2 | Compliance / AML lead | none (GG-02) | Defensible dispositions; audit trail | No explanation of ranking; unused audit helper | Unassigned |
| PE-3 | Underwriter / credit reviewer | `decision_source=MANUAL` 1,192; four decision sources coexist | Consistent decisions | Conflicting rule generations; 211 undecided-source records | Alias `product-owner` |
| PE-4 | Servicing / collections officer | `repayments.csv` statuses; 2,529 repayments over 90 days past due | Resolve exceptions quickly | Customer mismatches (218); stale CSV extracts | Alias `ops-lead` |
| PE-5 | Operations lead | `operations-runbook.txt`; `business-rules.txt:4` | Reconciliation before 08:00; stable release | Manual morning checks; rollback unclear | Alias `ops-lead` / `business-ops` |
| PE-6 | Product owner, lending | `contact-matrix.csv:2` | Throughput and unchanged behaviour | Any change that moves approvals | Alias `product-owner` |
| PE-7 | Security / privacy reviewer | `contact-matrix.csv:4` | Controlled access to personal data | Bulk unmasked records; client-asserted identity | Alias `security-team`; privacy owner missing |
| PE-8 | Executive sponsor | none (GG-01) | Lower cost, controlled risk | No targets or deadline | Unassigned |
| PE-9 | Customer / borrower (affected party) | `customers.csv` 3,500 | Fair, timely outcome; privacy | Wrong holds or declines | n/a |

[Verified Fact] 889 of 3,500 customers (25.4%) are flagged as politically exposed, so a sizeable share of alert reviews involve heightened-scrutiny customers.

## Assumptions

- [Assumption] Analyst identifiers in the data denote real reviewer roles.

## Unresolved Issues

- [Unknown] Actual day-in-the-life of each persona (interviews pending).

## Residual Risks

- Persona pain points inferred from data may miss the true daily friction.
