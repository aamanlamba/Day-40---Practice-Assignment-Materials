---
stage: "1 — Engage & Qualify"
title: "Engagement Risks"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/discovery/initial-risk-register.md"
  - "docs/00-preflight/operating-contract/open-governance-decisions.md"
  - "docs/00-preflight/ai-economics/economics-readiness.md"
  - "docs/legacy/contact-matrix.csv"
  - "CHANGE_REQUEST.md"
---

# Engagement Risks

Engagement-level risks (not duplicating system risks R-01 to R-17 in 0A, which are referenced where relevant). Likelihood and impact: H/M/L.

| ID | Risk | L | I | Evidence | Qualification effect |
|---|---|---|---|---|---|
| E-01 | No accountable sponsor; engagement could stall or lose mandate | H | H | No named sponsor; P1 placeholder ([Verified Fact]: `contact-matrix.csv`) | Condition C1 |
| E-02 | Success undefined; no urgency or target, so value cannot be proven | H | H | `CHANGE_REQUEST.md` qualitative only | Condition C2 |
| E-03 | True business rules unknown; preserving behaviour cannot be proven | H | H | 0A R-05; `approve()` conflicts with recorded outcomes | Condition C3 |
| E-04 | Regulatory obligations unknown in an AML/KYC domain | M | H | No compliance material in repo (Q-009) | Condition C4 |
| E-05 | Security debt may block safe exposure of any new capability | H | H | 0A R-01, R-04 | Condition C5 |
| E-06 | Baseline cannot be attributed to a workflow, so ROI is not measurable | H | M | Q-023, Q-024 | Condition C2 |
| E-07 | Single-person approvals; weak governance | H | M | 0B approval rules | Condition C1 |
| E-08 | Premature AI: change request invites AI "triage" before need is shown | M | H | `README.md:51`; 0C economics provisional | Stage 8 gate |
| E-09 | Stakeholders unavailable to validate assumptions | M | H | No contact evidence | Condition C1 |
| E-10 | Legacy documents stale, leading to wrong inferences | M | M | `docs/legacy/*` carry stale warnings | Mitigated by evidence ladder (0B) |
| E-11 | Synthetic-data conclusions may not transfer to real data | M | M | A-02 | Note in Stage 4/5 |
| E-12 | Cost figures are placeholders and could be mistaken for a business case | M | M | 0C | Condition C2 |
| E-13 | Thin test net makes safe change slow | H | M | 0A R-08 | Addressed in Stage 12/26 |

## Non-viability signals checked

- No sign that the system is unrunnable, undocumented beyond repair, or legally blocked. [Verified Fact] It runs and passes its tests.
- The strongest "premature" signal is the absence of people and targets, not technical infeasibility.

## Assumptions

- [Assumption] Ratings use qualitative judgement with the 0A/0B/0C evidence; no probability data exists.

## Unresolved Issues

- [Unknown] Hidden obligations (legal, contractual) outside the repository.

## Residual Risks

- Risks E-01 and E-03 could become blocking if not resolved by Stage 3.
