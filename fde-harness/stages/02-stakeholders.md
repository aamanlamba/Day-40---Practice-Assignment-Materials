---
id: 2
name: Stakeholder Discovery & Authority Confirmation
folder: 02-stakeholders
mode: read-only
depends_on: [0B, 1]
approval: false
artifacts:
  - stakeholder-map.md
  - stakeholder-needs-matrix.md
  - decision-rights-map.md
  - approval-authority-map.md
  - stakeholder-conflicts.md
  - escalation-map.md
  - operating-contract-confirmations.md
---
## Objective

Identify stakeholders and their authority, and reconcile them with the Stage 0B provisional contract, so that governance assumptions are confirmed or explicitly left open.

Use evidence from: Stage 0B and Stage 1 artifacts; contact matrices, ownership files (e.g. CODEOWNERS), commit history and inherited documents.

## Scope

Stakeholders across business, users, product, architecture, engineering, data, security, privacy, compliance, risk, operations and leadership. Capture needs, incentives, concerns, responsibilities, conflicts, approval authority and decision rights.

## Required Analysis

Evaluate:
1. Who exists (evidenced) vs who is implied vs who is missing.
2. Needs, incentives and concerns per stakeholder group.
3. Decision rights and approval authority.
4. Conflicts between stakeholder goals.
5. Escalation routes.
6. Which Stage 0B PROVISIONAL items can now be confirmed, changed or must remain open.

## Constraints / Guardrails

Do not: invent owners where none have been assigned — record them as **unresolved governance gaps**; edit Stage 0B artifacts (record confirmations here instead).

## Stage-Specific Completion Gate

- `operating-contract-confirmations.md` lists every 0B item flagged for Stage 2 with disposition: Confirmed / Changed / Still Provisional, plus evidence.
- Unassigned ownership appears as governance gaps, not names.

## Lifecycle Linkage

- Reconciles Stage 0B; uses Stage 1.
- Feeds Stage 3, Stage 23, Stage 25 and Stage 37.
