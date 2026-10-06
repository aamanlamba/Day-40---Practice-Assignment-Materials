---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Evidence Contract"
version: "1.1"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/_harness/README.md"
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/00-preflight/discovery/test-overview.md"
---

# Evidence Contract

## Classification

Every material statement is tagged `[Verified Fact]`, `[Inference]`, `[Assumption]` or `[Unknown]`.

- **Verified Fact**: observed in repo content, command output, a test result or approved stakeholder evidence, with a citation.
- **Inference**: names the facts it rests on.
- **Assumption**: listed in the artifact's Assumptions section.
- **Unknown**: listed with where to investigate; never replaced by invention.

## Rules

1. Stakeholder statements count as evidence only when recorded with who, when and in which document; verbal claims are Assumptions until written down.
2. Command evidence states the command and a summarized result (e.g. 0A: `pytest -q` gave 13 passed).
3. Counts and rates must be recomputable from repository data, with the method documented.
4. Prior-stage evidence is not rewritten. Corrections bump `version` and add a `## Change Log` entry; harness snapshots go to `docs/_harness/history/`.
5. Baselines (Stage 4) are frozen copies; later "after" measurements compare against them.
6. A claim of "complete", "fixed" or "passing" requires a command run in the current stage with its result in the report.
7. Legacy documents are not authoritative (`docs/legacy/release-notes.md:8`, `operations-runbook.txt:6`); their statements are Assumptions until corroborated.
8. Confidence (High/Medium/Low) and unresolved questions accompany each material finding.
9. Artifact headers and the sections `Assumptions`, `Unresolved Issues`, `Residual Risks` are checked by `fde.py check`.

## Evidence ladder (for conflicts)

1. Executed test or command output in the current stage
2. Code and configuration at the base commit
3. Data content
4. Documented, approved stakeholder statement
5. Legacy documentation
6. Undocumented recollection

[Inference] Rests on 0A facts: legacy docs carry stale warnings, and `domain_rules.py` conflicts with recorded data, so higher rungs must override lower ones.

## Assumptions

- [Assumption] This ordering is acceptable; stakeholders may reorder it in Stage 2.

## Unresolved Issues

- [Unknown] Whether regulators or auditors require a specific evidence format (U-09).

## Residual Risks

- Evidence from local agent runs depends on a Python 3.13 environment that may differ from real environments.

## Change Log

- v1.1 (2026-10-06, run 2): Version bump for re-run 2 on a new base commit (b2c1f27, 0A evidence committed); content unchanged. Prior version snapshotted under `docs/_harness/history/0b/`.
