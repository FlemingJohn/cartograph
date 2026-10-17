# Alan: data and tools

You build everything the agent **knows** and **can call**: the map in
FalkorDB Cloud and the MCP tool server that asks it questions.

Your folders: `graph/`, `tools/`, `tests/graph/`, `tests/tools/`.
Do not edit `agents/`, `api/` or `web/`. Those are Iesvs's.

---

## Setup

    git clone --recurse-submodules <repo url>
    cd cartograph
    cp .env.example .env
    uv sync

Fill in the FalkorDB Cloud host, port and password in `.env`. The Gemini
key is shared by the team.

---

## Your tasks, in order

Each task has a "done when" line. Do not start the next task until it is
true.

**1. Agree the contracts with Iesvs**
You write `docs/map-shape.md` and `docs/tool-contracts.md`, starting from
the drafts at the bottom of this file. Iesvs writes `docs/state-shape.md`.
Done when: both of you have read all three and nothing is left open.

**2. Connect to FalkorDB Cloud**
`graph/connection/get_database.py`, `graph/connection/get_graph.py`.
Done when: `RETURN 1` runs against the cloud graph named in `FALKORDB_GRAPH`.

**3. Load the MITRE knowledge**
`graph/threat/load_*.py`, reading `vendor/cyber-mcp-tools/data/`.
Store ids, names, tactics and links only. Long descriptions stay in
cyber-mcp-tools, because the free tier has 100 MB in total.
Done when: counts match 918 techniques, 1,251 actors, 2,017 mitigations,
918 detections, and `GRAPH.MEMORY USAGE` shows well under 50 MB.

**4. Make the company**
`graph/company/make_*.py`, then `load_company.py`. About 30 services.
Use a fixed random seed so every run builds the same company. It must
include:
- `Internet` reaching a front door (`web-gateway`)
- `payments-service` behind the gateway, two steps from `customer-cards`
  (a data store with `has_personal_data: true`)
- `report-generator`, internal, with **no** route from the internet
- log sources per service, with some deliberately missing
- a team that owns each service
Done when: the two demo stories hold in FalkorDB Browser. Payments is
reachable and near card data. The report generator is not reachable.

**5. Make and load a scan**
`graph/scan/make_sample_scan.py` writes `data/sample-scan.json` with 214
flaws, including report generator at severity 9.8 and payments at 6.5.
`graph/scan/load_scan.py` adds them and links each flaw to the library it
affects and to attack methods using a small weakness-to-method table. Flaws
the table does not cover are left without a method link. The agent links
those.
Done when: the scan loads, and payments' flaw links to `T1190`.

**6. One command to rebuild everything**
`graph/indexes/create_indexes.py`, `graph/seed_graph.py`.
Done when: `uv run python -m graph.seed_graph` wipes and rebuilds the whole
map from nothing. The free tier keeps no backups, so this is our backup.

**7. Test the graph functions on Cloud**
Shortest path from `Internet` to a service, and `algo.betweenness` over the
service links.
Done when: both return sensible answers for payments and the report
generator.

**8. Build the six tools**
One query per file in `tools/queries/`, one handler per file in
`tools/handlers/`, the shared result shape in `tools/types/tool_result.py`,
and the server in `tools/make_server.py` using the `mcp` package.
Every tool returns `{result, cypher, path}`.
Done when: each tool answers through the server, and `tests/tools/` has
one test per tool.

**9. Try the tools by hand**

    claude mcp add cartograph -- uv run python -m tools.make_server

Ask Claude Code to call each tool for payments and the report generator.
Done when: the answers match what you see in FalkorDB Browser.

**10. Check in with Iesvs**
Iesvs swaps the fake tools for yours. Run one full triage end to end.

**11. Saving decisions**
`record_decision` writes `(:TriageDecision)` linked to the flaw, the
evidence and the scan.
Done when: a second run sees the first run's decisions.

**12. Simulation**
Add `graph/simulation/add_link.py` and `graph/simulation/remove_link.py`.
The demo connects the report generator to the front door, reruns, and
shows its rank jump.
Done when: adding the link and rerunning moves the report generator up.

**13. README and blog post**
README: setup, how to run, MITRE credits. Blog post for the side prize:
the problem, the graph, one route, what we learned.

**14. Submit together.**

---

## Draft: map shape

Nodes:

| Label | Key fields |
|---|---|
| `Internet` | `id` |
| `Service` | `id`, `name`, `is_internal` |
| `Library` | `id`, `name`, `version` |
| `DataStore` | `id`, `name`, `has_personal_data` |
| `LogSource` | `id`, `name` |
| `Team` | `id`, `name` |
| `Finding` | `id`, `title`, `severity`, `scan_id` |
| `Scan` | `id`, `started_at` |
| `Technique` | `id`, `name`, `tactics` |
| `Actor` | `id`, `name`, `kind` |
| `Mitigation` | `id`, `name` |
| `Detection` | `id`, `name` |
| `Countermeasure` | `name`, `tactic` |
| `TriageDecision` | `id`, `status`, `score`, `reason`, `decided_at` |

Links:

| Link | From → To |
|---|---|
| `REACHES` | `Internet` → `Service` |
| `CALLS` | `Service` → `Service` |
| `READS` | `Service` → `DataStore` |
| `USES_LIBRARY` | `Service` → `Library` |
| `WRITES` | `Service` → `LogSource` |
| `OWNS` | `Team` → `Service` |
| `AFFECTS` | `Finding` → `Library` |
| `FOUND_IN` | `Finding` → `Scan` |
| `ENABLES` | `Finding` → `Technique` |
| `SUBTECHNIQUE_OF` | `Technique` → `Technique` |
| `USES` | `Actor` → `Technique` |
| `MITIGATES` | `Mitigation` → `Technique` |
| `DETECTS` | `Detection` → `Technique` |
| `NEEDS_LOG` | `Detection` → `LogSource` |
| `COUNTERS` | `Countermeasure` → `Technique` |
| `ABOUT` | `TriageDecision` → `Finding` |
| `IN_SCAN` | `TriageDecision` → `Scan` |

## Draft: tool contracts

Every tool returns:

    {
      "result": <the answer>,
      "cypher": "<the query that produced it>",
      "path": [<node ids along the route, empty if none>]
    }

| Tool | Inputs | `result` |
|---|---|---|
| `attack_paths` | `service_id`, `max_hops` = 6 | `{is_reachable, hop_count}` |
| `blast_radius` | `service_id`, `max_hops` = 3 | `[{data_store_id, has_personal_data, hop_count}]` |
| `chokepoints` | `limit` = 10 | `[{service_id, betweenness}]` |
| `actors_for` | `technique_ids`, `limit` = 10 | `{actor_count, actors: [{id, name}]}` |
| `detection_gap` | `service_id`, `technique_id` | `{needed_logs, written_logs, missing_logs}` |
| `record_decision` | `finding_id`, `status`, `score`, `reason`, `evidence_ids` | `{decision_id}` |

---

## Rules

- Follow `CLAUDE.md`: one thing per file, no comments, plain names, short
  functions.
- One file per commit, subject line only, for example
  `feat: add the attack paths query`.
- Never commit `.env`.
- If you change a contract, tell Iesvs before you push.
