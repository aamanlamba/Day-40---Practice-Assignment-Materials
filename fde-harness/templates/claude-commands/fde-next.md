---
description: Run the next pending AI FDE spine stage for this repository
allowed-tools: Bash(python3 {{FDE}}:*)
---
!`python3 "{{FDE}}" begin next --repo .`

---

If the output above is an error (spine complete, unmet dependencies, dirty tree), report it and stop. Otherwise execute the stage prompt above exactly, following the same rules as `/fde-stage`: read prior inputs; respect mode and write boundaries; create every required artifact with header and sections; write the stage report; run `python3 "{{FDE}}" check <stage> --repo .` and fix every ERROR; do not run `complete`; finish with the Required Final Response.
