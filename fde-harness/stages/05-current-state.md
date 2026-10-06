---
id: 5
name: Discover Current Process & Brownfield Landscape
folder: 05-current-state
mode: read-only
depends_on: [0A, 3, 4]
approval: false
artifacts:
  - current-process-map.md
  - business-workflow-map.md
  - system-landscape.md
  - integration-landscape.md
  - brownfield-inventory.md
  - manual-handoffs.md
  - process-bottlenecks.md
  - control-points.md
  - dependency-hotspots.md
  - current-state-summary.md
---
## Objective

Map the current end-to-end business process and system landscape to expose bottlenecks, control gaps and fragile dependencies.

Use evidence from: Stage 0A orientation, Stage 3 journeys, Stage 4 baseline; code paths, batch jobs, adapters, SQL, data and runbooks.

## Scope

Identify actors, steps, decisions, queues, handoffs, systems, APIs, events, databases, ETL, batch jobs, manual workarounds, integrations, controls and operational dependencies.

## Required Analysis

Evaluate:
1. End-to-end process flow (diagram in Mermaid where helpful) with each step traced to code or evidence.
2. System and integration landscape at a deeper level than 0A.
3. Bottlenecks, rework, duplication and delays (linked to Stage 4 KPIs where possible).
4. Control points and control gaps.
5. Fragile dependencies and hotspots.

## Constraints / Guardrails

Do not: modify the repository; recommend solutions (record observations and impacts only); overwrite Stage 0A artifacts — note where 0A was wrong or incomplete in `current-state-summary.md`.

## Stage-Specific Completion Gate

- Every process step and system cites code, configuration, data or documentation evidence, or is tagged Unknown.
- Bottlenecks and control gaps are linked to measurable impact or flagged as unmeasured.

## Lifecycle Linkage

- Deepens Stage 0A. Feeds Stage 6 (root cause) and Stage 7 (repo assessment).
