---
id: 1
name: Engage & Qualify
folder: 01-engagement
mode: read-only
depends_on: [0A, 0B, 0C]
approval: true
artifacts:
  - engagement-canvas.md
  - team-charter.md
  - qualification-checklist.md
  - use-case-hypothesis.md
  - engagement-risks.md
  - open-qualification-questions.md
  - engagement-go-no-go.md
checks:
  - "engagement-go-no-go.md :: (?im)^\\**classification:?\\**:?\\s*\\**(Go|Conditional Go|No-Go)\\b"
---
## Objective

Qualify the engagement using Stage 0 evidence, deciding whether it should proceed as **Go, Conditional Go or No-Go**.

Use evidence from:
- Stage 0A/0B/0C artifacts;
- any business change request, scenario description or stakeholder statements present in the repository.

## Scope

Identify: client context, business problem, sponsor, business owner, technical owner, urgency, expected outcomes, dependencies, delivery constraints, and reasons the initiative could be premature or non-viable.

Exclude: solution design and technology selection.

## Required Analysis

Evaluate:
1. Business problem clarity and evidence for it.
2. Sponsorship and ownership (evidenced vs claimed vs missing).
3. Urgency and expected outcomes.
4. Dependencies and delivery constraints.
5. Reasons the engagement could be premature or non-viable.

## Constraints / Guardrails

Do not:
- treat stakeholder claims as validated evidence — separate them explicitly;
- invent sponsors or owners; record gaps as open qualification questions.

Only: write under `docs/01-engagement/`.

## Stage-Specific Completion Gate

- `engagement-go-no-go.md` classifies the engagement as **Go, Conditional Go or No-Go** with evidence, on a line of the form `Classification: Conditional Go`; Conditional Go lists the conditions and who must satisfy them.
- Stakeholder claims and validated evidence are visibly separated.
- Human approval recorded at completion.

## Lifecycle Linkage

- Uses Stage 0 evidence.
- Feeds Stage 2 (stakeholders) and Stage 3 (problem framing).
