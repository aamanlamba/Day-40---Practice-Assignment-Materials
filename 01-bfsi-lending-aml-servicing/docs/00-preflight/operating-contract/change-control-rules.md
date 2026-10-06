---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Change Control Rules"
version: "1.1"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/_harness/README.md"
  - "docs/_harness/write-boundaries.txt"
  - "docs/legacy/release-notes.md"
  - "docs/00-preflight/discovery/test-overview.md"
  - "git log"
---

# Change Control Rules

## Rules (PROVISIONAL)

1. **Stage branches and commits.** [Verified Fact] The harness expects write-stage commits to follow `fde(<stage>): ...` and warns otherwise (`fde.py` check). Write stages use a branch off the base commit recorded in `docs/_harness/state.json`.
2. **Boundaries.** A change outside approved globs is a stop condition (S-02), not a warning.
3. **Characterize before change (T3).** Before altering behaviour, a passing test records the current behaviour; the altering commit changes that test deliberately and says why. [Verified Fact] Existing example: `tests/test_security_characterization.py`.
4. **Baseline preservation.** The 13-test baseline from 0A must still pass after each write stage, or each failure is explained as an approved intended change (H3/H4).
5. **Small commits** per concern; refactors and behaviour changes are not mixed.
6. **Dependencies.** Manifest changes are listed in the stage report with reasons; no multi-package upgrades in one step.
7. **Data.** `data/**` is frozen; derived data lives under stage folders.
8. **Rollback.** Each write stage records how to revert its commit range. [Verified Fact] Legacy rollback instructions are inconsistent (`release-notes.md:5`), so they are not relied on.
9. **Reporting.** Stage reports list files changed, tests run, results and deviations.
10. **Re-runs** bump artifact versions and add a Change Log entry.
11. **No force operations**: no force-push, history rewrite or deletion of harness history without explicit human instruction.

## Change classes

| Class | Examples | Approval |
|---|---|---|
| Documentation only | Stage artifacts | Stage completion |
| Test-only | New characterization tests | Engagement lead |
| Behaviour-preserving code change | Refactor under tests | Engagement lead |
| Behaviour-changing | authZ, rules, ETL drop logic | H3/H4 in `provisional-human-approval-rules.md` |
| Interface/schema | API shape, SQL schema | Engagement lead plus consumers (unknown, U-13) |

## Assumptions

- [Assumption] The git repository and its parent stay available for branch operations.

## Unresolved Issues

- [Unknown] The real organisation's change-management process (manual maintenance windows are mentioned in `release-notes.md:3`).
- [Unknown] Required reviewers.

## Residual Risks

- No CI exists, so rule 4 depends on manual runs until a later stage adds automation.

## Change Log

- v1.1 (2026-10-06, run 2): Version bump for re-run 2 on a new base commit (b2c1f27, 0A evidence committed); content unchanged. Prior version snapshotted under `docs/_harness/history/0b/`.
