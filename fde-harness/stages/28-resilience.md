---
id: 28
name: Reliability & Resilience Engineering
folder: 28-resilience
mode: write
depends_on: [21, 27]
approval: false
artifacts:
  - resilience-architecture.md
  - failure-mode-analysis.md
  - timeout-retry-policy.md
  - circuit-breaker-policy.md
  - fallback-matrix.md
  - capacity-plan.md
  - graceful-degradation-design.md
  - ai-disabled-mode.md
  - failure-injection-plan.md
  - failure-injection-results.md
  - resilience-readiness.md
---
## Objective

Design and test realistic failures.

Use evidence from: Stages 21, 27.

## Scope

Timeouts, retries, backoff, circuit breakers, bulkheads, fallback models/providers, caching, capacity limits, graceful degradation and AI-disabled operation. Prevent retry storms and cascading agent/tool failure.

## Brownfield Change Protocol

Same as Stage 15 (`fde(28): <summary>`). Failure injection runs locally only.

## Constraints / Guardrails

Do not: inject failures into shared or production environments.

## Stage-Specific Completion Gate

- Each failure mode has a test or injection result, or a documented reason it was not tested.

## Lifecycle Linkage

- Feeds Stages 29, 30.
