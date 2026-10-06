---
stage: "1 — Engage & Qualify"
title: "Engagement Canvas"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "WORKSHOP_SCENARIO.md"
  - "README.md"
  - "docs/legacy/contact-matrix.csv"
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/operating-contract/provisional-operating-contract.md"
  - "docs/00-preflight/ai-economics/economics-readiness.md"
---

# Engagement Canvas

Claims are labelled **[Claim]** (stated in a document but not independently validated). Evidence is **[Verified Fact]**. Personas P1-P10 are the assumed roles from 0B; none is a named person.

| Element | Content | Status |
|---|---|---|
| Client context | BFSI estate for digital lending, AML and loan servicing inherited during an "enterprise transformation" with incomplete documentation and ownership (`WORKSHOP_SCENARIO.md:5`) | [Claim] by scenario text; [Verified Fact] that the repo matches the described shape (0A) |
| Business problem | "Reduce manual fraud/AML triage and loan-servicing exceptions while preserving existing lending and payment behavior" (`CHANGE_REQUEST.md:3`) | [Claim]; a "business pressure statement, not an approved solution design" (`CHANGE_REQUEST.md:7`) |
| Proposed enhancement | Surface high-risk cases with evidence, explain routing, support analyst review, avoid autonomous financial decisions (`CHANGE_REQUEST.md:3`) | [Claim]; not approved |
| Sponsor | None named. P1 (Executive Sponsor) is an assumed placeholder | [Unknown] |
| Business owner | None named. `application` row lists product-owner as approver, no person (`contact-matrix.csv:2`) | [Unknown] |
| Technical owner | `app-team` alias, backup blank (`contact-matrix.csv:2`) | Partial [Verified Fact]: alias only |
| Urgency | No date, deadline or trigger stated in any document | [Unknown] |
| Expected outcomes | Qualitative only (less manual triage/exceptions, preserve behaviour). No target numbers | [Claim]; baseline exists but targets do not |
| Dependencies | Stage 2 confirmation of owners; source of true decision rules; data definitions; human approval of write boundaries (done: `docs/_harness/write-boundaries.txt`) | Mixed |
| Delivery constraints | Brownfield; preserve behaviour; synthetic data only; no AI before Stage 8; human control for high-impact actions; read-only until approved stages (`README.md:46-53`, 0B) | [Verified Fact] (documented constraints) |
| Measured baseline | 127,617 items over 180 days; 8,273.5 manual hours; error 4.80%; exception 7.29% (`data/baseline_metrics.csv`, 0C) | [Verified Fact]; meaning of "work item" unknown (Q-023) |
| System condition | Read-only API over CSVs; 13/13 tests pass; business rules not wired; weak authN/authZ (0A R-01, R-04, R-05) | [Verified Fact] |

## Claim vs evidence summary

- [Verified Fact] The problem domain is present in the repo: 1,800 alerts (923 open/escalated), 5,000 applications, 5,000 repayments, with manual-effort metrics.
- [Claim] That manual triage is the dominant cost or that alert triage is where the baseline hours go: not demonstrated. The baseline file does not say which workflow its hours belong to.
- [Claim] That the business wants this now: no urgency evidence.

## Assumptions

- [Assumption] The change request is a genuine business statement rather than only workshop scaffolding; the scenario text says it is not an approved design.
- [Assumption] Personas P1-P10 stand in for real stakeholders until Stage 2.

## Unresolved Issues

- [Unknown] Named sponsor, business owner, technical owner, urgency and target outcomes (Q-001, Q-011, Q-015).

## Residual Risks

- Starting design or build work without a named sponsor or measurable outcome risks effort with no accountable owner.
