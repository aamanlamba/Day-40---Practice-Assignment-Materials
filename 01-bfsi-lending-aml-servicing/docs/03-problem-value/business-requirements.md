---
stage: "3 — Frame Problem & Value"
title: "Business Requirements"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "data/baseline_metrics.csv"
  - "data/alerts.csv"
  - "docs/legacy/business-rules.txt"
  - "docs/legacy/release-notes.md"
  - "docs/03-problem-value/jobs-to-be-done.md"
  - "docs/00-preflight/discovery/initial-risk-register.md"
---

# Business Requirements

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

Requirements are technology-neutral and each has an ID and source. A *Claim* or *Hypothesis* source means the requirement still needs stakeholder confirmation. Priority (MoSCoW) is provisional.

| ID | Requirement | Source | JTBD | Priority |
|---|---|---|---|---|
| BR-001 | Each open alert shall show a priority ranking visible to the reviewer | Claim `CHANGE_REQUEST.md:3` | JTBD-01 | Must |
| BR-002 | Each ranking shall be accompanied by the reasons and evidence that produced it | Claim `CHANGE_REQUEST.md:3` ("explain routing") | JTBD-01, JTBD-04 | Must |
| BR-003 | A reviewer shall be able to see the customer, transaction and loan facts relevant to an alert together | Hypothesis (JTBD-02); Evidence: data split across files | JTBD-02 | Should |
| BR-004 | Every alert shall have a responsible owner or be visibly flagged as unowned | Evidence: 104 unowned alerts, 54 open/escalated | JTBD-01 | Must |
| BR-005 | A reviewer's disposition and reasoning shall be recorded and retrievable | Hypothesis (JTBD-03, JTBD-04); Evidence: no audit trail in use | JTBD-03, JTBD-04 | Must |
| BR-006 | No financial decision shall be made or executed without a human decision-maker, unless explicitly approved | Claim `CHANGE_REQUEST.md:3` | JTBD-08 | Must |
| BR-007 | Existing lending and payment results shall remain unchanged unless a change is explicitly approved | Claim `CHANGE_REQUEST.md:3` | JTBD-08 | Must |
| BR-008 | Repayment and loan records that disagree on the customer shall be reported with their cause | Evidence: 218 mismatches | JTBD-06 | Should |
| BR-009 | The approval and priority rules in force shall be documented with an accountable owner | Evidence: rule/outcome mismatch (0A R-05); GG-08 | JTBD-05 | Must |
| BR-010 | Access to personal data shall be limited to what a role needs and shall be logged | Evidence: 0A R-01, R-04 | JTBD-09 | Must |
| BR-011 | Daily exception results shall be available before 08:00 local | Evidence: `business-rules.txt:4` | JTBD-07 | Should |
| BR-012 | Support staff shall still be able to obtain CSV extracts during the transition | Evidence: `release-notes.md:6` | JTBD-07 | Should |
| BR-013 | The programme shall measure results against the pre-change baseline | Hypothesis (JTBD-10); Evidence: `data/baseline_metrics.csv` | JTBD-10 | Must |
| BR-014 | Records of case handling shall be retained as required by applicable regulation | Hypothesis; regulation unknown (Q-009) | JTBD-04 | Must (content pending) |

## Traceability notes

- [Verified Fact] None of these requirements is stakeholder-approved; 0 of 14 have a confirmed owner (GG-01, GG-02, GG-08).
- BR-006 and BR-007 are constraints taken directly from the change request and 0B terms T3, T6.
- BR-014 and BR-009 cannot be completed until the compliance owner and rule owner exist.

## Assumptions

- [Assumption] MoSCoW priorities are provisional.

## Unresolved Issues

- [Unknown] Stakeholder confirmation and priority for each; regulatory content for BR-014.

## Residual Risks

- Requirements derived from one-paragraph change request risk missing needs that interviews would surface.
