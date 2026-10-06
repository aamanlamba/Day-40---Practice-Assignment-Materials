# Open Question Log

Append-only log of questions raised at each stage. Each stage adds rows when it closes and updates the status of earlier rows; answered questions are marked, never deleted. "Ask" uses the assumed personas P1-P10 defined in `docs/00-preflight/operating-contract/provisional-operating-contract.md` (assumed, not evidenced).

Status values: OPEN, ANSWERED (with evidence reference), SUPERSEDED.

| ID | Raised | Question | Ask | Resolve in | Status |
|---|---|---|---|---|---|
| Q-001 | 0A (U-01) | Who are the named owners/approvers; data owner is "unclear", AI-model owner "not-established", backups blank | P1 | Stage 2 | OPEN |
| Q-002 | 0A (U-02) | What are the authoritative underwriting and AML-priority rules? `approve()` does not match recorded outcomes (176 DECLINED rows satisfy it) | P3, P4 | Stage 5/7 | OPEN |
| Q-003 | 0A (U-03) | Do production/staging/UAT environments exist; what is the release path? | P7, P8 | Stage 5 | OPEN |
| Q-004 | 0A (U-04) | What are the real partner and legacy-core interfaces and error codes beyond `00`/`91`? | P8 | Stage 5 | OPEN |
| Q-005 | 0A (U-05) | What is the system of record, lineage and refresh cadence for each CSV? | P6 | Stage 5 | OPEN |
| Q-006 | 0A (U-06) | Why are `kyc_cases.csv` and `beneficiaries.csv` unused; are they in scope? | P6, P4 | Stage 5 | OPEN |
| Q-007 | 0A (U-07) | Is the Postgres `ops` schema deployed and what populates it? | P6, P8 | Stage 7 | OPEN |
| Q-008 | 0A (U-08) | Does the Angular app build and does the Playwright test pass? | P8 | Stage 7 (needs write-capable stage) | OPEN |
| Q-009 | 0A (U-09), 0B (G-10) | Which regulatory/compliance obligations apply (AML/KYC retention, audit, residency)? | P4, P5, P10 | Stage 25 | OPEN |
| Q-010 | 0A (U-10) | What do null, `UNKNOWN`, `score` and `days_past_due` mean in business terms? | P3, P4, P6 | Stage 5 | OPEN |
| Q-011 | 0A (U-11), 0B (G-18) | What are the budget, timeline and value expectations behind the change request? | P1 | Stage 0C | OPEN |
| Q-012 | 0A (U-12) | What latency, load and availability baselines exist? | P7, P8 | Stage 5/6 | OPEN |
| Q-013 | 0A (U-13), 0B (G-05) | Who consumes the API besides the Angular app? | P8 | Stage 5 | OPEN |
| Q-014 | 0A (U-14) | Does the system behave the same on Python 3.11, the declared minimum? | P8 | Stage 7 | OPEN |
| Q-015 | 0B (G-01) | Who is the named sponsor, engagement lead and approver of the operating contract? | P1 | Stage 2 | OPEN |
| Q-016 | 0B (G-17) | Which write globs does a human approve for `docs/_harness/write-boundaries.txt`? | P2, P5 | Before Stage 15 | OPEN |
| Q-017 | 0B (G-06, G-07) | Which analyst/underwriter actions must stay human-decided, and what override/escalation evidence is required? | P3, P4 | Stage 23 | OPEN |
| Q-018 | 0B (G-09) | Who owns AI-model accountability? | P1, P9 | Stage 25 | OPEN |
| Q-019 | 0B (G-12, G-13) | What vendor/tool approvals and data-access audit policy apply? | P5 | Stage 25 | OPEN |
| Q-020 | 0B (G-14, G-15) | What is the steady-state RACI, support and incident model? | P1, P7 | Stage 37 | OPEN |
| Q-021 | 0B (data-use) | Does the tool provider retain prompt inputs, and is that acceptable for this data? | P5, P10 | Stage 2 | OPEN |
| Q-022 | 0B (this run) | Are the assumed personas P1-P10 acceptable as working placeholders? | P2 | Stage 2 | OPEN |
