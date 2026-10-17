# State shape

The LangGraph agent state. Callers send `TriageInput` and receive
`TriageOutput`. Everything else stays inside `TriageState`.

---

## TriageInput

| Key | Type |
|---|---|
| `scan_id` | text |

---

## TriageOutput

| Key | Type |
|---|---|
| `ranked_findings` | list of `{finding_id, score, status, reason}` |
| `report` | text |

---

## TriageState

| Key | Type | Reducer |
|---|---|---|
| `scan_id` | text | replace |
| `finding_ids` | list of text | replace |
| `measurements` | map of finding id to graph facts | replace |
| `scores` | map of finding id to `Score` | replace |
| `shortlist` | list of the top 20 finding ids | replace |
| `evidence` | list of `Evidence` | add |
| `verdicts` | list of checker answers | add |
| `plan` | list of planned actions | replace |
| `is_approved` | boolean | replace |
| `ranked_findings` | as in output | replace |
| `report` | text | replace |

---

## FindingStatus

`"fix_now"`, `"watch"`, `"accept"`.

---

## Score

| Key | Type |
|---|---|
| `severity_points` | integer, severity times 3, up to 30 |
| `reachable` | 30 if the internet can reach it, else 0 |
| `personal_data` | 20 within 2 steps, 10 within 3, else 0 |
| `attacker_groups` | 1 per group, up to 15 |
| `cannot_be_spotted` | 10 if any needed log is missing, else 0 |
| `total` | sum capped at 100, capped at 39 if not reachable |
| `status` | `FindingStatus` derived from total |

Thresholds: `fix_now` at 70 and above, `watch` at 40 to 69, `accept`
below 40.

---

## Evidence

| Key | Type |
|---|---|
| `finding_id` | text |
| `agent` | text |
| `tool` | text |
| `cypher` | text |
| `path` | list of text |
| `claim` | text |

---

## Context

The model, tools and graph name live in the run context, never in state.

