---
stage: "0B — Provisional Operating Contract & Engineering Boundaries"
title: "Repository Write Boundaries (Proposal)"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Provisional"
evidence_sources:
  - "docs/00-preflight/discovery/discovery-summary.md"
  - "docs/_harness/write-boundaries.txt"
  - "docs/00-preflight/discovery/system-landscape.md"
  - "docs/00-preflight/discovery/test-overview.md"
  - "tests/*.py"
  - "backend/app/main.py"
---

# Repository Write Boundaries (Proposal)

**These are proposals.** [Verified Fact] `docs/_harness/write-boundaries.txt` currently holds only comments, so no implementation writes are allowed. A human must transfer approved globs there and record the approver; this stage does not edit that file.

Globs are relative to the repository root `01-bfsi-lending-aml-servicing/`. Every write stage may also write its own `docs/<stage-folder>/**` and the harness-managed `docs/_harness/**`.

## Always protected (no write stage may change)

| Path | Reason |
|---|---|
| `docs/legacy/**` | Inherited evidence; harness-protected |
| `data/*.csv`, `data/manifest.json` | Baseline synthetic dataset; before/after comparison depends on it [Inference] |
| `docs/00-preflight/**` and other stages' `docs/**` | Prior evidence |
| `.claude/commands/**`, `docs/_harness/state.json`, `docs/_harness/history/**` | Harness integrity |
| `CHANGE_REQUEST.md`, `WORKSHOP_SCENARIO.md`, `README.md` | Business/problem statements |
| `.venv/**`, `node_modules/**`, `*.db`, `.env` | Local untracked artefacts and secrets |

## Proposed per-stage write globs

| Stage | Name | Proposed globs | Notes |
|---|---|---|---|
| 15 | Modernization | `backend/app/**`, `adapters/**`, `etl/**`, `tests/**`, `requirements.txt` | Only changes justified by the Stage 14 plan; characterization tests precede change (T3) |
| 19 | Intelligence | `backend/app/intelligence/**`, `tests/intelligence/**` | New directory; only if Stage 8 qualifies AI; no wiring into existing routes without Stage 23 controls |
| 20 | Application | `backend/app/**`, `frontend/src/**`, `frontend/e2e/**`, `tests/**` | `frontend/package.json` changes must be listed explicitly |
| 21 | Integration | `adapters/**`, `backend/app/config.py`, `tests/integration/**` | No real endpoint calls |
| 22 | Agentic engineering | `backend/app/agents/**`, `tests/agents/**` | Requires an approved Stage 23 human-control design first |
| 24 | Security & privacy | `backend/app/security.py`, `backend/app/config.py`, `backend/app/main.py`, `tests/**` | Changes to authN/authZ behaviour must update characterization tests deliberately |
| 26 | TEVV | `tests/**`, `scripts/run_tests.sh`, `pytest.ini`, `pyproject.toml` | Test/evaluation assets only |
| 27 | Hardening | `backend/app/**`, `etl/**`, `tests/**`, `requirements.txt` | |
| 28 | Resilience | `backend/app/**`, `adapters/**`, `etl/**`, `tests/**` | |
| 30 | Release | `scripts/**`, `.github/**`, `Dockerfile*` | New CI/deploy files; no real deploy |
| 31 | Observability | `backend/app/main.py`, `backend/app/audit.py`, `observability/**`, `tests/**` | |

- [Inference] Overlap of `backend/app/**` across stages is intentional; separation comes from stage branches and the `fde(<stage>):` commit convention.
- [Verified Fact] The harness reports changed files outside approved globs as errors in write stages (`fde.py` check, boundary section).

## Approval record (to be completed by a human)

- approved-by: none yet (PROVISIONAL)
- approved-at: none yet

## Assumptions

- [Assumption] The Stage 14 plan may narrow these globs; narrower is acceptable, broader requires new approval.
- [Assumption] Globs matching not-yet-existing directories are acceptable for new files.

## Unresolved Issues

- [Unknown] Whether the frontend may change (depends on Stage 5/7 findings, U-08).
- [Unknown] Whether dependency manifest changes need separate approval; this proposal treats them as listed-only.

## Residual Risks

- `backend/app/**` is wide; a stage could change unrelated modules inside it, mitigated only by diff review.
- With the enforcement file empty, the harness blocks all write stages until a human fills it.
