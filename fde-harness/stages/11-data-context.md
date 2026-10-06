---
id: 11
name: Data, Knowledge & Context Strategy
folder: 11-data-context
mode: read-only
depends_on: [9, 10]
approval: false
artifacts:
  - data-source-inventory.md
  - data-contracts.md
  - data-quality-rules.md
  - lineage-map.md
  - knowledge-model.md
  - metadata-model.md
  - retrieval-strategy.md
  - context-engineering-strategy.md
  - context-compaction-policy.md
  - provenance-policy.md
  - synthetic-data-strategy.md
  - data-context-risks.md
---
## Objective

Define the data, knowledge and runtime-context architecture.

Use evidence from: Stage 10 architecture, Stage 9 PRD; schemas, data files, ETL code and data descriptors in the repository.

## Scope

Sources, ownership, schemas, contracts, quality, lineage, provenance, freshness, retention, metadata, PII and access controls. Ingestion, chunking, indexing, retrieval, reranking, grounding, context assembly, compaction and provenance/citation requirements. Synthetic-data requirements where production data cannot be used.

## Required Analysis

Evaluate:
1. Data sources and contracts (schema, owner, freshness, quality rules).
2. Lineage from source to consumption.
3. PII and access-control requirements.
4. Retrieval/context strategy — only where Stage 8 accepted GenAI/agentic use; otherwise mark those artifacts Not Applicable with justification.
5. Synthetic-data strategy.

## Constraints / Guardrails

Do not: modify data or schemas; assume data ownership without evidence (mark PROVISIONAL).

## Stage-Specific Completion Gate

- Every data source has a contract or a documented gap.
- Retrieval/context artifacts are either specified or explicitly Not Applicable with reference to Stage 8.

## Lifecycle Linkage

- Uses Stages 9–10. Feeds Stages 12, 19, 21 and FINAL.
