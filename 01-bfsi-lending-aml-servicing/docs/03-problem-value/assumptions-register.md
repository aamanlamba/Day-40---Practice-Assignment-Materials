---
stage: "3 — Frame Problem & Value"
title: "Assumptions Register (Stage 3)"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/03-problem-value/*.md"
  - "docs/_harness/open-questions.md"
  - "docs/00-preflight/discovery/assumptions-unknowns.md"
---

# Assumptions Register (Stage 3)

Assumptions made while framing the problem. Earlier-stage registers (0A A-01 to A-07, etc.) remain in force.

| ID | Assumption | Impact if false | Log ref | Validate with | When |
|---|---|---|---|---|---|
| A3-01 | Baseline manual hours include alert and exception review | Medium impact: invalidates SC-01/04/05/06 if false | Q-023 | P7 | Stage 4 |
| A3-02 | Poor prioritisation and fragmented information drive review time (root-problem hypothesis) | High | none | P4, P7, analysts | Stage 4/5 |
| A3-03 | A false-positive share near 24% is higher than acceptable | Medium | Q-011 | P1, P4 | Stage 4 |
| A3-04 | Missed cases are not currently a larger harm than false positives | High; no miss data exists | none | P4 | Stage 4/5 |
| A3-05 | The change request represents a genuine business need and priority | High | Q-015 | P1 | Stage 2/3 follow-up |
| A3-06 | Labour value of $30/h applies | Medium | Q-026 | P1, P2 | Stage 3/4 |
| A3-07 | Reviewers will adopt a new prioritised view | High | none | Analysts, P7 | Stage 23/34 |
| A3-08 | Legacy notes still describe real practice | Medium | none | P7 | Stage 5 |
| A3-09 | Synthetic data behaves like real data for sizing purposes | Medium | A-02 | P6 | Stage 4/5 |
| A3-10 | No regulatory rule forbids the intended handling of case data | High | Q-009 | P4, P10 | Stage 25 (needed earlier) |

## Highest-impact to validate first

1. A3-02 root problem; A3-04 miss rate; A3-05 genuine need; A3-10 regulation.
- [Inference] If A3-02 or A3-05 is false, much of the requirement set would change; if A3-10 is false, retention and logging requirements (BR-005, BR-014, NFR-013) would change.

## Assumptions

- This register is itself the list of assumptions for Stage 3.

## Unresolved Issues

- [Unknown] Which assumptions stakeholders reject; validation needs interviews (blocked by C1).

## Residual Risks

- Unvalidated high-impact assumptions can propagate into Stages 4-9.
