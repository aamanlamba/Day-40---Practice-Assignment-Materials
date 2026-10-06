---
stage: "1 — Engage & Qualify"
title: "Engagement Go / No-Go"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/01-engagement/qualification-checklist.md"
  - "docs/01-engagement/engagement-risks.md"
  - "docs/01-engagement/engagement-canvas.md"
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/operating-contract/operating-contract-readiness.md"
  - "docs/00-preflight/ai-economics/economics-readiness.md"
  - "docs/legacy/contact-matrix.csv"
  - "CHANGE_REQUEST.md"
---

# Engagement Go / No-Go

Classification: Conditional Go

## Basis

**Validated evidence (supports proceeding)**

- [Verified Fact] The system runs: self-check OK, 13/13 tests pass; 21 components mapped with repository citations (0A).
- [Verified Fact] The business domain and problem area exist in the data: alerts, applications, repayments and a 180-day effort/exception baseline (`data/`; 0C).
- [Verified Fact] Boundaries and approvals are defined: operating contract, write globs approved in `docs/_harness/write-boundaries.txt`, evidence and change rules (0B).
- [Verified Fact] A provisional cost envelope exists, with deterministic and conventional options costed alongside AI (0C).
- [Inference] No technical or legal blocker is evident, so the engagement is viable to continue in read-only and analysis stages.

**Stakeholder claims (not validated)**

- [Claim] Manual triage and servicing exceptions are a problem worth solving (`CHANGE_REQUEST.md:3`).
- [Claim] Existing behaviour must be preserved and decisions must not become autonomous (`CHANGE_REQUEST.md:3`).
- [Claim] The estate is business-critical (`WORKSHOP_SCENARIO.md:5`).
- No stakeholder has been heard from; the request is "a business pressure statement, not an approved solution design" (`CHANGE_REQUEST.md:7`).

**Why not a plain Go**

- Sponsor, business owner, urgency and measurable targets are missing (criteria 3, 4, 6, 7).
- True business rules and regulatory constraints are unknown (criteria 12, 13).
- Security gaps in the existing system are unaddressed (criterion 17).

**Why not No-Go**

- Nothing found makes the engagement non-viable; the gaps are fillable by stakeholder input and by later discovery stages. Continuing in read-only stages costs little and is reversible.

## Conditions

| ID | Condition | Who must satisfy | Needed by |
|---|---|---|---|
| C1 | Name a sponsor, business owner, technical owner and approvers (replace personas P1-P10 with people) | Executive Sponsor (P1) | Before Stage 3 starts; confirmed in Stage 2 |
| C2 | State measurable outcomes and a trigger/deadline; define "work item" and "cost unit" so a workflow baseline can be taken | Sponsor (P1), Product Owner (P3), Operations Lead (P7) | Before Stage 4 completes |
| C3 | Identify the authoritative approval and AML-priority rules and who owns them | Product Owner (P3), MLRO (P4) | Before Stage 5 completes |
| C4 | Identify applicable regulatory, audit and retention obligations | MLRO (P4), Privacy (P10), Security (P5) | Before any write stage (15, 19-22, 24, 26-28, 30, 31) |
| C5 | Accept, or schedule treatment of, the known security gaps (R-01, R-04) before any new capability exposes data | Security Architect (P5), Sponsor (P1) | Before any write stage |
| C6 | No AI/agent build until Stage 8 qualifies it and Stage 23 defines human control | Engagement Lead (P2) | Standing |

If C1 is not satisfied by the end of Stage 2, the classification should be re-evaluated toward No-Go.

## Confidence

Medium that the engagement is viable; Low on value, owing to the missing targets.

## Human approval

Recorded at completion via `fde.py complete 1 --approved-by ...`. Until then this classification is a recommendation, not a decision.

## Assumptions

- [Assumption] The Stage 2 interviews will be possible; if stakeholders cannot be reached the classification reverts to No-Go pending access.
- [Assumption] Conditions are owned by the personas named; real owners are unconfirmed.

## Unresolved Issues

- [Unknown] Whether the conditions can be met on the engagement timeline (no timeline exists).

## Residual Risks

- A Conditional Go can be treated as Go in practice if the conditions are not tracked; they are tracked in `open-qualification-questions.md` and the open question log.
