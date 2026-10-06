---
id: 24
name: Security + Privacy + Responsible AI by Design
folder: 24-security-privacy
mode: write
depends_on: [10, 21, 23]
approval: false
artifacts:
  - threat-model.md
  - attack-surface-map.md
  - security-control-matrix.md
  - privacy-impact-assessment.md
  - prompt-injection-controls.md
  - agent-security-controls.md
  - data-protection-controls.md
  - responsible-ai-controls.md
  - security-test-plan.md
  - security-test-results.md
  - residual-security-risks.md
  - security-readiness.md
---
## Objective

Threat-model the system and define and implement controls **within approved scope**.

Use evidence from: Stage 10 security architecture, Stages 20–23.

## Scope

Application, APIs, identity, data, prompts, RAG, models, agents, tools, context, supply chain and integrations. Address prompt/indirect injection, data exfiltration, insecure output handling, excessive agency, insecure tool use, poisoning, secrets exposure, authorization bypass, privacy/PII and relevant responsible-AI risks.

## Brownfield Change Protocol

Control implementations follow the Stage 15 protocol (`fde(24): <control-id> <summary>`), with a test for each control.

## Constraints / Guardrails

Do not: perform attacks against anything outside the local repository; mark AI-specific controls as implemented if Stage 8 rejected AI (mark Not Applicable).

## Stage-Specific Completion Gate

- Every threat maps to a control or an accepted residual risk.

## Lifecycle Linkage

- Feeds Stages 25, 26, 27.
