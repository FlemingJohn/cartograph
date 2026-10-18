# CartoGraph

Attack path intelligence. CartoGraph ranks security flaws by what an attacker
can actually reach, using a FalkorDB graph of your systems, your scanner
findings and MITRE attacker knowledge, and shows the route behind every
decision.

Built for Graph Hacks 2026, Track 1: Agents That Act on Connected Data.

## Setup

    cp .env.example .env
    pip install -e .
    python -m graph.seed_graph

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
