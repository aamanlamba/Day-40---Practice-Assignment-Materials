---
description: Run the AI FDE gate check for a stage and fix failures
argument-hint: <stage-id>
allowed-tools: Bash(python3 {{FDE}}:*)
---
!`python3 "{{FDE}}" check $ARGUMENTS --repo . 2>&1 || true`

Explain the gate-check result above. For each ERROR, state whether it is fixable inside the stage's write boundaries; if so, fix it and re-run the check. Never fix a boundary error by changing files belonging to another stage — revert the out-of-boundary change instead. Do not run `fde.py complete`.
