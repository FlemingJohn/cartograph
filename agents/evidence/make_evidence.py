from agents.state.evidence import Evidence
from agents.state.tool_result import ToolResult


def make_evidence(
    finding_id: str, agent: str, tool: str, tool_result: ToolResult, claim: str
) -> Evidence:
    return {
        "id": f"{finding_id}:{agent}:{tool}",
        "finding_id": finding_id,
        "agent": agent,
        "tool": tool,
        "cypher": tool_result["cypher"],
        "path": tool_result["path"],
        "claim": claim,
    }
