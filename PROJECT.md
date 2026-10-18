# CartoGraph: what is in the project and what was built

CartoGraph ranks security flaws by what an attacker can actually reach. A
scanner reports 214 flaws. Instead of sorting them by severity alone, it asks
a FalkorDB graph of the company: can the internet reach this service, what
personal data sits near it, which attacker groups use the method it opens,
and would we even see the attack in our logs. A Gemini model then explains
the top 20 in plain words and plans fixes, and a person approves before
anything is saved.

The headline example: the report generator flaw has severity 9.8 but nothing
on the internet can reach it, so it ranks near the bottom. The payments flaw
has severity 6.5 but sits three steps from the internet and two from card
data, so it lands in "fix now".

---

## How a run works

    load_scan          read the 214 flaws from the graph
    measure_findings   ask the graph tools about every flaw, no model
    score_findings     score formula, no model, keep the top 20
    check_routes       ┐
    check_attackers    ├ three checkers in parallel, one model call each
    check_logs         ┘
    plan_actions       one model call: reason and fix steps per flaw
    ask_approval       pause until a person approves or turns it down
    take_actions       save each decision to the graph, write tickets
    write_report       rank all 214 and summarise

Facts come from the graph, judgment from the model. A run makes 4 model
calls in total.

### Score formula

| Part | Points |
|---|---|
| Severity | severity × 3, up to 30 |
| Reachable from the internet | +30 |
| Personal data within 2 steps / 3 steps | +20 / +10 |
| Attacker groups using the method | +1 each, up to 15 |
| A needed log is missing | +10 |

Not reachable caps the score at 39. 70 and above is **fix now**, 40 to 69 is
**watch**, below 40 is **accept**.

---

## What is in each folder

| Folder | Owner | Holds |
|---|---|---|
| `graph/` | Alan | Builds the company map, MITRE data and the scan in FalkorDB. `seed_graph.py` rebuilds everything. `simulation/` adds or removes a link. |
| `tools/` | Alan | The MCP tool server with the six tools: `attack_paths`, `blast_radius`, `chokepoints`, `actors_for`, `detection_gap`, `record_decision`. |
| `agents/` | Iesvs | The LangGraph triage graph: state, nodes, prompts, schemas, scoring, the tool connection and the run context. |
| `api/` | Iesvs | FastAPI backend: start a run, stream its steps, approve, read findings and routes, add or remove the simulation link. |
| `web/` | Iesvs | React dashboard: intro, dashboard, approvals and simulation screens. |
| `docs/` | both | Map shape, tool contracts and state shape. |
| `data/` | Alan | The sample scan of 214 flaws. |
| `tests/` | both | Tool tests against FalkorDB, score tests. |
| `vendor/cyber-mcp-tools/` | outside | MITRE ATT&CK and D3FEND data the seed reads. |

### The backend routes

| Route | Does |
|---|---|
| `POST /runs` | Start a fresh triage for a scan |
| `GET /runs/{scan_id}/stream` | Server-sent events, one per agent step |
| `POST /runs/{scan_id}/approve` | Resume a paused run with yes or no |
| `GET /runs/{scan_id}/findings` | Ranked findings, the plan and the report |
| `GET /runs/{scan_id}/findings/{finding_id}/route` | Route, evidence and plan for one flaw |
| `POST` / `DELETE /simulations/link` | Link or unlink the front door and the report generator |

### The dashboard

- **Intro**: a 1 to 100 % counter, then "CartoGraph" in particles that scatter
  from the cursor over a moving blue gradient, and a "Try now" button.
- **Dashboard**: headline, summary boxes, ranked list, the attack route drawn
  with `@falkordb/canvas`, the reasons panel with the score breakdown and the
  Cypher behind each claim, and the live agent activity.
- **Approvals**: the 20 planned fixes with approve and turn down.
- **Simulation**: link the front door to the report generator, rerun, and
  see its rank before and after.
- A magnetic dock at the bottom centre switches screens. White and blue
  theme, DM Sans throughout.

---

## What I built and changed

### Agents and backend (tasks 1 to 9)

- Wrote the state shape, the triage graph, scoring, schemas, prompts, the
  approval pause and the FalkorDB save points.
- Built the backend with live step streaming.
- Built fakes first, then swapped them for Alan's real tools over MCP and
  deleted the fakes.

### Dashboard (tasks 10 and 11)

- Built every screen above, went through a dark theme, then the white and
  blue theme you chose.
- Added the intro, the particle title, the gradient background, the dock and
  the start animation.
- Built the simulation screen on Alan's link scripts.

### Bringing in Alan's work today

- **Moved his work into place.** He pushed everything inside a nested
  `cartograph-main/` folder, so the real `graph/` and `tools/` were still
  empty. I moved his files to the top level unchanged and removed the stale
  duplicates.
- **Fixed the rebuild command.** `graph/seed_graph.py` could not run because
  its imports reached outside the package.
- **Stored each flaw's service.** The scan loader now saves `service_id` on
  each Finding, so a flaw is measured against its own service instead of
  every service that shares its library. I updated the live graph in place
  by rerunning his loader, without wiping anything.
- **Made the tools fast.** Every tool call opened a new connection to
  FalkorDB Cloud. Reusing one connection took measuring all 214 flaws from
  41 seconds to under 3.
- **Mapped his tool names** (`check_attack_paths` and so on) to the contract
  names, and kept one tool session open for the backend's lifetime.
- **Added the missing scan reader.** None of the six tools can list a scan's
  flaws, so `agents/tools/list_findings.py` runs one read-only query.

### Fitting the Gemini free tier

The free tier allows **20 requests per model per day**. The first design sent
each of the top 20 flaws to three checkers separately, which is 61 calls per
run and spent a whole day's quota in one go. Each checker now answers for all
20 flaws in one call, so a run makes **4 calls**. The answers are still per
flaw, because each schema returns a list keyed by finding id.

### Things that went wrong and how they were fixed

| Problem | Cause | Fix |
|---|---|---|
| "Bad request" on Start triage | The backend running was yesterday's code, which only accepted the old dashboard port | Restart the backend. The dashboard now explains this in the activity log instead of failing silently. |
| Triage hung on Gemini | This network re-signs secure traffic, which Python did not trust | `truststore` makes Python use the Windows certificates |
| Gemini quota used up | 61 calls per run against a 20 per day limit | Batched checkers, 4 calls per run |
| Moving gradient stood still | The shader material kept its own copy of the time value | Update the time on the material itself |
| Backend started without a database | Missing FalkorDB settings only failed mid-run | The backend now refuses to start and names the missing settings |

---

## Checked end to end on 18 October

A full run in the browser against Alan's FalkorDB Cloud graph and real Gemini:

| Step | Result |
|---|---|
| Start triage to the approval pause | 96 seconds, 9 agent steps |
| Measuring all 214 flaws | under 3 seconds, 92 tool calls |
| Ranking | 74 fix now, 99 watch, 41 accept |
| Payments flaw (severity 6.5) | score 94, fix now, route Internet → web-gateway → checkout-service → payments-service, two steps from customer-cards |
| Report generator flaw (severity 9.8) | score 39, accept, rank 185, no route from the internet |
| Approve | decisions saved to the graph as `TriageDecision` nodes |
| Simulation: link and rerun | report generator jumps from #185 to #18, score 84, fix now |
| Undo the link | back to #185, and the link is gone from the graph |

Tests: 6 tool tests against the cloud graph and 3 score tests all pass.

---

## How to run it

1. Fill `.env` with the FalkorDB host, port, username and password, a Gemini
   key and `MODEL_NAME`. Keep keys in `.env` only, never `.env.example`.
2. Start the backend:

       uv run uvicorn api.make_app:app

3. Start the dashboard in a second terminal and open http://localhost:5180:

       cd web
       npm run dev

4. Demo order: **Try now** → **Start triage** → pick the payments flaw →
   **Approvals** → **Approve plan** → **Simulation** → **Link and rerun** →
   **Undo the link**.

To rebuild the whole graph from nothing, run `git submodule update --init`
then `uv run python -m graph.seed_graph`. This wipes the shared graph, so
check with Alan first.

### Gemini quota for recording

Each run uses 4 calls, and the simulation rerun is another run, so one full
demo take uses about 8. With 20 per model per day, that is two takes per
model. Every model has its own quota, so switch `MODEL_NAME` between
`gemini-3.5-flash`, `gemini-3-flash-preview` and `gemini-3.8-flash` (after
its quota resets) to get more takes.

Left on your key today, after testing: about 15 calls on `gemini-3.5-flash`
(set in `.env` now), about 7 on `gemini-3-flash-preview`, none on
`gemini-3.8-flash` until its quota resets on 19 October. Alan's key is a
separate project with its own full quota if you need more takes.

---

## Still to do

- Record the demo, three minutes, more than one take (task 12).
- Submit together with Alan by 11 PM (task 13).
- Rotate the FalkorDB password and Gemini keys after the hackathon. They were
  shared in chat.
