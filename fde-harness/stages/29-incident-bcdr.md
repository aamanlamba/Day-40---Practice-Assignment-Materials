---
id: 29
name: AI Incident Response + BC/DR
folder: 29-incident-bcdr
mode: read-only
depends_on: [28]
approval: false
artifacts:
  - ai-incident-playbook.md
  - incident-severity-matrix.md
  - containment-procedures.md
  - forensics-evidence-policy.md
  - communications-plan.md
  - bc-plan.md
  - dr-plan.md
  - rto-rpo.md
  - failover-procedure.md
  - recovery-procedure.md
  - tabletop-scenario.md
  - tabletop-results.md
  - incident-readiness.md
---
## Objective

Define incident and continuity procedures and exercise them with a tabletop or simulation.

Use evidence from: Stages 24, 27, 28.

## Scope

Prompt injection, unsafe actions, compromised tools, data leakage, bad retrieval, model/provider failure, cost runaway, corrupted configuration, infrastructure outages and disaster scenarios. Detection, severity, containment, evidence preservation, communications, recovery, RTO/RPO and failover.

## Constraints / Guardrails

Do not: claim a tabletop occurred unless it did — `tabletop-results.md` must record date, participants (roles) and outcomes, or state it is pending.

## Stage-Specific Completion Gate

- Every scenario has detection, containment and recovery steps; RTO/RPO are stated with their basis.

## Lifecycle Linkage

- Feeds Stages 30, 38.
