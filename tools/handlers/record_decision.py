from datetime import datetime, timezone
from typing import List
import uuid

from graph.connection.get_graph import get_graph
from ..queries.record_decision_query import record_decision_query
from ..types.tool_result import ToolResult


def record_decision(
    finding_id: str,
    status: str,
    score: int,
    reason: str,
    evidence_ids: List[str] = None,
) -> dict:
    graph = get_graph()
    decision_id = f"dec-{uuid.uuid4().hex[:8]}"
    decided_at = datetime.now(timezone.utc).isoformat()
    cypher = record_decision_query()

    graph.query(
        cypher,
        {
            "finding_id": finding_id,
            "decision_id": decision_id,
            "status": status,
            "score": score,
            "reason": reason,
            "decided_at": decided_at,
        },
    )

    result = {
        "decision_id": decision_id,
    }
    return ToolResult(result=result, cypher=cypher, path=[]).to_dict()

