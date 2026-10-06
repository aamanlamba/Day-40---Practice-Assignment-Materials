---
stage: "1 — Engage & Qualify"
title: "Qualification Checklist"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "WORKSHOP_SCENARIO.md"
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/initial-risk-register.md"
  - "docs/00-preflight/operating-contract/operating-contract-readiness.md"
  - "docs/00-preflight/ai-economics/economics-readiness.md"
  - "docs/_harness/open-questions.md"
---

# Qualification Checklist

Result per criterion: **Met** (evidenced), **Partly met**, **Not met**, **Unknown**.

| # | Criterion | Result | Evidence / reason |
|---|---|---|---|
| 1 | Business problem is stated | Met | `CHANGE_REQUEST.md:3` ([Claim]) |
| 2 | Problem is evidenced in data or metrics | Partly met | Baseline shows 7.29% exception and 4.80% error rates and 8,273.5 manual hours, but the workflow is undefined (Q-023) |
| 3 | Named sponsor | Not met | None named; P1 placeholder |
| 4 | Named business owner | Not met | alias `product-owner` only |
| 5 | Named technical owner | Partly met | alias `app-team`; backup blank |
| 6 | Urgency / trigger is stated | Not met | No date or driver in any document |
| 7 | Expected outcomes are measurable | Partly met | Qualitative outcomes; baseline exists; no targets |
| 8 | Brownfield system is accessible and runs | Met | `self_check.py` OK; 13 tests pass (0A) |
| 9 | Repository evidence sufficient to qualify | Met | 0A discovery, 12 artifacts |
| 10 | Engagement boundaries and approvals defined | Met (provisional) | 0B contract; globs approved in `write-boundaries.txt` |
| 11 | Data use is permitted | Partly met | Synthetic per `README.md:50` (unverified, A-02); real-data rules unknown (Q-009) |
| 12 | Regulatory constraints known | Not met | None in repo (Q-009) |
| 13 | Current business rules are known | Not met | `approve()` disagrees with recorded outcomes; true rules unlocated (Q-002) |
| 14 | Economics are plausible | Partly met | 0C envelope provisional: placeholder prices, cost-unit undefined (Q-024) |
| 15 | AI is justified | Not assessed | Deferred to Stage 8 by design (`README.md:51`) |
| 16 | Delivery constraints known | Met | `README.md:46-53`, 0B |
| 17 | Security posture acceptable for change | Not met | Client-asserted identity, name-based admin, bulk PII, no access audit (0A R-01, R-04) |
| 18 | Test safety net exists | Partly met | 13 passing tests; none for rules, ETL, adapters (0A R-08) |
| 19 | Stakeholder access for validation | Unknown | No stakeholder contact evidenced |

Tally: Met 5, Partly met 6, Not met 6, Unknown/Not assessed 2 (19 criteria).

[Inference] The technical and boundary-setting criteria are met; the people, urgency, regulatory and business-rule criteria are not. This pattern is typical of a viable engagement that cannot yet commit to outcomes.

## Assumptions

- [Assumption] The criteria set is the minimum a delivery engagement needs; the organisation may add its own.

## Unresolved Issues

- [Unknown] Criteria 3, 4, 6, 12, 13 and 19 depend on stakeholder input (Stage 2).

## Residual Risks

- Treating partly-met criteria as met would overstate readiness.
