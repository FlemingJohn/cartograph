# Connecting the CartoGraph MCP server to a client

The CartoGraph MCP server lets any MCP client, such as Claude Code, Claude
Desktop, Cursor or Antigravity, ask the same questions the dashboard answers:
which flaws to fix first, why, and what route an attacker would take.

It is read-only and makes no model calls. Every answer comes straight from
the FalkorDB graph, so it costs nothing to call and cannot change the map.

---

## The tools

| Tool | Answers |
|---|---|
| `list_scans` | Which scans are in the graph, with their dates and flaw counts |
| `rank_findings` | Every flaw in a scan ranked by the score formula, the top ones in detail, and how many are fix now, watch and accept |
| `explain_finding` | One flaw's rank, score breakdown, route from the internet, nearby data, attacker groups and missing logs |
| `get_decisions` | Triage decisions people approved in the dashboard, newest first |
| `attack_paths` | The shortest route from the internet to a service |
| `blast_radius` | The data stores a service can reach within a few steps |
| `chokepoints` | The services that sit on the most routes |
| `actors_for` | The attacker groups that use given MITRE ATT&CK techniques |
| `detection_gap` | The logs needed to spot a technique that a service does not write |

The last five are Alan's graph tools from `tools/handlers/`. They return
`{result, cypher, path}`, so a client can show the query behind each answer.

Try asking a connected client: *"Rank the flaws in the latest scan and
explain why the payments flaw beats the report generator."*

---

## Before connecting

The server reads the FalkorDB settings from `.env` in the project folder.
Fill in `FALKORDB_HOST`, `FALKORDB_PORT`, `FALKORDB_USERNAME` and
`FALKORDB_PASSWORD`, then install the Python packages once:

    uv sync

Check the server starts on its own:

    uv run python -m cartograph_mcp.serve_stdio

It waits silently for a client. Stop it with Ctrl+C.

---

## The config block

All the clients below use the same `mcpServers` shape, so one block copies
between them. Only the file location differs.

```json
{
  "mcpServers": {
    "cartograph": {
      "command": "C:\\Users\\Immanuel AJ\\Desktop\\cartograph\\.venv\\Scripts\\python.exe",
      "args": ["-m", "cartograph_mcp.serve_stdio"],
      "env": {
        "PYTHONPATH": "C:\\Users\\Immanuel AJ\\Desktop\\cartograph"
      }
    }
  }
}
```

`command` is the Python inside the project's `.venv`, so the client does not
need `uv` on its path. `PYTHONPATH` points at the project folder so Python can
find the packages, and the server finds `.env` on its own.

### Paths

Both paths are absolute and specific to this machine, with doubled
backslashes because JSON escapes them. On another machine, change both to
where the project lives. On macOS or Linux the block becomes:

```json
{
  "mcpServers": {
    "cartograph": {
      "command": "/absolute/path/to/cartograph/.venv/bin/python",
      "args": ["-m", "cartograph_mcp.serve_stdio"],
      "env": { "PYTHONPATH": "/absolute/path/to/cartograph" }
    }
  }
}
```

Relative paths do not work. The client starts the server from its own
working folder, not from the project.

---

## Claude Code

Project scope, committed with the repo as `.mcp.json`. Claude Code asks once
whether to trust it, then starts the server with the session.

Or add it from the terminal without editing a file:

    claude mcp add cartograph --env PYTHONPATH="C:\Users\Immanuel AJ\Desktop\cartograph" -- "C:\Users\Immanuel AJ\Desktop\cartograph\.venv\Scripts\python.exe" -m cartograph_mcp.serve_stdio

Check it connected with `/mcp` inside Claude Code.

## Claude Desktop

Global only, no project scope. Paste the same block into
`claude_desktop_config.json` and restart the app:

    Windows   %APPDATA%\Claude\claude_desktop_config.json
    macOS     ~/Library/Application Support/Claude/claude_desktop_config.json

## Cursor

Project scope, committed as `.cursor/mcp.json`. Global lives at
`%USERPROFILE%\.cursor\mcp.json` on Windows or `~/.cursor/mcp.json` elsewhere.
Project config wins over global.

## Antigravity

Workspace scope, committed as `.agents/mcp_config.json`. Global lives at
`~/.gemini/config/mcp_config.json`. In the IDE the same file opens from the
agent side panel under MCP Servers, then Manage MCP Servers, then View raw
config.

---

## Over HTTP

The same server also speaks streamable HTTP, for clients that connect by URL:

    uv run python -m cartograph_mcp.serve_http

It listens on `http://127.0.0.1:8765/mcp`. Set `MCP_HOST` and `MCP_PORT` to
change that. A client then needs only:

```json
{
  "mcpServers": {
    "cartograph": {
      "type": "http",
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

In Claude Code that is one line:

    claude mcp add --transport http cartograph http://127.0.0.1:8765/mcp

### Before exposing it beyond this machine

By default it only listens on this machine. Setting `MCP_HOST=0.0.0.0` or
deploying it opens the graph to anyone with the URL. There is no sign-in, and
the graph describes the company's systems, its weak points and the routes
into them. Put it behind authentication before sharing a public URL.

---

## How it is built

    cartograph_mcp/make_server.py          builds the server and registers the nine tools
      ├─ cartograph_mcp/serve_stdio.py     for local clients
      └─ cartograph_mcp/serve_http.py      for clients that connect by URL

    cartograph_mcp/triage/                 list_scans, rank_findings, explain_finding, get_decisions
    cartograph_mcp/connection/             Alan's handlers wrapped as tools the agent code can call
    cartograph_mcp/tool_descriptions.py    what each tool tells the client it does

`rank_findings` and `explain_finding` run the agents' own `load_scan`,
`measure_findings` and `score_findings` steps, so their answers always match
the dashboard. A full ranking of 214 flaws takes about 5 seconds.

---

## Checking it works

Without a client, the MCP Inspector drives the server directly:

    npx @modelcontextprotocol/inspector "C:\Users\Immanuel AJ\Desktop\cartograph\.venv\Scripts\python.exe" -m cartograph_mcp.serve_stdio

It opens in a browser, lists the nine tools and lets you call each one.
Run it from the project folder so the server finds the packages.
