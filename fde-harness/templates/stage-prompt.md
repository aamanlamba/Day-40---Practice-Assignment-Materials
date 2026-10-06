# AI FDE Spine — Stage {{id}} — {{name}}

| Field | Value |
|---|---|
| Target repository | `{{repo}}` |
| Run date (UTC) | {{date}} |
| Author / agent | {{author}} |
| Stage mode | **{{mode}}** — {{mode_meaning}} |
| Git branch | `{{branch}}` |
| Base commit | `{{base}}` |
| Run number | {{run}} |

{{contract}}

---

{{body}}

---

## Evidence Rules

Classify every material statement as one of:

- **Verified Fact** — directly observed in the repository, a command output, a test result or approved stakeholder evidence. Cite it.
- **Inference** — reasoned from verified facts. Name the facts it rests on.
- **Assumption** — taken as true without evidence. Record it in the artifact's Assumptions section.
- **Unknown** — not determinable from available evidence. Record it; do not invent an answer.

Inline tags such as `[Verified Fact]`, `[Inference]`, `[Assumption]` and `[Unknown]` are preferred.

Where repository/system evidence exists, reference file paths (with line numbers where useful), configuration, APIs, schemas, tests, logs, database objects, architecture artifacts and approved stakeholder evidence. Do not present assumptions as facts.

For every material finding: state the finding; provide evidence; identify impact; identify risk; identify confidence (High / Medium / Low); identify unresolved questions.

---

## Write Boundaries (enforced by `fde.py check`)

{{boundaries}}

Never modify `docs/legacy/` or another stage's `docs/` folder. Earlier evidence is preserved by the harness under `docs/_harness/history/`; do not delete or silently rewrite it. If you are re-running this stage, bump each artifact's `version` and add a `## Change Log` entry that explains what changed and why.

---

## Prior-Stage Inputs

{{inputs}}

---

## Required Artifacts

Create the directory `docs/{{folder}}/` and save:

{{artifacts}}

Every artifact must start with this header (YAML front matter) and contain the mandatory sections:

```markdown
{{artifact_header}}
```

---

## Completion Gate (generic — applies in addition to the stage-specific gate above)

The stage is complete only when:

- all required artifacts exist under `docs/{{folder}}/` with valid headers and mandatory sections;
- critical gaps are resolved or explicitly documented as blocking;
- evidence supports the stage conclusion;
- no file outside the write boundaries above has been changed;
- `python3 "{{fde}}" check {{id}} --repo "{{repo}}"` passes.

Do not proceed to Stage {{next}} if any blocking condition remains. Do not run `fde.py complete` yourself — completion (and any approval) is recorded by a human.

---

## Required Final Response

Write the stage report to `docs/_harness/reports/{{report_name}}` using exactly this template, then run the check command above and fix any failures:

```markdown
{{report_template}}
```

Then return to the user, in this order:

1. Stage status: **PASS / CONDITIONAL PASS / BLOCKED**
2. Key findings
3. Major risks
4. Assumptions / unknowns
5. Artifacts created
6. Blocking issues
7. Recommended next action
