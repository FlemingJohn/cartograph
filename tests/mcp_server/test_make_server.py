import asyncio

from cartograph_mcp.make_server import make_server

EXPECTED_TOOLS = {
    "list_scans",
    "rank_findings",
    "explain_finding",
    "get_decisions",
    "attack_paths",
    "blast_radius",
    "chokepoints",
    "actors_for",
    "detection_gap",
}


def test_server_offers_every_tool_with_a_description():
    tools = asyncio.run(make_server().list_tools())
    assert {tool.name for tool in tools} == EXPECTED_TOOLS
    assert all(tool.description for tool in tools)
