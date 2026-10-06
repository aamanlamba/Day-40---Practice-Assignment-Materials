---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Provisional Operating Contract"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/initial-risk-register.md"
  - "docs/00-preflight/discovery/assumptions-unknowns.md"
  - "docs/legacy/contact-matrix.csv"
  - "README.md:46-53 (workshop constraints)"
  - "WORKSHOP_SCENARIO.md:11-17 (non-negotiables)"
  - "CHANGE_REQUEST.md"
---

# Provisional Operating Contract

All decisions here are **PROVISIONAL**. Nothing in this contract is final governance authority; it is derived from Stage 0A evidence and must be confirmed in Stages 2, 23, 25 and 37 (see `open-governance-decisions.md`).

## Engagement summary

- [Verified Fact] System: BFSI digital lending, AML and loan servicing brownfield estate (`README.md:1-5`). Business pressure: reduce manual fraud/AML triage and servicing exceptions "while preserving existing lending and payment behavior", with no autonomous financial decisions unless explicitly approved (`CHANGE_REQUEST.md:3`).
- [Verified Fact] Stated non-negotiables: brownfield not greenfield; preserve and prove critical behaviour before change; evidence outranks assumptions; high-impact actions remain under explicit human/deterministic control (`WORKSHOP_SCENARIO.md:11-17`).
- [Verified Fact] Stated constraint: "Do not introduce AI or agent autonomy until Stage 8 qualifies it" (`README.md:51`).

## Contract terms (provisional)

| # | Term | Status | Basis |
|---|---|---|---|
| T1 | Work proceeds through the AI FDE spine in order; no stage is skipped without recorded justification | PROVISIONAL | Harness dependency checks; `README.md:48` |
| T2 | Discovery/analysis stages are read-only; only write stages named in `repository-write-boundaries.md` may change code, and only inside human-approved globs | PROVISIONAL | [Verified Fact] `docs/_harness/write-boundaries.txt` has no globs today |
| T3 | Legacy behaviour is evidence to characterise, not assumed correct | PROVISIONAL | `README.md:49`; 0A finding that rule code diverges from recorded outcomes (R-05) |
| T4 | Only the bundled synthetic data may be used; no real customer or company data enters the repo or any tool | PROVISIONAL | `README.md:50`, `data/README.md:3`; A-02 unverified |
| T5 | No AI/agent capability is built or enabled before Stage 8 qualification and Stage 23 human-control design | PROVISIONAL | `README.md:51` |
| T6 | Any financial decision (approval, payment, AML disposition) stays human/deterministic unless explicitly approved | PROVISIONAL | `CHANGE_REQUEST.md:3` |
| T7 | Every artifact carries evidence tags and cites repo paths; unsupported claims are Unknowns | PROVISIONAL | `evidence-contract.md` |
| T8 | Stop conditions in `stop-conditions.md` override schedule | PROVISIONAL | This stage |

## Roles

- [Verified Fact] `docs/legacy/contact-matrix.csv` lists team aliases only: application = app-team (approver product-owner), data = data-ops (approver "unknown", status "unclear"), security = security-team (backup platform-team, approver ciso-delegate), operations = ops-lead (approver business-ops), ai-model = unassigned ("not-established"). No named individuals; backups are blank for application, data and operations.
- [Unknown] Who the engagement sponsor is and who approves this contract beyond the human who runs `fde.py complete 0B --approved-by`. Every role is a PROVISIONAL functional placeholder.

## Assumptions

- [Assumption] The human executing the harness acts as interim approving authority for stage completion; this is not evidence of organisational decision rights.
- [Assumption] The contract applies to this repository folder only (A-01).

## Unresolved Issues

- [Unknown] Sponsor, approver of the final contract, data owner, AI-model owner (U-01).
- [Unknown] Compliance obligations that may add terms (U-09).

## Residual Risks

- Terms rest on workshop documents rather than a signed engagement agreement; their authority is unverified.
- The repo is nested in a larger git repository, so path boundaries must be applied relative to this folder.
