---
id: 7
name: Deep Brownfield Repository Assessment & Behaviour Baseline
folder: 07-repo-assessment
mode: read-only
depends_on: [0A, 5, 6]
approval: false
artifacts:
  - repo-assessment.md
  - architecture-drift.md
  - dependency-map.md
  - technical-debt-register.md
  - legacy-pattern-register.md
  - partial-migration-register.md
  - critical-workflow-inventory.md
  - baseline-test-results.md
  - baseline-behaviour.md
  - characterization-test-plan.md
  - security-code-quality-findings.md
  - maintainability-assessment.md
  - repo-transformation-readiness.md
---
## Objective

Perform the detailed engineering assessment intentionally deferred from Stage 0A and capture a **behaviour baseline** that later transformation must preserve.

Use evidence from: Stage 0A/5/6; the full source tree, tests, configuration, dependencies and git history.

## Scope

Analyse architecture drift, module boundaries, dependencies, duplication, complexity, obsolete libraries, legacy patterns, partial migrations, configuration, data handling, security, testability, observability and maintainability.

## Required Analysis

Evaluate:
1. Architecture drift: intended (docs) vs actual (code).
2. Dependency map (internal modules and external packages with versions).
3. Technical debt, legacy patterns and partial migrations — each with file:line evidence, impact and risk.
4. Critical workflows whose behaviour must be preserved.
5. Baseline test execution: run existing tests **where safe**, record the exact command, environment, pass/fail counts and raw output summary in `baseline-test-results.md`.
6. Baseline behaviour of critical workflows (inputs → outputs, including quirks that may be wrong but are relied upon).
7. Characterization tests needed before refactoring where coverage is insufficient (plan only).

## Constraints / Guardrails

Do not:
- refactor, fix or change intended behaviour during this stage;
- commit test caches, databases or build outputs produced by running tests (run in a way that leaves the tree clean, or delete generated artefacts that are git-ignored only);
- write characterization tests into the repository yet — plan them here; they are implemented in Stage 15.

Only: read, run existing tests/tools read-only, and write under `docs/07-repo-assessment/`.

Preserve: all current behaviour, including suspected defects (record them as findings).

## Stage-Specific Completion Gate

- `baseline-test-results.md` records a real test run (command + counts) or a documented reason tests could not be run safely.
- Every critical workflow in `critical-workflow-inventory.md` has baseline behaviour and either existing test coverage or a characterization test planned.
- `repo-transformation-readiness.md` states whether transformation can safely start.

## Lifecycle Linkage

- Deepens Stage 0A. The behaviour baseline is compared in Stage 16; characterization tests are implemented in Stage 15.
