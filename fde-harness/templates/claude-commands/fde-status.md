---
description: Show AI FDE delivery-spine progress for this repository
allowed-tools: Bash(python3 {{FDE}}:*)
---
!`python3 "{{FDE}}" status --repo .`

Summarise the status above in 3–5 lines: stages completed, any BLOCKED stages, stages awaiting human approval, and the next stage to run (`/fde-next` or `/fde-stage <id>`).
