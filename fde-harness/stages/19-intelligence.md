---
id: 19
name: Intelligence Core — Prompt, Retrieval & Model Engineering
folder: 19-intelligence
mode: write
depends_on: [8, 11, 18]
approval: false
na_allowed: true
artifacts:
  - prompt-registry.md
  - model-configuration.md
  - model-benchmark.md
  - extraction-pipeline.md
  - retrieval-pipeline.md
  - rag-design.md
  - evaluation-dataset-spec.md
  - rag-evaluation-results.md
  - prompt-evaluation-results.md
  - grounding-results.md
  - quality-latency-cost-results.md
  - intelligence-release-gate.md
---
## Objective

Implement the **approved** intelligence layer: version-controlled prompts, model configuration, structured outputs, extraction, embeddings, retrieval, reranking, grounding and inference.

Use evidence from: Stage 8 decision, Stage 11 data/context strategy, Stage 18 delivery plan.

## Scope

Build evaluation datasets **before** tuning. Benchmark models where justified. Measure retrieval relevance, groundedness, answer quality, hallucination/unsupported claims, abstention, latency and cost.

## Brownfield Change Protocol

Follow the same protocol as Stage 15: paths must be inside `write-boundaries.txt`; one work item per commit (`fde(19): WI-### <summary>`); run tests/evals after each change; log results. Store executable prompts/configuration in version-controlled implementation directories (e.g. `prompts/`, `config/`), not only in docs.

## Constraints / Guardrails

Do not: implement intelligence not approved in Stage 8; tune against the evaluation set used for release decisions; commit secrets or API keys; report metrics you did not measure.

**If Stage 8 approved no GenAI/ML capability**, create only `not-applicable.md` with justification citing `docs/08-ai-qualification/qualification-decision.md` (harness extension mirroring the Stage 22 rule).

## Stage-Specific Completion Gate

- Evaluation datasets exist before tuning results are reported.
- `intelligence-release-gate.md` compares measured results to declared thresholds.

## Lifecycle Linkage

- Applicable only where Stage 8 approved it. Evaluated formally in Stage 26; costs measured in Stage 32.
