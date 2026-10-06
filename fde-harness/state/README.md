# Harness state

- `registry.json` — **local, git-ignored run state**: one entry per initialised target repository: engagement name, stages done / total, next stage, blocked stages, last update. Updated automatically by `fde.py` (override the location with `FDE_REGISTRY=/path/registry.json`).
- Per-repository authoritative state lives **in the target repository** under `docs/_harness/state.json` so that it is version-controlled alongside the evidence it describes. Schema:

```jsonc
{
  "harness_version": "1.0.0",
  "harness_path": "/abs/path/fde-harness",
  "engagement": "repo-name",
  "author": "…",
  "test_command": "python -m pytest",
  "initialised_at": "…Z",
  "initial_commit": "<sha>",
  "stages": {
    "0A": {
      "status": "NOT STARTED | IN PROGRESS | PASS | CONDITIONAL PASS | BLOCKED",
      "runs": 1,
      "folder": "00-preflight/discovery",
      "branch": "main | fde/stage-15-…",
      "base_commit": "<sha at begin>",
      "started_at": "…Z", "completed_at": "…Z",
      "approved_by": "…",
      "forced_with_unmet_dependencies": ["…"],
      "last_check": {"at": "…Z", "result": "PASS", "errors": 0, "warnings": 2}
    }
  }
}
```
