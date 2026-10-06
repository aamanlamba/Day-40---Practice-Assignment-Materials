---
stage: "3 — Frame Problem & Value"
title: "Problem Statement"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "CHANGE_REQUEST.md"
  - "data/baseline_metrics.csv"
  - "data/alerts.csv"
  - "docs/legacy/business-rules.txt"
  - "docs/legacy/operations-runbook.txt"
---

# Problem Statement

**Technology-neutral.** This statement describes the situation and outcome sought without naming any solution technique.

## Situation

A lender that also handles anti-money-laundering and fraud review must decide each day which suspicious-activity alerts, know-your-customer cases and loan-servicing exceptions to examine first, and must record why. [Verified Fact] Recorded data shows 1,800 alerts of four types and four severities, 923 of them open or escalated; and a daily workload of about 709 work items consuming about 46 manual hours a day (`data/baseline_metrics.csv`, `data/alerts.csv`).

## Problem

1. **Time.** Reviewers spend about 3.9 minutes of manual effort per work item and 81.5 minutes of elapsed time per item on average, with 7.3% of items becoming exceptions and 4.8% containing errors ([Verified Fact], `data/baseline_metrics.csv`).
2. **Priority.** Nearly a quarter (23.8%) of alerts are closed as not suspicious, and the share is similar whichever mechanism raised them (22.7% to 25.0%), so current prioritisation does not visibly separate real cases from false ones ([Verified Fact], `data/alerts.csv`).
3. **Explanation.** The organisation cannot show, from the records it holds, why a given case was ranked or routed as it was; the existing rule definitions do not match recorded outcomes ([Verified Fact], 0A R-05).
4. **Ownership and consistency.** Some cases have no responsible reviewer (54 of 923 open or escalated alerts), and related records disagree (218 repayments name a different customer from their loan application) ([Verified Fact]).

## Outcome sought

Reviewers can see, for each case, how urgent it is and the evidence and reasons behind that, so that effort goes to the cases that need it, while all existing lending and payment results stay unchanged and every consequential decision stays with an accountable person.

## Boundaries

Existing lending and payment behaviour is preserved; no financial decision is made without a human decision-maker unless explicitly approved (`CHANGE_REQUEST.md:3`).

## Not claimed

- That any particular means, or any particular degree of change, is required.
- That the figures above are caused by poor prioritisation; that is a hypothesis to test.

## Assumptions

- [Assumption] Work items in the baseline include alert and exception review (Q-023).
- [Assumption] A false-positive share near 24% is higher than the business wants; no target exists.

## Unresolved Issues

- [Unknown] The business tolerance for false positives and the cost of misses (Q-011, Stage 4).

## Residual Risks

- A neutral statement may still be read as implying a particular approach; solution choice belongs to later stages.
