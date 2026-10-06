---
stage: "1 — Engage & Qualify"
title: "Use Case Hypothesis"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "data/alerts.csv"
  - "data/baseline_metrics.csv"
  - "docs/00-preflight/discovery/workflow-overview.md"
  - "docs/00-preflight/ai-economics/solution-scenarios.md"
---

# Use Case Hypothesis

Hypotheses only. Nothing here selects a solution, a model or a vendor, and AI is not assumed to be required (Stage 8 decides).

## Hypotheses (to be tested)

| ID | Hypothesis | Rests on | Status |
|---|---|---|---|
| H-1 | Analysts spend material time on alert triage that a better-prioritised, evidence-linked view could reduce | [Claim] `CHANGE_REQUEST.md:3`; [Verified Fact] 923 of 1,800 alerts are OPEN/ESCALATED and 901 are CRITICAL/HIGH, so many alerts look urgent | Untested; baseline does not say which workflow the manual hours belong to |
| H-2 | Routing today is inconsistent and could be explained better | [Verified Fact] alert `source` includes `rules-v1`, `rules-v2`, `ml-legacy`, `manual`; 104 alerts have no owner; `aml_priority()` exists but is unused | Untested |
| H-3 | Servicing exceptions arise partly from data mismatches | [Verified Fact] 218 of 5,000 repayments reference a different customer than their application; ETL drops rows with any blank | Untested; causality unknown |
| H-4 | A deterministic or conventional approach may meet the need without AI | 0C S1/S2 scenarios; existing rule vocabulary (score, PEP flag) | Untested |
| H-5 | If AI helps, it helps with summarising evidence and explaining routing, not deciding | [Claim] `CHANGE_REQUEST.md:3` ("explain routing", "support analyst review") | Untested; contingent on Stage 8 |

## Candidate outcome measures (not targets)

- Analyst time per alert, share of alerts closed as FALSE_POSITIVE (429 of 1,800 today, [Verified Fact]), time to first review, exception rate (7.29% mean, [Verified Fact]), error rate (4.80% mean).

## Preconditions before any hypothesis can be tested

- Definition of work item and cost unit (Q-023, Q-024); a baseline for the specific workflow (Stage 4).
- The authoritative rules for approval and AML priority (Q-002).
- Human-control design for any surfaced recommendation (Stage 23; 0B terms T5, T6).

## Assumptions

- [Assumption] Alerts are the primary triage artefact; the change request does not say so explicitly.

## Unresolved Issues

- [Unknown] Whether triage time is the bottleneck, and which volume of work is triage (Q-023, Q-025).

## Residual Risks

- Hypotheses may be read as commitments; they are testable guesses.
