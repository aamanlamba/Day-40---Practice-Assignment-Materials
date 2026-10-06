---
stage: "3 — Frame Problem & Value"
title: "Scope and Exclusions (Problem Level)"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "README.md"
  - "docs/01-engagement/engagement-canvas.md"
  - "docs/00-preflight/operating-contract/scope-boundaries.md"
---

# Scope and Exclusions (Problem Level)

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

## In scope (problem level)

- Prioritisation and explanation of fraud, AML, sanctions and KYC-refresh alerts for analyst review.
- Detection and explanation of loan-servicing exceptions, including repayment/application mismatches.
- Evidence for reviewers: the facts that bear on a case, in one place.
- Preservation of existing lending and payment results.
- Records of who reviewed what and why.

## Out of scope

| Exclusion | Reason |
|---|---|
| Autonomous financial decisions (approve, decline, pay, block, report) | `CHANGE_REQUEST.md:3`; 0B T6 |
| Changing underwriting policy or credit appetite | Not requested; owner unassigned (GG-08) |
| Replacing the core lending or payment systems | Not requested; unseen systems |
| Real customer data | 0B data constraints |
| Regulatory reporting submissions | Not requested; compliance owner missing |
| Choice of tooling or technique | Stage 8 and later |

## Undecided (needs a stakeholder)

- Whether KYC cases and beneficiary data are included (Q-006).
- Whether alert generation itself is in scope, or only handling of alerts already raised.
- Whether customer-facing communications are affected.

## Assumptions

- [Assumption] Handling of alerts, not their generation, is the intended scope.

## Unresolved Issues

- [Unknown] Items under Undecided; ask the sponsor and compliance owner (Stage 2/3 follow-up).

## Residual Risks

- Scope uncertainty around alert generation could double the effort.
