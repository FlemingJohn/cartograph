# CartoGraph

Attack path intelligence. CartoGraph ranks security flaws by what an attacker
can actually reach, using a FalkorDB graph of your systems, your scanner
findings and MITRE attacker knowledge, and shows the route behind every
decision.

Built for Graph Hacks 2026, Track 1: Agents That Act on Connected Data.

## Setup

    cp .env.example .env
    uv sync

Fill in your FalkorDB Cloud credentials, Google Gemini API key, and Cyber MCP URL
in `.env`.

## Folders

| Folder | Holds |
|---|---|
| `graph/` | Builds the map in FalkorDB |
| `tools/` | Our MCP tool server |
| `agents/` | The LangGraph agents |
| `api/` | Backend the dashboard talks to |
| `web/` | The dashboard |
| `docs/` | Map shape, tool contracts and state shape |
| `vendor/cyber-mcp-tools/` | MITRE ATT&CK and D3FEND data and tools |

## Running the app

Download the MITRE data the seed reads, then rebuild the map. The rebuild
wipes the graph and loads everything again, so it is also the backup.

    git submodule update --init
    uv run python -m graph.seed_graph

Start the backend. It starts the tool server itself.

    uv run uvicorn api.make_app:app

Start the dashboard in a second terminal and open http://localhost:5180.

    cd web
    npm install
    npm run dev

On networks that re-sign secure traffic, set `UV_SYSTEM_CERTS=1` before the
`uv` commands and `NODE_OPTIONS=--use-system-ca` before the `npm` ones.

## Demo order

1. Press **Try now**, then **Start triage**. The agent steps stream into the
   activity log and the run pauses for approval.
2. Pick the payments flaw to see its route from the internet to card data.
3. Open **Approvals** and approve the plan. Decisions are saved to the graph.
4. Open **Simulation** and press **Link and rerun**. The report generator
   gains a route from the front door and its rank jumps. **Undo the link**
   puts the map back.

## Running the tool server

    python -m tools.make_server

## Running tests

    python -m pytest tests/tools/ -v

## Credits

Attacker knowledge comes from MITRE ATT&CK and MITRE D3FEND, through
[cyber-mcp-tools](https://github.com/FlemingJohn/cyber-mcp-tools). Their
licence notices are in [NOTICE](NOTICE) and travel with any copy of this
project.

ATT&CK and D3FEND are registered trademarks of The MITRE Corporation. This
project is not affiliated with or endorsed by MITRE.
