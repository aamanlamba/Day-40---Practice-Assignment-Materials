---
id: 39
name: Drift + Continuous Improvement
folder: 39-continuous-improvement
mode: read-only
depends_on: [31, 38]
approval: false
artifacts:
  - drift-framework.md
  - data-drift-metrics.md
  - knowledge-drift-metrics.md
  - retrieval-drift-metrics.md
  - prompt-model-drift-metrics.md
  - agent-drift-metrics.md
  - evaluation-cadence.md
  - change-trigger-thresholds.md
  - continuous-evaluation-plan.md
  - controlled-change-process.md
  - improvement-backlog.md
---
## Objective

Define continuous evaluation and thresholds that trigger investigation or controlled change.

## Scope

Data, knowledge, retrieval, prompts, models, agents, application quality, adoption, reliability, latency, tokens/cost and changing requirements — as applicable (mark AI-specific metrics Not Applicable where Stage 8 rejected AI).

## Constraints / Guardrails

Do not: permit untracked prompt/model changes in production — `controlled-change-process.md` must require versioning and evaluation for every such change.

## Stage-Specific Completion Gate

- Every drift metric has a threshold and an owner (or open item).

## Lifecycle Linkage

- Feeds Stage 40.
