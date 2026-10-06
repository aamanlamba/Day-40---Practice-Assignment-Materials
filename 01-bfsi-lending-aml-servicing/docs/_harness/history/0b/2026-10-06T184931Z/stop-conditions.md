---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Stop Conditions"
version: "1.0"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/initial-risk-register.md"
  - "docs/_harness/write-boundaries.txt"
  - "backend/app/config.py"
  - "docs/00-preflight/discovery/data-flow-overview.md"
---

# Stop Conditions

Work stops and is escalated to the human engagement lead when any condition below is true. Each has a test the agent can apply.

| ID | Condition | How to test | Source |
|---|---|---|---|
| S-01 | `fde.py check` reports a `boundary:` error | Run the check | harness |
| S-02 | A write is needed outside approved globs, or `write-boundaries.txt` has no globs when a write stage is requested | `grep -v '^#' docs/_harness/write-boundaries.txt` shows no globs ([Verified Fact] true today) | harness |
| S-03 | The 0A baseline fails (`python -m pytest -q` not 13 passed) without an approved intended change | Run tests | 0A |
| S-04 | Data appears real (valid government IDs, real card numbers, a real company domain, public figures' names) | Pattern scan of `customers.csv`/`beneficiaries.csv` before first use; any hit | `README.md:50` |
| S-05 | A credential or secret other than the known default is found in repo, logs or tool output | Secret grep | `config.py:7` |
| S-06 | A step would contact a non-local host, real partner or legacy endpoint | Inspect command/URL | `environment-access-boundaries.md` |
| S-07 | A change would alter an approval, payment or AML disposition outcome without H4/H6 approval | Diff touches `domain_rules.py`, decision flows or ETL drop logic without an approval record | `CHANGE_REQUEST.md:3` |
| S-08 | AI/agent behaviour is about to be introduced before Stage 8 qualification | New model call, or any code path reading `ENABLE_EXPERIMENTAL_SCORING` | `README.md:51` |
| S-09 | A required prior stage is not PASS, or its report is BLOCKED | `fde.py status` | harness |
| S-10 | An evidence conflict that changes a conclusion cannot be settled by the evidence ladder | Two sources contradict, neither outranks | `evidence-contract.md` |
| S-11 | An action needs an approver whose role is unassigned (e.g. AI-model owner) | Role blank in `contact-matrix.csv` | `contact-matrix.csv:6` |
| S-12 | Unexplained tracked changes outside the stage | `git status --short` | harness |
| S-13 | A command would delete or overwrite prior evidence, `data/**` or `docs/legacy/**` | Inspect command | `repository-write-boundaries.md` |
| S-14 | A tool run would send customer-style records to an external service | Inspect tool/destination | `data-use-constraints.md` |
| S-15 | The stage report cannot honestly be PASS because required evidence is missing | Gate check and self-review | execution contract |

## Escalation

[Assumption] Escalation path: agent to the human engagement lead (PROVISIONAL). Organisational escalation (security-team, ciso-delegate, product-owner) is unconfirmed until Stage 2.

## Assumptions

- [Assumption] Concrete patterns for S-04 and S-05 are defined when first used and recorded in that stage's evidence.

## Unresolved Issues

- [Unknown] Additional regulatory stop conditions (U-09).
- [Unknown] Time-based stop conditions pending Stage 0C.

## Residual Risks

- S-04 and S-14 involve judgment and cannot be fully automated.
