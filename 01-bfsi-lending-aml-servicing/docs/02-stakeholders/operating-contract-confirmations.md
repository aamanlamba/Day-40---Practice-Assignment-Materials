---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Operating Contract Confirmations"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/operating-contract/open-governance-decisions.md"
  - "docs/00-preflight/operating-contract/provisional-operating-contract.md"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
  - "docs/00-preflight/operating-contract/stop-conditions.md"
  - "docs/00-preflight/operating-contract/evidence-contract.md"
  - "docs/_harness/write-boundaries.txt"
  - "docs/_harness/state.json"
  - "docs/_harness/open-questions.md"
  - "docs/02-stakeholders/approval-authority-map.md"
---

# Operating Contract Confirmations

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

Disposition of every 0B item flagged for Stage 2 (and related provisional terms). 0B artifacts are not edited; confirmations are recorded here only.

| 0B item | Subject | Disposition | Evidence |
|---|---|---|---|
| G-01 | Named sponsor, engagement lead, contract approver | Still Provisional | No person named; role "Engagement Lead" recorded in `state.json` but authority unverified; GG-01 |
| G-02 | Product-owner authority and backup | Still Provisional | Alias only (`contact-matrix.csv:2`); backup blank (GG-07) |
| G-03 | Data owner and approval authority | Still Provisional | Authority `unknown`, status `unclear` (`contact-matrix.csv:3`); GG-06 |
| G-04 | ops-lead / business-ops authority | Still Provisional | Alias only (`contact-matrix.csv:5`); backup blank |
| G-05 | Other consumers of the API | Still Provisional | [Verified Fact] the only in-repo caller is the Angular client (`legacy-api.service.ts`); external consumers not evidenced either way (Q-013) |
| G-06, G-07, G-08 | Human-control decisions | Still Provisional | Owned by Stage 23; no compliance owner (GG-02) to confirm |
| G-09 | AI-model owner | Still Provisional | `ai-model` row blank (GG-05) |
| G-10 | Regulatory, audit, retention obligations | Still Provisional | No compliance material; no owner (GG-02); Q-009 |
| G-11, G-12, G-13 | Classification, vendor approvals, access-audit policy | Still Provisional | Owned by Stage 25; security alias only |
| G-14, G-15, G-16 | Steady-state RACI, support model, contract review cadence | Still Provisional | Owned by Stage 37 |
| G-17 | Approved write globs | **Confirmed** (action taken; approver is the role, not a verified person) | `docs/_harness/write-boundaries.txt:6-7` approved 2026-10-06 |
| G-17 (content) | Per-stage proposals become one enforced union list | **Changed** | Harness enforces one list for all write stages; the approved file is the union of the proposals, so the per-stage separation in `repository-write-boundaries.md` is not technically enforced |
| G-18 | Budget and economic envelope | Still Provisional | 0C envelope exists but budget and targets unstated (Q-011, Q-026) |
| Personas P1-P10 | Assumed roles are acceptable working placeholders (Q-022) | **Confirmed** as placeholders only | Implicit by approval of 0B, 0C and Stage 1 using them; they remain unfilled roles, not people |
| H1 / H2 / H7 / H11 | Engagement-lead approvals for completion, boundaries, dependencies, pushes | **Confirmed** operationally | Recorded in `state.json`, `run-log.md`; role authority unverified |
| H3, H4, H5, H6, H8, H9, H10 | Other approval triggers | Still Provisional | Approver aliases or gaps (see `approval-authority-map.md`) |
| Evidence ladder | Ordering of evidence types (`evidence-contract.md:51`) | Still Provisional | No stakeholder has reviewed it |
| Escalation path | Agent to Engagement Lead; organisational escalation (`stop-conditions.md:40`) | Level 1 **Confirmed** in practice; rest Still Provisional | See `escalation-map.md` |
| Tool-provider data handling | Whether the tool provider's retention of inputs is acceptable (Q-021) | Still Provisional | No security/privacy owner has answered; data is assumed synthetic (A-02) |
| Terms T1-T8 | Operating contract terms | Still Provisional | Contract derived from workshop documents (`README.md:46-53`), not stakeholder agreement |

## Summary

- Confirmed: 4 items, operational only (G-17 action, persona placeholders, engagement-lead approvals, Level-1 escalation); Changed: 1 (enforced union of write globs); Still Provisional: all other items.
- [Inference] Stage 2 produced no stakeholder confirmation of authority because no stakeholder input exists. The governance gaps GG-01 to GG-08 carry forward to Stages 23, 25 and 37.
- [Verified Fact] Stage 1 condition C1 (name sponsor and owners) is **not** met by this stage. It remains open and the Stage 1 trigger to re-evaluate toward No-Go applies if it is still open at the end of Stage 2.

## Assumptions

- [Assumption] Implicit acceptance of the personas by approving earlier stages is sufficient to treat them as placeholders.

## Unresolved Issues

- [Unknown] Whether any provisional item is already settled outside the repository. Resolve by interviewing the sponsor-appointed contacts and recording signed answers as evidence.

## Residual Risks

- Treating role-recorded approvals as organisational authority would overstate governance maturity.
