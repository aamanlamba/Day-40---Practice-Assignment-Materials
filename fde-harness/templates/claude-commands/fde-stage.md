---
description: Begin and execute one AI FDE spine stage (e.g. 0A, 7, 15, FINAL) against this repository
argument-hint: <stage-id>
allowed-tools: Bash(python3 {{FDE}}:*)
---
The harness has begun stage `$ARGUMENTS` (dependency check, evidence snapshot, branch for write stages) and rendered the stage prompt below.

!`python3 "{{FDE}}" begin $ARGUMENTS --repo .`

---

Execute the stage prompt above **exactly**, as the AI FDE agent:

1. If the output above is an error (unmet dependencies, dirty tree, unknown stage), stop and explain it — do not work around it.
2. Read the listed prior-stage inputs first.
3. Respect the stage mode and write boundaries. In READ-ONLY stages change nothing outside the stage's docs folder and `docs/_harness/reports/`.
4. Create every required artifact with the mandatory header and sections; classify evidence; never invent facts.
5. Write the stage report, then run `python3 "{{FDE}}" check $ARGUMENTS --repo .` and fix every ERROR. Repeat until it passes or the stage is genuinely BLOCKED.
6. Do **not** run `fde.py complete` — completion and approvals are recorded by a human.
7. Finish with the Required Final Response (7 items).
