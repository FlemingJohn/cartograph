# State shape

What the triage graph takes in, gives back and keeps inside. Code lives in
`agents/state/`. The model, the tools and the graph name live in the run
context (`agents/context/app_context.py`), never in state.

## `TriageInput`

| Key | Type |
|---|---|
| `scan_id` | text |

The scan id is also the thread id, so a run can pause and resume.

## `TriageOutput`

| Key | Type |
|---|---|
| `ranked_findings` | list of `RankedFinding` |
| `report` | text |

## `TriageState`, everything inside

| Key | Type | Reducer |
|---|---|---|
| `scan_id` | text | replace |
| `findings` | list of `Finding` | replace |
| `measurements` | map of finding id to `Measurement` | replace |
| `scores` | map of finding id to `Score` | replace |
| `shortlist` | list of the top 20 finding ids | replace |
| `evidence` | list of `Evidence` | add |
| `verdicts` | list of `CheckerVerdict` | add |
| `plan` | list of `PlannedAction` | replace |
| `is_approved` | yes or no | replace |
| `ranked_findings` | as in output | replace |
| `report` | text | replace |

Only `evidence` and `verdicts` are written by the three checkers at the same
time, so only they need a reducer.

## Pieces

`FindingStatus`: `"fix_now"`, `"watch"`, `"accept"`.

`Finding`: `{finding_id, title, severity, service_id, technique_ids}`.
`technique_ids` is empty when the scan's weakness table did not cover the
flaw. The attacker checker links those.

`ToolResult`: `{result, cypher, path}`, exactly as in `tool-contracts.md`.

`Measurement`: graph facts for one flaw, gathered with no model call.

| Key | Type |
|---|---|
| `finding` | `Finding` |
| `attack_paths` | `ToolResult` |
| `blast_radius` | `ToolResult` |
| `actors_for` | `ToolResult` |
| `detection_gap` | list of `ToolResult`, one per technique |

`ScoreParts`: `{severity, reachable, personal_data, attacker_groups,
cannot_be_spotted}`, the points from each line of the score formula.

`Score`: `{finding_id, total, status, parts}`.

`Evidence`: `{id, finding_id, agent, tool, cypher, path, claim}`.
`id` is `<finding_id>:<agent>:<tool>`, and is what `record_decision` takes as
`evidence_ids`.

`CheckerVerdict`: `{finding_id, agent, answer}`. `answer` is the checker's
schema as a map.

`PlannedAction`: `{finding_id, status, score, reason, fix_steps}`.

`RankedFinding`: `{finding_id, score, status, reason}`.

## The approval pause

`ask_approval` stops the run with `interrupt()` and hands out the `plan`.
The run resumes with `Command(resume={"is_approved": true})` or `false`.

## Reading the scan

`load_scan` uses `list_findings`, a read-only query in
`agents/tools/list_findings.py` that returns every `Finding` in the scan with
its `service_id` and linked techniques. It runs on the agent side because the
six server tools have no way to list flaws.
