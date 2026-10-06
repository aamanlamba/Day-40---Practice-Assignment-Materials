---
id: 16
name: Validate the Good Repo
folder: 16-repo-validation
mode: read-only
depends_on: [7, 10, 12, 15]
approval: false
artifacts:
  - repo-quality-gate.md
  - regression-results.md
  - architecture-conformance-report.md
  - test-results.md
  - security-scan-summary.md
  - dependency-scan-summary.md
  - data-contract-results.md
  - behavior-difference-report.md
  - remaining-debt-register.md
  - validation-signoff.md
---
## Objective

Validate the transformed repository against target architecture, specifications and engineering standards, and explain every behavioural difference from the Stage 7 baseline.

Use evidence from: Stage 7 baseline, Stage 10 architecture, Stage 12 specs, Stage 15 logs.

## Scope

Run unit, integration, contract, characterization, security and data-contract tests plus relevant static, dependency and architecture checks available locally.

## Required Analysis

Evaluate:
1. Test results (command, environment, counts, failures) vs Stage 7 baseline.
2. Architecture conformance vs Stage 10.
3. Security and dependency scan results (record tool + version; if a tool is unavailable, say so — do not fabricate results).
4. Data-contract results.
5. Behaviour differences: each one classified as Approved change (spec ID) / Defect / Unexplained.

## Constraints / Guardrails

Do not: fix code in this stage (record defects; fixes go back through Stage 15); suppress failing tests.

## Stage-Specific Completion Gate

- `behavior-difference-report.md` has zero Unexplained differences for PASS.
- `repo-quality-gate.md` states PASS/FAIL per gate criterion with evidence.

## Lifecycle Linkage

- Compares Stage 7 with Stage 15 output. Feeds Stage 17.
