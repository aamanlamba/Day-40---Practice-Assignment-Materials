---
id: 31
name: Observability + SLO/SLA Engineering
folder: 31-observability
mode: write
depends_on: [30]
approval: false
artifacts:
  - observability-architecture.md
  - logging-spec.md
  - metrics-spec.md
  - tracing-spec.md
  - ai-telemetry-spec.md
  - agent-telemetry-spec.md
  - dashboard-catalog.md
  - alert-catalog.md
  - slo-sla-definitions.md
  - error-budget-policy.md
  - operational-runbook.md
  - observability-validation.md
---
## Objective

Instrument application, infrastructure, data, RAG, models and agents where applicable, and define SLOs/SLAs.

Use evidence from: Stage 12 observability spec, Stage 30 release.

## Scope

Privacy-safe logs, metrics and traces for requests, retrieval, prompt/config versions, model latency, tokens, tool calls, agent trajectories, errors and business outcomes. SLOs, SLAs, alerts and error budgets.

## Brownfield Change Protocol

Instrumentation code follows the Stage 15 protocol (`fde(31): <summary>`).

## Constraints / Guardrails

Do not: log PII or secrets; create AI/agent telemetry for capabilities Stage 8 rejected (mark Not Applicable).

## Stage-Specific Completion Gate

- `observability-validation.md` shows that each SLO has a working signal.

## Lifecycle Linkage

- Feeds Stages 32, 34, 39.
