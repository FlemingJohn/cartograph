from langchain_core.tools import tool

from agents.fakes.fake_findings import make_fake_findings
from agents.state.tool_result import ToolResult

LIST_FINDINGS_CYPHER = (
    "MATCH (f:Finding {scan_id: $scan_id})-[:AFFECTS]->(:Library)<-[:USES_LIBRARY]-(s:Service) "
    "OPTIONAL MATCH (f)-[:ENABLES]->(t:Technique) "
    "RETURN f.id, f.title, f.severity, s.id, collect(t.id)"
)


@tool("list_findings")
def fake_list_findings(scan_id: str) -> ToolResult:
    """List every flaw in a scan with the service it sits in and its attack methods."""
    return {"result": make_fake_findings(scan_id), "cypher": LIST_FINDINGS_CYPHER, "path": []}
