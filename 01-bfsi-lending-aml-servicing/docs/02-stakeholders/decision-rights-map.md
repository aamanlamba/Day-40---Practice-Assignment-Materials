---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Decision Rights Map"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/legacy/contact-matrix.csv"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
  - "docs/00-preflight/operating-contract/open-governance-decisions.md"
  - "docs/_harness/state.json"
  - "docs/_harness/write-boundaries.txt"
---

# Decision Rights Map

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

Evidence of who may decide each matter. "Evidenced" means a repository document or harness record shows it; everything else is a **governance gap**.

| Decision area | Who decides (evidenced) | Source | Status |
|---|---|---|---|
| Application / underwriting rules | `product-owner` (as approval authority); owner alias `app-team` | `contact-matrix.csv:2` | Evidenced as alias; no named person; no backup (GG-07, GG-08) |
| Data definitions, quality, use | `data-ops` is owner; approval authority `unknown` | `contact-matrix.csv:3` | **Gap GG-06** |
| Security controls, access, secrets | `security-team`, approver `ciso-delegate`, backup `platform-team` | `contact-matrix.csv:4` | Evidenced as alias |
| Operations, runbook, release timing | `ops-lead`, approver `business-ops` | `contact-matrix.csv:5`; maintenance windows (`release-notes.md:3`) | Evidenced as alias; no backup |
| AI model use and risk | None | `contact-matrix.csv:6` | **Gap GG-05** |
| AML rules and alert disposition | None | no document | **Gap GG-02** |
| Privacy and data protection | None | no document | **Gap GG-03** |
| Architecture and technology choices | None | stale notes only | **Gap GG-04** |
| Budget, scope and funding | None | no document | **Gap GG-01** |
| Stage completion in this engagement | Engagement Lead role | `docs/_harness/state.json` `approved_by` for 0B, 0C, 1 | [Verified Fact]; the role's own authority is provisional |
| Repository write boundaries | Engagement Lead role (approved 2026-10-06) | `docs/_harness/write-boundaries.txt:6-7` | [Verified Fact] action taken |

## Decision rights implied by 0B (still provisional)

- H3 (security change), H4 (rules change), H5/H6 (AI), H9 (release), H10 (real data): approvers named by role in `provisional-human-approval-rules.md`; none confirmed by a stakeholder.
- [Inference] Authority for AML-related decisions (H4, H6) cannot be exercised because no compliance owner exists.

## Assumptions

- [Assumption] The contact matrix lists the current authority structure; its date is unknown.

## Unresolved Issues

- [Unknown] Delegation, thresholds (e.g. value limits) and who may act when the named authority is absent (GG-07).

## Residual Risks

- Decisions needing an unassigned authority would be blocked or made by default by whoever is available.
