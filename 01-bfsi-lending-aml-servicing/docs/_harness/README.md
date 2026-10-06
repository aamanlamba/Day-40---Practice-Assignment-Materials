# docs/_harness

Harness state for the AI FDE production-delivery spine. Managed by `/Users/aamanlamba/Code/Day-40---Practice-Assignment-Materials/fde-harness/bin/fde.py`.

- `state.json` — stage statuses, runs, approvals, base commits
- `write-boundaries.txt` — human-approved globs for write-mode stages
- `reports/` — stage reports (Required Final Response)
- `checks/` — machine gate-check results
- `prompts/` — rendered prompts as executed (audit)
- `history/` — snapshots of earlier stage evidence before re-runs (never edit)
- `run-log.md` — append-only event log
