---
id: 10
name: Target Architecture + ADRs
folder: 10-architecture
mode: read-only
depends_on: [7, 8, 9]
approval: false
artifacts:
  - architecture-options.md
  - target-architecture.md
  - component-model.md
  - integration-architecture.md
  - deployment-architecture.md
  - security-architecture.md
  - model-service-scorecard.md
  - architecture-risk-register.md
  - architecture-decision-summary.md
globs:
  - "adrs/ADR-*.md :: 1"
---
## Objective

Develop and compare architecture options and select a target architecture, recording each material decision as an ADR.

Use evidence from: Stage 7 assessment, Stage 8 decision and Stage 9 PRD.

## Scope

Options across application, frontend/backend, APIs, AI/model, data, knowledge, integration, security, identity, observability, human control and deployment.

## Required Analysis

Evaluate options against functional requirements, NFRs, security, portability, cost, latency, scalability, resilience and maintainability. Score candidate models/services in `model-service-scorecard.md` (or record "Not applicable — Stage 8 rejected AI" with justification).

## Constraints / Guardrails

Do not: design for AI capabilities rejected in Stage 8; ignore brownfield constraints from Stage 7.

ADRs go in `docs/10-architecture/adrs/` named `ADR-001-<slug>.md`, `ADR-002-<slug>.md`, ... — **one ADR per material decision**, each with Context, Options, Decision, Consequences, Status, and the standard artifact header.

## Stage-Specific Completion Gate

- At least one ADR exists and every material decision in `architecture-decision-summary.md` links to an ADR.
- Options are compared against the same criteria.

## Lifecycle Linkage

- Uses Stages 7–9. Feeds Stages 11, 12, 14 and FINAL (as-built architecture).
