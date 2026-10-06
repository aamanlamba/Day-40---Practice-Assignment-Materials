---
id: 8
name: AI-vs-No-AI Qualification
folder: 08-ai-qualification
mode: read-only
depends_on: [0C, 3, 6, 7]
approval: true
artifacts:
  - intervention-options.md
  - ai-vs-no-ai-matrix.md
  - deterministic-vs-ai-boundaries.md
  - minimum-intelligence-assessment.md
  - minimum-agency-assessment.md
  - intervention-hypothesis.md
  - economics-baseline-reconciliation.md
  - qualification-decision.md
checks:
  - "qualification-decision.md :: (?i)agentic"
---
## Objective

Decide, per intervention, the **minimum necessary intelligence and minimum necessary agency**, rejecting AI wherever conventional approaches are safer, cheaper or more reliable.

Use evidence from: Stage 0C envelope, Stage 3 problem, Stage 6 root causes and Stage 7 assessment.

## Scope

Evaluate each intervention against: process redesign, policy change, deterministic software, rules engines, workflow automation, analytics, classical ML, GenAI and agentic AI.

## Required Analysis

Evaluate:
1. Intervention options per confirmed root cause.
2. AI-vs-no-AI matrix with criteria: safety, cost, reliability, explainability, latency, maintainability, data availability.
3. What uncertainty, language, reasoning, generation or adaptive-decision requirement (if any) justifies AI.
4. Deterministic vs AI boundaries.
5. Minimum intelligence and minimum agency for each accepted AI use.
6. Reconciliation with Stage 0C — retire irrelevant AI cost assumptions.

## Constraints / Guardrails

Do not: justify AI by novelty or stakeholder preference; accept agentic AI where a bounded workflow suffices.

## Stage-Specific Completion Gate

- `qualification-decision.md` states explicitly, per intervention: **No AI / Classical ML / GenAI / Agentic AI**, and states clearly whether agentic AI is **justified or rejected** (Stage 22 depends on this).
- `economics-baseline-reconciliation.md` lists retained and retired 0C assumptions.
- Human approval recorded at completion.

## Lifecycle Linkage

- Uses 0C, 3, 6, 7. Determines applicability of Stages 19, 22 and the AI-specific portions of 26 and 32.
