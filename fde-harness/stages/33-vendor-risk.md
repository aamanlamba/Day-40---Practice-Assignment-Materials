---
id: 33
name: Vendor / Third-Party / Concentration Risk
folder: 33-vendor-risk
mode: read-only
depends_on: [10, 32]
approval: false
artifacts:
  - vendor-inventory.md
  - vendor-scorecards.md
  - third-party-risk-assessment.md
  - data-processing-dependencies.md
  - concentration-risk-analysis.md
  - lock-in-analysis.md
  - portability-assessment.md
  - substitution-strategy.md
  - exit-plan.md
  - vendor-risk-acceptance.md
---
## Objective

Assess critical model, platform, infrastructure, data and service providers.

Use evidence from: Stage 10 architecture, dependency manifests, Stage 32 economics.

## Scope

Availability, contractual terms, security/privacy, data usage, regulatory constraints, price risk, portability, concentration, lock-in, substitution and exit feasibility.

## Constraints / Guardrails

Do not: state contract terms you have not seen — mark Unknown.

## Stage-Specific Completion Gate

- Every critical vendor has a scorecard and an exit/substitution position.

## Lifecycle Linkage

- Feeds Stages 37, 41.
