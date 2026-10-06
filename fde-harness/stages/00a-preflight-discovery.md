---
id: 0A
name: Pre-Flight Repository & System Orientation
folder: 00-preflight/discovery
mode: read-only
depends_on: []
approval: false
artifacts:
  - repository-overview.md
  - system-landscape.md
  - technology-inventory.md
  - high-level-architecture.md
  - integration-overview.md
  - data-flow-overview.md
  - workflow-overview.md
  - test-overview.md
  - security-observability-overview.md
  - assumptions-unknowns.md
  - initial-risk-register.md
  - discovery-summary.md
---
## Objective

Establish a high-level factual orientation of the existing brownfield environment **before changing anything**, so that the engagement can be qualified (Stage 1) without making transformation recommendations.

Use evidence from:
- the repository tree, README/operational notes, manifests and build files;
- source code, configuration, schemas, SQL, data descriptors and scripts;
- existing tests, CI definitions, observability assets and inherited documentation.

## Scope

Analyse across:
- repository structure, technologies, languages, frameworks and dependency manifests;
- applications, services, APIs and their entry points;
- databases, schemas, ETL/data pipelines and batch jobs;
- integrations, adapters and external interfaces;
- tests, security mechanisms, observability, runtime/deployment clues;
- major business workflows the system appears to support.

Include: what is clearly present, what appears operational, what is unknown, and where deeper investigation is required.

Exclude: deep refactoring analysis, code-quality scoring, technical-debt registers and any transformation recommendation (these belong to Stage 7 and later).

## Required Analysis

Evaluate:
1. Repository layout and component boundaries (as observed, not as intended).
2. Technology inventory with versions where declared.
3. Runtime topology: what runs, how it is started, what it talks to.
4. Data stores, data flows and pipeline/batch behaviour.
5. Integration points and protocols.
6. Business workflows inferred from code, data and docs.
7. Test assets: what exists, what they appear to cover (do not judge quality yet).
8. Security and observability mechanisms present or visibly absent.
9. Risks visible at orientation depth.

## Constraints / Guardrails

Do not:
- modify application code, tests, dependencies, configuration, infrastructure, data or workflows;
- install dependencies into the repository, run migrations, or start processes that write to repository data;
- perform deep refactoring analysis or recommend transformations;
- invent owners, purposes or behaviours not supported by evidence.

Only:
- read files, list directories, inspect git history, and run strictly read-only commands;
- write under `docs/00-preflight/discovery/` and the harness report.

Preserve: the repository exactly as found.

## Stage-Specific Completion Gate

- Orientation is sufficient to conduct engagement qualification (Stage 1).
- Every component listed in `system-landscape.md` cites at least one repository path.
- `assumptions-unknowns.md` separates Assumptions from Unknowns, and each Unknown says where deeper investigation is required.
- `initial-risk-register.md` lists risks with likelihood, impact and evidence.
- No transformation recommendations appear in any artifact.

## Lifecycle Linkage

- First stage of the spine; no prior inputs.
- Feeds Stage 0B (boundaries), 0C (economics envelope), Stage 1 (qualification) and Stage 5 (current state).
- Deep repository assessment is intentionally deferred to Stage 7.
