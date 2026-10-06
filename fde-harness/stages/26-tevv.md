---
id: 26
name: TEVV + AI Red Teaming
folder: 26-tevv
mode: write
depends_on: [13, 19, 22, 24, 25]
approval: false
artifacts:
  - tevv-plan.md
  - golden-dataset-spec.md
  - edge-dataset-spec.md
  - adversarial-dataset-spec.md
  - failure-dataset-spec.md
  - evaluation-metrics.md
  - release-thresholds.md
  - tevv-results.md
  - red-team-plan.md
  - red-team-findings.md
  - remediation-evidence.md
  - residual-tevv-risks.md
  - tevv-release-gate.md
---
## Objective

Execute formal Test, Evaluation, Verification and Validation across deterministic and probabilistic behaviour.

Use evidence from: Stage 13 traceability, Stages 19–25.

## Scope

Representative, golden, edge, adversarial, safety and failure datasets. Evaluate functionality, model/RAG quality, groundedness, hallucination, abstention, agents/tools where applicable, security, privacy, resilience and business outcomes. Red-team prompt injection, data leakage, control bypass, excessive agency and tool abuse.

## Brownfield Change Protocol

Test and evaluation assets may be added in the repository (e.g. `tests/`, `evals/`) within `write-boundaries.txt`, committed as `fde(26): <summary>`. Implementation fixes go back through the owning stage.

## Constraints / Guardrails

Release thresholds must be **objective and pre-declared** — commit `release-thresholds.md` before running the evaluations it governs. Do not change thresholds after seeing results.

## Stage-Specific Completion Gate

- `tevv-release-gate.md` compares each result to its pre-declared threshold.

## Lifecycle Linkage

- Feeds Stages 27, 30, 42.
