import asyncio

from langchain_core.tools import tool

from agents.state.tool_result import ToolResult
from graph.connection.get_graph import get_graph

LIST_FINDINGS_CYPHER = (
    "MATCH (f:Finding {scan_id: $scan_id}) "
    "OPTIONAL MATCH (f)-[:ENABLES]->(t:Technique) "
    "RETURN f.id, f.title, f.severity, f.service_id, collect(t.id) "
    "ORDER BY f.id"
)


@tool("list_findings")
async def list_findings(scan_id: str) -> ToolResult:
    """List every flaw in a scan with the service it sits in and its attack methods."""
    rows = await asyncio.to_thread(read_finding_rows, scan_id)
    return {
        "result": [make_finding(row) for row in rows],
        "cypher": LIST_FINDINGS_CYPHER,
        "path": [],
    }


def read_finding_rows(scan_id: str) -> list[list]:
    return get_graph().ro_query(LIST_FINDINGS_CYPHER, {"scan_id": scan_id}).result_set


def make_finding(row: list) -> dict:
    finding_id, title, severity, service_id, technique_ids = row
    return {
        "finding_id": finding_id,
        "title": title,
        "severity": severity,
        "service_id": service_id,
        "technique_ids": technique_ids,
    }
