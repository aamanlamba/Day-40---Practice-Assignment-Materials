---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Provisional Tool and Agent Permissions"
version: "1.1"
date: "2026-10-06"
author: "Aaman Lamba / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/_harness/README.md"
  - "docs/_harness/write-boundaries.txt"
  - "README.md:51"
  - "CHANGE_REQUEST.md:3"
  - "backend/app/experimental_ai.py"
---

# Provisional Tool and Agent Permissions

## Permission matrix for the engagement agent (Claude Code), PROVISIONAL

| Capability | Read-only stages | Write stages (15, 19-22, 24, 26-28, 30, 31) |
|---|---|---|
| Read repo files and git history | Allowed | Allowed |
| Write own stage `docs/<folder>/**` and `docs/_harness/reports/**` | Allowed | Allowed |
| Run existing tests/self-check | Allowed if no tracked changes result | Allowed |
| Run ETL scripts (stdout only) | Allowed | Allowed |
| Run `bootstrap_sqlite.py`, `npm install`, builds | Not allowed (writes) | Allowed within approved globs and gitignored dirs |
| Edit code/config/tests | **Prohibited** | Only inside human-approved globs in `write-boundaries.txt` |
| Modify `data/**`, `docs/legacy/**` | Prohibited | Prohibited |
| Start local servers | Loopback, short-lived | Loopback |
| Install dependencies | Prohibited | Allowed with a listed manifest change |
| Network beyond localhost | Prohibited except documentation/package lookups | Same, plus approved registries |
| Git commit | Only if the human asks | `fde(<stage>): ...` on the stage branch; no push unless asked |
| `fde.py complete` and approvals | **Human only** | **Human only** |
| Edit `docs/_harness/write-boundaries.txt` | Human only | Human only |

## Autonomy limits

- [Verified Fact] No AI/agent autonomy before Stage 8 qualification (`README.md:51`). The only AI-like code, `experimental_ai.suggest()`, is a keyword heuristic that nothing calls (0A component C10); `ENABLE_EXPERIMENTAL_SCORING` defaults `true` but is unread (`config.py:8`). Neither may be wired in.
- The agent takes no financial decision, changes no customer outcome and touches no real system (T6).
- Sub-agents inherit these limits; none gets broader permissions than the parent.
- Third-party skills and connectors (browser, scraping, mail, calendar, drive) are not used on this engagement without explicit human instruction, because they send data outside the repo.
- [Unknown] The tool provider's data-handling terms for prompts.

## Assumptions

- [Assumption] The human runs the harness commands and reviews diffs before any push.

## Unresolved Issues

- [Unknown] Organisational AI policy and the AI-model owner ("not-established", `contact-matrix.csv:6`), for Stages 2 and 25.
- [Unknown] Whether Stages 19 and 22 will run at all (depends on Stage 8).

## Residual Risks

- Permissive tool modes in the agent runtime can exceed this matrix; only the harness write-boundary check enforces it technically.

## Change Log

- v1.1 (2026-10-06, run 2): Version bump for re-run 2 on a new base commit (b2c1f27, 0A evidence committed); content unchanged. Prior version snapshotted under `docs/_harness/history/0b/`.
