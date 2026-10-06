---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Stakeholder Conflicts"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/02-stakeholders/stakeholder-needs-matrix.md"
  - "docs/00-preflight/operating-contract/provisional-operating-contract.md"
  - "CHANGE_REQUEST.md"
  - "backend/app/security.py"
  - "docs/00-preflight/discovery/initial-risk-register.md"
---

# Stakeholder Conflicts

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

Potential conflicts are [Inference] from the needs matrix; none is reported by a stakeholder. Each should be raised in interviews.

| ID | Conflict | Parties | Basis | Resolution route |
|---|---|---|---|---|
| X-1 | **Preserve existing behaviour** vs **fix weak security** (client-asserted identity, name-based admin are *characterized* by tests) | Product owner, operations vs security, privacy | `tests/test_security_characterization.py`; 0A R-01 | Sponsor decides priority; H3 approval; Stage 24 |
| X-2 | **Less manual triage** vs **no autonomous decisions** | Sponsor, operations vs compliance, model risk | `CHANGE_REQUEST.md:3` | Stage 8 qualification and Stage 23 human-control design |
| X-3 | **Speed/cost** (AI aid, token cost) vs **explainability and audit** | Sponsor vs compliance | 0C envelope; `audit()` unused | Stage 8/23/25 |
| X-4 | **Data completeness** (ETL drops any row with a blank) vs **retention of records** needed for compliance | Data operations vs compliance | `etl/common.py:11-13`; nulls have several meanings (`business-rules.txt:5`) | Data owner + compliance; Stage 11 |
| X-5 | **Business rules in code** (`approve()`) vs **recorded outcomes** (MODEL_V1/V2/RULE/MANUAL) | Product owner vs underwriters | 0A R-05 | Stage 5/7 with product owner |
| X-6 | **Stable CSV exports** for support vs **PII minimisation** | Operations vs privacy | `release-notes.md:6`; `admin_export` | Privacy + operations; Stage 24 |
| X-7 | **Release in a manual window** vs **automated delivery** | Operations vs engineering | `release-notes.md:3` | Stage 30 |
| X-8 | **Tool provider use** for analysis vs **data-handling policy** | Engagement vs security/privacy | 0B data constraints; Q-021 | Security + privacy, Stage 2 |

## Conflict handling rules (provisional)

- Conflicts involving security, compliance or AI go to the sponsor with the security and compliance owners; until they exist, they stay open and block the affected actions.
- [Inference] X-1 and X-2 are the most likely to stall delivery because they set the scope of any change.

## Assumptions

- [Assumption] No conflict has already been settled informally.

## Unresolved Issues

- [Unknown] Real positions and prior decisions (Stage 2 interviews).

## Residual Risks

- Unraised conflicts tend to surface late as rework or vetoes.
