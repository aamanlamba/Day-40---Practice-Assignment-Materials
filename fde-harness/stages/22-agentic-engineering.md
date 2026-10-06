---
id: 22
name: Agent, Tool, Harness, Loop & Graph Engineering
folder: 22-agentic-engineering
mode: write
depends_on: [8, 19, 20]
approval: false
na_allowed: true
artifacts:
  - agent-architecture.md
  - harness-specification.md
  - tool-contracts.md
  - tool-permission-map.md
  - state-model.md
  - memory-policy.md
  - context-policy.md
  - graph-definition.md
  - loop-control-policy.md
  - termination-rules.md
  - agent-budget-policy.md
  - sandbox-policy.md
  - agent-test-plan.md
  - agent-test-results.md
  - agent-readiness-gate.md
---
## Objective

**Only where Stage 8 justified agentic behaviour**, engineer the full agent runtime.

Use evidence from: Stage 8 decision, Stage 19 intelligence core, Stage 20 application.

## Scope

Planner/reasoner roles, strict tool schemas, tool gateways, state, memory, context management, workflow graph, loop controls, termination criteria, token/time/tool budgets, retries, evaluator/critic logic, sandboxing, permissions and recovery.

## Constraints / Guardrails

Prevent uncontrolled recursion, privilege expansion, tool misuse and context accumulation. Follow the Stage 15 brownfield change protocol for code (`fde(22): WI-### <summary>`).

**If agentic AI was rejected at Stage 8, create `not-applicable.md` with justification rather than inventing agent artifacts.**

## Stage-Specific Completion Gate

- Either all artifacts exist with test evidence, or `not-applicable.md` cites the Stage 8 rejection.

## Lifecycle Linkage

- Gated by Stage 8. Controls reconciled in Stage 23; red-teamed in Stage 26.
