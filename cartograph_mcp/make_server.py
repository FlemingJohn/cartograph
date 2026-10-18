import os

from mcp.server.fastmcp import FastMCP

from cartograph_mcp.tool_descriptions import TOOL_DESCRIPTIONS
from cartograph_mcp.triage.explain_finding import explain_finding
from cartograph_mcp.triage.get_decisions import get_decisions
from cartograph_mcp.triage.list_scans import list_scans
from cartograph_mcp.triage.rank_findings import rank_findings
from tools.handlers.actors_for import actors_for
from tools.handlers.attack_paths import attack_paths
from tools.handlers.blast_radius import blast_radius
from tools.handlers.chokepoints import chokepoints
from tools.handlers.detection_gap import detection_gap

SERVER_TOOLS = [
    list_scans,
    rank_findings,
    explain_finding,
    get_decisions,
    attack_paths,
    blast_radius,
    chokepoints,
    actors_for,
    detection_gap,
]
INSTRUCTIONS = (
    "CartoGraph ranks security flaws by what an attacker can actually reach. "
    "Start with rank_findings for a scan, then explain_finding for any flaw. "
    "Every graph tool returns {result, cypher, path} so the evidence can be checked."
)


def make_server() -> FastMCP:
    server = FastMCP(
        "cartograph",
        instructions=INSTRUCTIONS,
        host=os.environ.get("MCP_HOST", "127.0.0.1"),
        port=int(os.environ.get("MCP_PORT", "8765")),
    )
    for tool in SERVER_TOOLS:
        server.add_tool(tool, name=tool.__name__, description=TOOL_DESCRIPTIONS[tool.__name__])
    return server
