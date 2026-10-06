---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Escalation Map"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/operating-contract/stop-conditions.md"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
  - "docs/legacy/contact-matrix.csv"
  - "docs/00-preflight/discovery/initial-risk-register.md"
---

# Escalation Map

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

## Routes

| Trigger | First stop | Next | Final | Status |
|---|---|---|---|---|
| Engagement stop condition (S-01 to S-15) | Engagement Lead (P2) | Sponsor (P1) | Sponsor | Level 1 confirmed in practice; Levels 2-3 gap GG-01 |
| Security incident or finding (e.g. R-01, R-04) | `security-team` | `ciso-delegate` | Sponsor | Aliases evidenced (`contact-matrix.csv:4`); no names |
| Rule or business-behaviour question | `product-owner` | `business-ops` | Sponsor | Aliases evidenced; no AML branch (GG-02) |
| Data quality or use question | `data-ops` | authority `unknown` | n/a | Broken at level 2 (GG-06) |
| Operations incident or release problem | `ops-lead` | `business-ops` | Sponsor | Aliases evidenced; no backup |
| AI-related concern | none | none | none | GG-05 |
| Privacy concern | none | none | none | GG-03 |
| Regulatory contact | none | none | none | No evidence anyone owns this |

## Observations

- [Verified Fact] The only operational escalation target is the Engagement Lead role (0B `stop-conditions.md`).
- [Verified Fact] `platform-team` is the only evidenced backup, and only for security.
- [Inference] Three routes (AI, privacy, regulatory) end nowhere, and the data route ends at `unknown`.
- Provisional rule: where a route ends at a gap, the issue is recorded in `docs/_harness/open-questions.md` and the Engagement Lead holds it; blocked actions stay blocked.

## Assumptions

- [Assumption] Aliases correspond to people who would respond.

## Unresolved Issues

- [Unknown] Response times, on-call expectations and out-of-hours coverage; whether a regulator-facing contact exists.

## Residual Risks

- Incidents touching data, AI or privacy have no evidenced owner and could stall.
