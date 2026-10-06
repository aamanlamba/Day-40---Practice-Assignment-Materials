---
id: 6
name: Root-Cause Analysis
folder: 06-root-cause
mode: read-only
depends_on: [4, 5]
approval: false
artifacts:
  - root-cause-tree.md
  - five-whys.md
  - fishbone-analysis.md
  - causal-hypotheses.md
  - evidence-confidence-matrix.md
  - validation-plan.md
  - confirmed-root-causes.md
  - root-cause-readiness.md
---
## Objective

Perform evidence-based causal analysis to identify the root causes behind the problem framed in Stage 3 and the bottlenecks found in Stage 5.

Use evidence from: Stages 3–5; data, logs, code paths and tests in the repository.

## Scope

Causes across process, people, policy, data, technology, organization and architecture. Use 5-Whys, Fishbone, causal trees or equivalent.

## Required Analysis

For every proposed cause record:
1. supporting evidence;
2. contradictory evidence;
3. confidence (High / Medium / Low);
4. validation method (data query, test, stakeholder confirmation, experiment).

## Constraints / Guardrails

Do not: label correlation as causation without evidence; promote a hypothesis to `confirmed-root-causes.md` without a completed validation.

## Stage-Specific Completion Gate

- Every causal hypothesis has supporting and contradictory evidence fields (even if "none found").
- `confirmed-root-causes.md` contains only validated causes; others remain hypotheses with a validation plan.

## Lifecycle Linkage

- Uses Stages 4–5. Feeds Stage 8 (intervention choice) and Stage 9 (PRD).
