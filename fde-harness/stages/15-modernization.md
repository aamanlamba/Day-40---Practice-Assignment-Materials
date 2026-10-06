---
id: 15
name: Transform Bad Repo → Good Repo
folder: 15-modernization
mode: write
depends_on: [0B, 7, 14]
approval: true
artifacts:
  - transformation-log.md
  - changed-components.md
  - behavior-preservation-evidence.md
  - approved-behavior-changes.md
  - refactoring-decisions.md
  - dependency-changes.md
  - remaining-technical-debt.md
  - test-execution-log.md
  - modernization-summary.md
---
## Objective

Execute **only the approved transformation** from Stage 14, preserving validated behaviour except where approved specifications intentionally change it.

Use evidence from: Stage 14 backlog and gates, Stage 7 behaviour baseline and characterization plan, Stage 12 specs, Stage 0B boundaries.

## Scope

Improve repository structure, boundaries, dependencies, configuration, tests, maintainability, documentation, security and engineering automation.

## Brownfield Change Protocol (mandatory)

Work through the Stage 14 backlog **one `TX-###` item at a time**:

1. Confirm the item's paths are inside `docs/_harness/write-boundaries.txt`. If not, stop and record it as blocked.
2. **Characterize first**: implement the planned characterization tests for the affected behaviour; run them against the unchanged code; they must pass.
3. Make the smallest change that achieves the item.
4. Run the relevant tests (and the full suite before closing the item). Record command, result and counts in `test-execution-log.md`.
5. Commit with message `fde(15): TX-### <summary>` — one reviewable commit per item (or per logical sub-step). Never mix items.
6. Append to `transformation-log.md`: item, commit SHA, files changed, tests run, behaviour preserved/changed, rollback step.
7. If any behaviour changes, it must be listed in `approved-behavior-changes.md` with the approving spec ID — otherwise revert.

## Constraints / Guardrails

Do not:
- modify implementation outside approved Stage 0B / `write-boundaries.txt` boundaries;
- change behaviour that is not explicitly approved by a spec;
- batch unrelated changes into one commit; rewrite git history;
- delete legacy components without a Stage 14 item that says so;
- upgrade dependencies opportunistically (record each change in `dependency-changes.md`).

Preserve: Stage 7 baseline behaviour for all critical workflows.

## Stage-Specific Completion Gate

- Every completed `TX-###` has a commit, a log entry and passing tests.
- `behavior-preservation-evidence.md` maps each critical workflow to before/after test evidence.
- Incomplete items are listed with reason in `modernization-summary.md`.
- Human approval recorded at completion.

## Lifecycle Linkage

- Executes Stage 14 within 0B boundaries. Validated by Stage 16.
