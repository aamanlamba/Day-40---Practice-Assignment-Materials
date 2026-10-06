---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Stakeholder Map"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/legacy/contact-matrix.csv"
  - "docs/legacy/operations-runbook.txt"
  - "docs/legacy/interface-codes.csv"
  - "data/alerts.csv"
  - "data/applications.csv"
  - "git log (single committer account)"
  - "docs/01-engagement/team-charter.md"
  - "docs/00-preflight/operating-contract/provisional-operating-contract.md"
---

# Stakeholder Map

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

| # | Group | Stakeholder | Persona | Class | Evidence |
|---|---|---|---|---|---|
| S1 | Leadership | Executive sponsor | P1 | **Missing** (GG-01) | None named; no budget/mandate document |
| S2 | Business | Lending product owner | P3 | Evidenced (alias `product-owner`) | `contact-matrix.csv:2` approval authority for `application` |
| S3 | Business / compliance | MLRO / AML compliance | P4 | **Missing** (GG-02) | No AML owner in any document, though AML alerts exist (`alerts.csv`, 464 AML + 432 SANCTIONS) |
| S4 | Operations | Operations lead / business operations | P7 | Evidenced (aliases `ops-lead`, `business-ops`) | `contact-matrix.csv:5`; runbook describes morning exception review (`operations-runbook.txt:2`) |
| S5 | Users | Alert analysts | n/a | Evidenced in data | `alerts.owner` values `analyst_a` (553), `analyst_b` (590), `queue` (553); 104 unassigned |
| S6 | Users | Underwriters / credit reviewers | n/a | Implied | `applications.decision_source` = MANUAL (1,192), RULE, MODEL_V1, MODEL_V2; 211 blank |
| S7 | Users | KYC / servicing / collections staff | n/a | Implied | `kyc_cases.csv`, `repayments.csv` statuses; "support staff may use CSV exports" (`operations-runbook.txt:3`) |
| S8 | Engineering | Application team | P8 | Evidenced (alias `app-team`, backup blank) | `contact-matrix.csv:2` |
| S9 | Engineering | Platform team | P8 | Evidenced (alias `platform-team`, backup for security) | `contact-matrix.csv:4` |
| S10 | Data | Data operations | P6 | Evidenced (alias `data-ops`; approver `unknown`, status `unclear`) | `contact-matrix.csv:3` |
| S11 | Security | Security team / CISO delegate | P5 | Evidenced (aliases `security-team`, `ciso-delegate`) | `contact-matrix.csv:4` |
| S12 | Privacy | Privacy / DPO | P10 | **Missing** (GG-03) | PII present (`customers.csv`) but no privacy owner |
| S13 | Risk | Model risk / AI owner | P9 | Evidenced as a gap | `ai-model` row blank, status `not-established` (`contact-matrix.csv:6`) |
| S14 | Architecture | Enterprise / solution architect | n/a | **Missing** (GG-04) | No architecture owner; architecture notes are stale (`docs/legacy/architecture-notes.md:3`) |
| S15 | External | Partner API owner | n/a | Implied | `adapters/partner_adapter.py`; interface code `partner,UNKNOWN` (`interface-codes.csv:4`) |
| S16 | External | Legacy-core owner | n/a | Implied | `adapters/legacy_adapter.py`; codes `00`, `91` (`interface-codes.csv`) |
| S17 | External | Regulators / auditors | n/a | Implied, no evidence of involvement | AML/KYC domain; no compliance document |
| S18 | Affected parties | Customers and borrowers | n/a | Evidenced as data subjects | `customers.csv` 3,500 rows incl. 889 PEP-flagged |
| S19 | Engagement | Engagement lead | P2 | Evidenced as a role, not a person | `docs/_harness/state.json` records approvals as "Engagement Lead"; all git commits come from one committer account |

## Evidenced vs implied vs missing

- [Verified Fact] Five owner areas exist as aliases only (`application`, `data`, `security`, `operations`, `ai-model`); none is a named individual, and `ai-model` has no owner.
- [Verified Fact] Backups are blank for `application`, `data`, `operations` and `ai-model`.
- [Verified Fact] No CODEOWNERS file, no `.github`, no per-file ownership; commit history has 11 commits from one committer account, so authorship does not reveal domain experts.
- [Inference] Analysts, underwriters and servicing staff are the daily users, but no document describes their workflow, so their needs are unvalidated.

## Governance gaps (unassigned ownership, no names)

| ID | Gap |
|---|---|
| GG-01 | No executive sponsor |
| GG-02 | No AML / compliance owner |
| GG-03 | No privacy owner |
| GG-04 | No architecture owner |
| GG-05 | No AI-model owner (`contact-matrix.csv:6`) |
| GG-06 | No data authority (`approval_authority=unknown`) |
| GG-07 | No backups for application, data, operations |
| GG-08 | No named business owner for underwriting rules |

## Assumptions

- [Assumption] Aliases in the contact matrix refer to real, current teams; the file is inherited and undated.

## Unresolved Issues

- [Unknown] Real names, headcount, availability for all stakeholders; interviews not conducted (Q-001, Q-015). Resolve by scheduling Stage 2 interviews with the sponsor-appointed contacts.

## Residual Risks

- Reliance on aliases means decisions may reach no one; vacancy risk is invisible.
