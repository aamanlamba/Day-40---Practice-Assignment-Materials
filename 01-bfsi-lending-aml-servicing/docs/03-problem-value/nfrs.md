---
stage: "3 — Frame Problem & Value"
title: "Non-Functional Requirements"
version: "1.0"
date: "2026-10-06"
author: "Engagement Lead / Claude Code"
status: "Approved"
evidence_sources:
  - "docs/00-preflight/discovery/security-observability-overview.md"
  - "docs/00-preflight/ai-economics/quality-latency-cost-envelope.md"
  - "docs/00-preflight/operating-contract/data-use-constraints.md"
  - "docs/legacy/business-rules.txt"
  - "docs/legacy/release-notes.md"
  - "CHANGE_REQUEST.md"
---

# Non-Functional Requirements

No stakeholder has been interviewed (Stage 2). Personas P1-P10 and all stakeholder positions are [Inference]; requirement sources marked *Evidence* are repository facts, *Claim* is a document statement, *Hypothesis* is to be validated with the named persona.

| ID | Requirement | Source | Category |
|---|---|---|---|
| NFR-001 | Existing lending and payment outputs shall be identical before and after any change, verified by a regression comparison on the baseline dataset | Claim `CHANGE_REQUEST.md:3`; 0B change control rule 4 | Behaviour |
| NFR-002 | Case ranking and reasons shall be explainable to a non-technical reviewer in the same screen | Claim `CHANGE_REQUEST.md:3` | Explainability |
| NFR-003 | Reviewers shall receive priority information within an interactive response time agreed with operations (proposal: 5 s at the 95th percentile) | Assumption; 0C envelope (5 s) | Performance |
| NFR-004 | The daily reconciliation shall complete before 08:00 local (window length to be confirmed) | Evidence `business-rules.txt:4` | Timeliness |
| NFR-005 | Access shall require a verified identity and role-based permission; administrative functions shall not depend on user names | Evidence 0A R-01 | Security |
| NFR-006 | Personal data shown or exported shall be minimised and every access shall be auditable | Evidence 0A R-04; 0B data constraints | Privacy/audit |
| NFR-007 | All record sets shall be synthetic unless a human approves real data | Evidence `README.md:50`; 0B | Data governance |
| NFR-008 | Every consequential recommendation shall have a named human who can accept or override it, and the override shall be recorded | Claim `CHANGE_REQUEST.md:3`; 0B T6 | Human control |
| NFR-009 | Cost of any added automation shall stay within the envelope the sponsor approves (provisional $0.10 per case, 0C) | Assumption; 0C | Cost |
| NFR-010 | Operational health (availability, error rate, latency) shall be observable per route with status information | Evidence 0A R-07 | Observability |
| NFR-011 | Changes shall be releasable and reversible with a documented rollback | Evidence `release-notes.md:5` | Operability |
| NFR-012 | Existing automated checks (13 tests at baseline) shall pass, and new behaviour shall have tests | Evidence 0A test overview; 0B change control | Quality |
| NFR-013 | Retention and deletion of case records shall meet applicable regulation | Hypothesis; Q-009 | Compliance |

- [Verified Fact] NFR-003 and NFR-009 take their numbers from the provisional 0C envelope, which is itself an assumption (no latency measurement of the current service exists).
- NFR-005 conflicts with preserving existing behaviour in the narrow case of the characterized admin shortcut (conflict X-1 in `docs/02-stakeholders/stakeholder-conflicts.md`); the sponsor must resolve it.

## Assumptions

- [Assumption] Proposed numeric limits are starting points for negotiation.

## Unresolved Issues

- [Unknown] Required availability, volume and retention targets; none stated by any stakeholder.

## Residual Risks

- Numbers inherited from 0C could be repeated as if agreed.
