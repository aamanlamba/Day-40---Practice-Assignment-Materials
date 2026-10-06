---
id: 0C
name: Provisional Token Efficiency & AI Economics Envelope
folder: 00-preflight/ai-economics
mode: read-only
depends_on: [0A, 0B]
approval: false
artifacts:
  - workload-assumptions.md
  - solution-scenarios.md
  - provisional-model-call-inventory.md
  - token-flow-scenarios.md
  - provisional-token-budget.md
  - provisional-context-budget.md
  - provisional-loop-budget.md
  - volume-assumptions.md
  - cost-scenarios.md
  - quality-latency-cost-envelope.md
  - preliminary-finops-baseline.md
  - preliminary-tco.md
  - economics-readiness.md
---
## Objective

Establish a provisional economic and resource envelope **without assuming that AI has already been justified**, producing design constraints (cost, latency, context, loop limits) that later stages must respect or explicitly revise.

Use evidence from:
- Stage 0A discovery (workloads, data volumes, workflows) and Stage 0B constraints;
- data volumes, logs, metrics or batch schedules present in the repository.

## Scope

Create scenarios for:
- deterministic software;
- conventional automation;
- GenAI;
- agentic AI (where relevant).

For each, estimate where evidence allows: workload volume, context size, model calls, input/output/retrieval/tool tokens, agent-loop overhead, retries, latency and infrastructure consumption.

Exclude: selecting a solution, selecting a model/vendor, or claiming AI is required.

## Required Analysis

Evaluate:
1. Workload volume and shape (per request, per case, per batch).
2. Token-flow and context-size scenarios per solution type.
3. Agent-loop and retry overhead scenarios.
4. Cost scenarios (low / expected / high) with explicit unit-price assumptions.
5. Maximum acceptable cost/request, cost/case, latency, context size and agent-loop limits as **provisional design constraints**.
6. Preliminary FinOps baseline and TCO including non-AI costs and human effort.

## Constraints / Guardrails

Do not:
- present estimates as measurements — clearly separate measured data from assumptions;
- assume AI is justified; deterministic and conventional scenarios must be costed with the same rigour;
- quote vendor prices without date and source, or mark them Assumption.

Only: estimate where enough evidence exists; otherwise record Unknown.

Preserve: the repository exactly as found.

## Stage-Specific Completion Gate

- Every numeric figure is tagged Measured / Estimated / Assumption with source.
- `quality-latency-cost-envelope.md` states provisional maximums as design constraints.
- `economics-readiness.md` states which AI-specific portions are contingent on Stage 8.

## Lifecycle Linkage

- Uses 0A and 0B.
- Stage 8 determines whether AI-specific portions remain applicable and reconciles this envelope.
- Stage 32 measures actual economics against the applicable 0C scenario.
