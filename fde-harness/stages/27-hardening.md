---
id: 27
name: Production Hardening
folder: 27-hardening
mode: write
depends_on: [24, 26]
approval: false
artifacts:
  - hardening-plan.md
  - identity-rbac-hardening.md
  - secrets-hardening.md
  - runtime-hardening.md
  - dependency-hardening.md
  - supply-chain-controls.md
  - sbom-summary.md
  - vulnerability-register.md
  - scan-results.md
  - vulnerability-disposition.md
  - production-readiness-checklist.md
---
## Objective

Harden identity, RBAC, secrets, network/runtime, infrastructure, dependencies, APIs, CI/CD, build artifacts and software supply chain.

Use evidence from: Stages 24, 26.

## Scope

Generate/review SBOMs; scan source, dependencies, infrastructure and artifacts; remove debug behaviour, test secrets, unnecessary ports, excessive privileges and insecure defaults.

## Brownfield Change Protocol

Same as Stage 15 (`fde(27): <summary>`); re-run the full test suite after each hardening change.

## Constraints / Guardrails

Do not: fabricate scan output — if a scanner is unavailable, record it; disable tests to make hardening pass.

## Stage-Specific Completion Gate

- Every vulnerability has a disposition (Fixed / Mitigated / Accepted with approver / False positive).

## Lifecycle Linkage

- Feeds Stages 28, 30.
