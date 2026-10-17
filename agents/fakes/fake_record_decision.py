from langchain_core.tools import tool

from agents.state.finding_status import FindingStatus
from agents.state.tool_result import ToolResult

RECORD_DECISION_CYPHER = (
    "MATCH (f:Finding {id: $finding_id})-[:FOUND_IN]->(s:Scan) "
    "CREATE (d:TriageDecision {id: $decision_id, status: $status, score: $score, "
    "reason: $reason, decided_at: timestamp()}) "
    "CREATE (d)-[:ABOUT]->(f), (d)-[:IN_SCAN]->(s)"
)


@tool("record_decision")
def fake_record_decision(
    finding_id: str,
    status: FindingStatus,
    score: int,
    reason: str,
    evidence_ids: list[str],
) -> ToolResult:
    """Save a triage decision linked to the flaw, its evidence and the scan."""
    decision_id = f"D-{finding_id}"
    return {
        "result": {"decision_id": decision_id},
        "cypher": RECORD_DECISION_CYPHER,
        "path": [decision_id, finding_id],
    }
