---
id: 0B
name: Provisional Operating Contract & Engineering Boundaries
folder: 00-preflight/operating-contract
mode: read-only
depends_on: [0A]
approval: true
artifacts:
  - provisional-operating-contract.md
  - scope-boundaries.md
  - repository-write-boundaries.md
  - environment-access-boundaries.md
  - data-use-constraints.md
  - provisional-tool-agent-permissions.md
  - provisional-human-approval-rules.md
  - evidence-contract.md
  - change-control-rules.md
  - stop-conditions.md
  - open-governance-decisions.md
  - operating-contract-readiness.md
checks:
  - "provisional-operating-contract.md :: PROVISIONAL"
  - "open-governance-decisions.md :: (?i)stage\\s*2"
  - "open-governance-decisions.md :: (?i)stage\\s*23"
  - "open-governance-decisions.md :: (?i)stage\\s*25"
  - "open-governance-decisions.md :: (?i)stage\\s*37"
---
## Objective

Create a **provisional** engagement operating contract from currently available evidence, defining what the engagement may and may not do, so that later stages act inside explicit, reviewable boundaries.

Use evidence from:
- Stage 0A discovery artifacts (`docs/00-preflight/discovery/`);
- repository configuration, environments, data descriptors and inherited documentation.

## Scope

Define:
- current scope and exclusions; repositories and environments in play;
- data boundaries and data-use constraints (including synthetic vs real data, PII handling);
- permitted and prohibited actions; repository write restrictions; production-access restrictions;
- security/privacy constraints;
- provisional tool and agent permissions;
- evidence requirements and change-control expectations;
- human-approval triggers, stop conditions and escalation assumptions.

Exclude: final governance authority, final ownership assignments and the steady-state operating model (Stage 37).

## Required Analysis

Evaluate:
1. Which repository paths are safe to modify later and under which stage (write boundaries).
2. Which environments exist or are implied, and what access is permissible.
3. Data classes present and constraints on their use.
4. Which actions require explicit human approval.
5. Conditions under which work must stop and escalate.
6. Governance decisions that cannot be made yet and who would plausibly confirm them.

## Constraints / Guardrails

Do not:
- invent owners, approvers or decision rights — mark unresolved ownership or decision rights as **PROVISIONAL**;
- treat any provisional decision as final authority;
- modify anything outside `docs/00-preflight/operating-contract/`.

Only:
- derive boundaries from evidence and record their basis.

Preserve: the repository exactly as found.

`repository-write-boundaries.md` must list concrete path globs that later write stages (15, 19–22, 24, 26–28, 30, 31) may change. These are **proposals**: a human transfers approved globs into `docs/_harness/write-boundaries.txt`, which is what the harness enforces.

## Stage-Specific Completion Gate

- Every ownership/decision-right statement without evidence is labelled PROVISIONAL.
- `open-governance-decisions.md` explicitly flags items requiring confirmation during Stages 2, 23, 25 and 37.
- `stop-conditions.md` lists concrete, testable stop conditions.
- `operating-contract-readiness.md` states whether the contract is sufficient to proceed, with gaps.
- Human approval recorded at completion (`fde.py complete 0B --approved-by ...`).

## Lifecycle Linkage

- Uses Stage 0A evidence.
- Confirmed or updated in Stage 2 (authority), Stage 23 (human control), Stage 25 (governance) and closed in Stage 37 (operating model).
- Stage 15 may modify implementation only within approved 0B boundaries.
