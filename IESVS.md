# Iesvs: agents and app

You build everything the agent **thinks** and **shows**: the LangGraph
agents, the backend and the dashboard.

Your folders: `agents/`, `api/`, `web/`, `tests/agents/`, `tests/api/`.
Do not edit `graph/` or `tools/`. Those are Alan's.

---

## Setup

    git clone --recurse-submodules <repo url>
    cd cartograph
    cp .env.example .env
    uv sync

Put the shared Gemini key in `.env`. The model is set by `MODEL_NAME`,
default `gemini-3.8-flash`.

Read `langgraph.md` before writing any graph code.

---

## How a run works

Facts come from the graph, judgment from the model.

    load_scan            load the 214 flaws
    measure_findings     call Alan's tools directly for every flaw, no model
    score_findings       score formula, no model, keep the top 20
    send_each_finding    send each of the top 20 to the three checkers
      check_routes       model + tools: explains reachability and nearby data
      check_attackers    model + tools: links missing attack methods, names groups
      check_logs         model + tools: explains what we could not spot
    plan_actions         model: verdict and fix plan per flaw
    ask_approval         pause until a person says yes
    take_actions         save decisions, write tickets to the mock list

Add two files the starter structure does not have yet:
`agents/nodes/measure_findings.py` and `agents/scoring/get_score.py`.

---

## Your tasks, in order

Each task has a "done when" line. Do not start the next task until it is
true.

**1. Agree the contracts with Alan**
You write `docs/state-shape.md`, starting from the draft at the bottom of
this file. Alan writes `docs/map-shape.md` and `docs/tool-contracts.md`.
Done when: both of you have read all three and nothing is left open.

**2. Fake tools**
`agents/fakes/` returns fixed answers in exactly the shape of
`docs/tool-contracts.md`. Payments is reachable, two steps from card data,
used by 14 groups, missing logs. The report generator is not reachable.
Done when: each fake returns `{result, cypher, path}`.

**3. Run context**
`agents/context/app_context.py` holds the model, the tool list and the
graph name. Build the model with `ChatGoogleGenerativeAI` from
`langchain-google-genai`, reading `MODEL_NAME`.
Done when: one model call works from code.

**4. Graph skeleton**
State files in `agents/state/`, nodes in `agents/nodes/`, the fan-out in
`agents/routing/send_each_finding.py`, wiring in
`agents/make_triage_graph.py`. Use the fakes.
Done when: a run on the fake scan reaches the end, and the three checkers
run in parallel.

**5. Scoring**
`agents/scoring/get_score.py` and `agents/nodes/score_findings.py`, using
the formula below. No model call.
Done when: payments lands near the top and the report generator lands in
`accept`.

**6. Model answers with a schema**
`agents/schemas/` and `agents/prompts/`. Every model answer uses
`with_structured_output`. No parsing of text by hand.
Done when: each checker returns its schema for payments.

**7. Approval pause and save points**
`agents/nodes/ask_approval.py` uses `interrupt()`. Compile with
`FalkorDBSaver` from `langchain-falkordb`. Thread id is the scan id.
Done when: a run pauses, the process can stop, and it resumes from the save
point after approval.

**8. Backend**
`api/make_app.py` and `api/routes/`. `stream_run` sends each agent step to
the dashboard as server-sent events.
Done when: `curl` on `stream_run` shows steps arriving live.

**9. Check in with Alan**
Swap `agents/fakes/` for the real tools in `agents/connect_tools.py`, using
`MultiServerMCPClient` with three servers: ours, the FalkorDB MCP server in
read-only mode, and cyber-mcp-tools at `CYBER_MCP_URL`. Run one full triage
end to end. Then delete `agents/fakes/`.

**10. Dashboard**
Set up the web app:

    npm create vite@latest web -- --template react-ts
    cd web
    npm install @falkordb/canvas

Keep the `src/` folders already in the repo. Build the top bar, the side
panel that folds to icons, the summary numbers, the ranked list, the route
map with `@falkordb/canvas`, the reasons panel and the agent activity.
Colours come only from `src/styles/theme.css`: copper and white, sharp
corners.
Done when: a full run shows on the dashboard with the payments route drawn.

**11. Approval and simulation screens**
`ApprovalsScreen.tsx` resumes the run. `SimulationScreen.tsx` calls Alan's
add-link script and reruns.
Done when: both work in the demo order.

**12. Record the demo**
Three minutes, run locally. Follow the demo plan on the team page. Keep
`.env` and the Gemini key off screen. Record more than one take.

**13. Submit together.**

---

## Score formula

    severity points     severity × 3                   up to 30
    reachable           +30 if the internet can reach it
    personal data       +20 within 2 steps, +10 within 3
    attacker groups     +1 per group                   up to 15
    cannot be spotted   +10 if any needed log is missing

    not reachable       score capped at 39
    total               capped at 100

    fix_now   70 and above
    watch     40 to 69
    accept    below 40

## Draft: state shape

`TriageInput`

| Key | Type |
|---|---|
| `scan_id` | text |

`TriageOutput`

| Key | Type |
|---|---|
| `ranked_findings` | list of `{finding_id, score, status, reason}` |
| `report` | text |

`TriageState`, everything inside

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
| `is_approved` | yes or no | replace |
| `ranked_findings` | as in output | replace |
| `report` | text | replace |

`FindingStatus`: `"fix_now"`, `"watch"`, `"accept"`.

`Evidence`: `{finding_id, agent, tool, cypher, path, claim}`.

The model, tools and graph name live in the run context, never in state.

---

## Rules

- Follow `CLAUDE.md` and `langgraph.md`: one thing per file, no comments,
  plain names, short functions, routing with `Command` instead of `if`
  chains.
- One file per commit, subject line only, for example
  `feat: add the score formula`.
- Never commit `.env`.
- If you need a tool to return something new, ask Alan to change the
  contract first.
