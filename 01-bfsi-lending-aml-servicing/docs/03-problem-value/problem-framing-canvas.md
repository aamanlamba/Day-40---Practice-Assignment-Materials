---
stage: "3 — Frame Problem & Value"
title: "Problem Framing Canvas"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "data/baseline_metrics.csv"
  - "data/alerts.csv"
  - "data/repayments.csv"
  - "data/applications.csv"
  - "docs/01-engagement/engagement-go-no-go.md"
  - "docs/02-stakeholders/stakeholder-conflicts.md"
  - "docs/00-preflight/discovery/discovery-summary.md"
---

# Problem Framing Canvas

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

The four layers are kept apart so a proposed solution is not mistaken for the problem.

| Layer | Content | Status |
|---|---|---|
| **Symptom** | Analysts and operations staff spend a lot of manual effort on fraud/AML alert review and loan-servicing exceptions. Measured: 8,273.5 manual hours over 180 days (about 3.89 minutes per work item), 7.29% mean exception rate, 4.80% mean error rate, 81.5 min mean cycle time (`data/baseline_metrics.csv`). 429 of 1,800 alerts (23.8%) end as FALSE_POSITIVE; 923 are OPEN or ESCALATED, of which 54 have no owner (`data/alerts.csv`) | [Verified Fact] figures; the link between these hours and the alert workflow is [Unknown] (Q-023) |
| **Root problem (hypothesised)** | Staff cannot quickly tell which cases need attention first, or why, because the information for a decision is scattered across separate records, rules disagree and ownership is incomplete. Evidence: alert `source` mixes four generations (`manual`, `ml-legacy`, `rules-v1`, `rules-v2`) with similar false-positive shares (22.7%-25.0%); 104 alerts have no owner; 218 of 5,000 repayments disagree with their application on the customer; 211 applications lack a decision source; recorded outcomes do not follow the documented approval rule (0A R-05) | [Inference]; causal link untested |
| **Proposed solution (stakeholder)** | "Surface high-risk cases with evidence, explain routing, support analyst review", avoiding autonomous financial decisions (`CHANGE_REQUEST.md:3`) | [Claim]; "not an approved solution design" (`CHANGE_REQUEST.md:7`). Treated as a candidate, not a requirement |
| **Assumed AI need** | The request does not mention AI; the workshop frames AI as something to be qualified (`README.md:51`). Any AI need is therefore **not established** | [Verified Fact] no stakeholder asks for AI; decided in Stage 8 |

## Problem in one line (technology-neutral version is in `problem-statement.md`)

Reviewers of financial-crime alerts and servicing exceptions spend more time than the business wants on cases of mixed urgency, and the organisation cannot show why a case was prioritised the way it was.

## What is not yet known

- The size of the share of manual effort that is alert triage vs other work (Q-023).
- Whether false positives or missed cases is the larger cost (no miss data exists).
- The business target and deadline (Q-011).

## Assumptions

- [Assumption] The manual-effort baseline covers the workflows named in the change request.
- [Assumption] Review time rises with poor prioritisation and fragmented information.

## Unresolved Issues

- [Unknown] Whether the root problem hypothesis is right; interview analysts and the compliance owner (GG-02) to test it.

## Residual Risks

- Fixing a mis-identified root problem delivers no value; the hypothesis must be tested in Stage 4/5.
