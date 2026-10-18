import asyncio

from graph.connection.get_graph import get_graph

GET_DECISIONS_CYPHER = (
    "MATCH (d:TriageDecision)-[:ABOUT]->(f:Finding) "
    "WHERE $finding_id = '' OR f.id = $finding_id "
    "RETURN d.id, f.id, d.status, d.score, d.reason, d.decided_at "
    "ORDER BY d.decided_at DESC LIMIT $limit"
)


async def get_decisions(finding_id: str = "", limit: int = 20) -> list[dict]:
    rows = await asyncio.to_thread(read_rows, finding_id, limit)
    return [make_decision(row) for row in rows]


def read_rows(finding_id: str, limit: int) -> list[list]:
    parameters = {"finding_id": finding_id, "limit": limit}
    return get_graph().ro_query(GET_DECISIONS_CYPHER, parameters).result_set


def make_decision(row: list) -> dict:
    decision_id, finding_id, status, score, reason, decided_at = row
    return {
        "decision_id": decision_id,
        "finding_id": finding_id,
        "status": status,
        "score": score,
        "reason": reason,
        "decided_at": decided_at,
    }
