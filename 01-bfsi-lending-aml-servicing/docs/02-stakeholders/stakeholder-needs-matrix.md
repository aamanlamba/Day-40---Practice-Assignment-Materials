---
stage: "2 — Stakeholder Discovery & Authority Confirmation"
title: "Stakeholder Needs Matrix"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/02-stakeholders/stakeholder-map.md"
  - "CHANGE_REQUEST.md"
  - "docs/legacy/contact-matrix.csv"
  - "docs/legacy/business-rules.txt"
  - "docs/legacy/release-notes.md"
  - "docs/legacy/operations-runbook.txt"
---

# Stakeholder Needs Matrix

**Important:** no stakeholder interview, statement or sign-off exists in the repository or this session. Stakeholders below are classified **Evidenced** (named as an alias in a repository document or visible in data), **Implied** (a role the system or domain needs but no document names) or **Missing** (expected for this domain, not evidenced). Needs, incentives and concerns are [Inference] from the domain and repository, not stakeholder-validated. No person is named; unassigned ownership is a **governance gap (GG)**, not a placeholder name. Personas P1-P10 (0B) are working labels only.

All cells are [Inference] from the change request, domain norms and legacy notes unless a [Verified Fact] is cited. They are hypotheses to put to each stakeholder.

| Stakeholder | Likely needs | Likely incentives | Likely concerns | Supporting evidence |
|---|---|---|---|---|
| S1 Sponsor | Lower cost, fewer exceptions, controlled risk | Visible savings, regulator comfort | Cost overrun, reputational and regulatory exposure | `CHANGE_REQUEST.md:3` ([Verified Fact] that the request asks for reduced manual triage) |
| S2 Product owner | Preserve lending behaviour and throughput | Approval volume, turnaround | Any change altering approvals | "preserving existing lending and payment behavior" ([Verified Fact]) |
| S3 MLRO / compliance | Defensible alert disposition, audit trail | Avoid missed suspicious activity and regulatory findings | Autonomous decisions, unexplained scoring, false negatives | `CHANGE_REQUEST.md:3` (explain routing, avoid autonomy); `audit()` unused (0A) |
| S4 Operations | Reliable batches before 08:00, stable CSV exports, clear release steps | Fewer morning exceptions | Cutover risk, rollback gaps | `business-rules.txt:4`, `release-notes.md:3-6` ([Verified Fact] documented practices) |
| S5 Analysts | Prioritised queue, evidence in one place, less rework | Time saved, fewer false positives (429 of 1,800 alerts are FALSE_POSITIVE) | Opaque scores, extra steps, being second-guessed | `alerts.csv` status counts ([Verified Fact]) |
| S6 Underwriters | Consistent rules, clear decision source | Fewer overrides | Model/rule conflicts (MODEL_V1, MODEL_V2, RULE, MANUAL coexist) | `applications.csv` ([Verified Fact]) |
| S8-S9 Engineering | A safe-to-change codebase, tests, CI | Lower maintenance, fewer incidents | Thin tests, dormant code, unclear consumers | 0A R-08, R-12 |
| S10 Data operations | Stable extracts, clear definitions | Data quality | Blank handling, 218 repayment-customer mismatches | 0A R-06, `business-rules.txt:5` |
| S11 Security | Real authentication, role-based access, auditability | Reduced exposure | Client-asserted `X-User`, name-based admin, bulk PII | 0A R-01, R-04 ([Verified Fact]) |
| S12 Privacy | Minimised PII, lawful use | Compliance | Unmasked PII in API responses and potential prompts | `main.py:49-72`, 0B data constraints |
| S13 Model risk | Evidence before any AI; validation, monitoring | Control | AI introduced without justification | `README.md:51`, `ai-model` row blank |
| S15-S16 External systems | Stable contracts, idempotency | Avoid breaking changes | Retries without idempotency keys | `operations-runbook.txt:4` |
| S17 Regulators / auditors | Records, explainability | Compliance | Gaps in evidence | None evidenced |
| S18 Customers | Fair, timely decisions; privacy | n/a | Wrong declines/holds, data exposure | Domain norm |

## Cross-cutting need

- [Inference] Every group wants explainability and unchanged core behaviour; the divergent needs are in cost and speed vs control (see `stakeholder-conflicts.md`).

## Assumptions

- [Assumption] Domain-typical incentives apply to this organisation.

## Unresolved Issues

- [Unknown] Actual needs and priorities; no interviews held. Resolve by structured Stage 2 interviews using this matrix as a script.

## Residual Risks

- Needs written without stakeholder input can embed the author's bias.
