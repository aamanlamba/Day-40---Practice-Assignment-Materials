---
stage: "1 — Engage & Qualify"
title: "Team Charter"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/operating-contract/provisional-operating-contract.md"
  - "docs/00-preflight/operating-contract/provisional-human-approval-rules.md"
  - "docs/00-preflight/operating-contract/provisional-tool-agent-permissions.md"
  - "docs/legacy/contact-matrix.csv"
  - "docs/_harness/write-boundaries.txt"
---

# Team Charter

**PROVISIONAL.** Roles are assumed personas from 0B (`provisional-operating-contract.md`), not evidenced people. [Verified Fact] `contact-matrix.csv` lists only team aliases and leaves backups blank for application, data and operations.

## Engagement roles

| Role | Persona | Responsibility in this engagement | Evidence of real holder |
|---|---|---|---|
| Executive Sponsor | P1 | Funds and scopes; accepts residual risk; names owners; Go/No-Go business acceptance | None |
| Engagement Lead | P2 | Runs the spine, approves stage completion and commits; escalation point | [Verified Fact] the human approving stages is recorded as "Engagement Lead" in `docs/_harness/state.json` |
| Product Owner, Lending | P3 | Underwriting/servicing rules and priorities | alias `product-owner` |
| MLRO / AML Compliance | P4 | AML rules, disposition, regulatory view | None |
| Security Architect | P5 | AuthN/authZ, secrets, tool approval | aliases `security-team`, `ciso-delegate` |
| Data Owner | P6 | Data definition, lineage, use approval | alias `data-ops`, status "unclear" |
| Operations Lead | P7 | Baselines, runbook, release windows | aliases `ops-lead`, `business-ops` |
| Platform Lead | P8 | Code ownership, API consumers, review | alias `app-team` |
| Model Risk Manager | P9 | Any AI capability | none ("not-established") |
| Privacy / DPO | P10 | PII handling | None |
| AI delivery agent | n/a | Claude Code: analysis, drafting, implementation within approved globs | [Verified Fact] limits in `provisional-tool-agent-permissions.md` |

## Working agreements (from 0B)

- Stage completion, approval of globs and any push are human decisions. Write boundaries are the approved globs in `docs/_harness/write-boundaries.txt` (approved 2026-10-06).
- Evidence tagged Verified Fact / Inference / Assumption / Unknown; legacy docs treated as non-authoritative.
- Open questions go to `docs/_harness/open-questions.md` on completion of each stage.
- Escalation: agent to Engagement Lead; organisational escalation unconfirmed.

## Gaps

- No named sponsor, no named business owner, no AI-model owner; single-person approval.

## Assumptions

- [Assumption] The Engagement Lead is authorised to approve stage completion for the workshop only.

## Unresolved Issues

- [Unknown] Real people for P1, P3-P10, availability and decision turnaround (Q-001, Q-015, Q-022). Resolve in Stage 2.

## Residual Risks

- Segregation of duties is weak while one person approves everything.
