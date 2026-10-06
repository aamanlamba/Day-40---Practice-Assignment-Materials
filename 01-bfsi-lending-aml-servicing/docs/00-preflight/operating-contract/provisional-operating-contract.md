---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Provisional Operating Contract"
version: "1.1"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
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
- [Unknown] Who the engagement sponsor is and who approves this contract beyond the human who runs `fde.py complete 0B --approved-by`. Roles below use assumed personas (P1-P10) that are PROVISIONAL placeholders.


## Assumed personas (v1.1, PROVISIONAL)

Typical roles for a lending/AML engagement, **assumed** so approval rules have a concrete shape. [Assumption] None is evidenced by the repository; `docs/legacy/contact-matrix.csv` supplies only team aliases (mapped in the last column). Each persona must be replaced by a named person in Stage 2.

| ID | Persona (assumed typical role) | Typical decision rights (assumed) | Closest evidence |
|---|---|---|---|
| P1 | Executive Sponsor (e.g. Head of Digital Lending) | Funds and scopes the engagement; accepts residual risk; names owners | none |
| P2 | Engagement Lead / FDE Lead | Approves stage completion (H1), dependency changes, commit/push; escalation point | harness user |
| P3 | Product Owner, Lending | Underwriting and servicing rule changes (H4) | `application` row: product-owner |
| P4 | MLRO / Head of AML Compliance | AML-priority rules, alert disposition, regulatory interpretation (H4, H6) | none; no AML owner listed |
| P5 | Security Architect / CISO delegate | AuthN/authZ changes, secrets, tool approvals (H3, H8) | `security` row: security-team, ciso-delegate |
| P6 | Data Owner / Head of Data Operations | Data use, classification, real-data decisions (H10) | `data` row: data-ops, authority "unknown" |
| P7 | Operations Lead / Head of Loan Servicing Ops | Runbook, release windows, cutover (H9) | `operations` row: ops-lead, business-ops |
| P8 | Platform / Application Engineering Lead | Code ownership, merge review, API consumers | `application` row: app-team |
| P9 | Model Risk Manager (AI-model owner) | Any AI/agent capability (H5, H6) | `ai-model` row: blank, "not-established" |
| P10 | Data Protection Officer / Privacy | Privacy impact, PII handling | none |

Principle: an assumed persona never grants authority. Until a named person confirms the role, the approval falls back to P2 as stated in `provisional-human-approval-rules.md`, and each use is logged in the open question log (`docs/_harness/open-questions.md`).

## Assumptions

- [Assumption] The human executing the harness acts as interim approving authority for stage completion; this is not evidence of organisational decision rights.
- [Assumption] The contract applies to this repository folder only (A-01).

## Unresolved Issues

- [Unknown] Sponsor, approver of the final contract, data owner, AI-model owner (U-01).
- [Unknown] Compliance obligations that may add terms (U-09).

## Residual Risks

- Terms rest on workshop documents rather than a signed engagement agreement; their authority is unverified.
- The repo is nested in a larger git repository, so path boundaries must be applied relative to this folder.

## Change Log

- v1.1 (2026-10-06, run 2): Added assumed personas P1-P10 (typical lending/AML roles) to give approval rules a concrete shape; marked PROVISIONAL. No scope or terms changed. Prior version snapshotted under `docs/_harness/history/0b/`.
