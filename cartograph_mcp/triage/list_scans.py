import asyncio

from graph.connection.get_graph import get_graph

LIST_SCANS_CYPHER = (
    "MATCH (s:Scan) OPTIONAL MATCH (f:Finding)-[:FOUND_IN]->(s) "
    "RETURN s.id, s.started_at, count(f) ORDER BY s.started_at DESC"
)


async def list_scans() -> list[dict]:
    rows = await asyncio.to_thread(read_rows)
    return [
        {"scan_id": scan_id, "started_at": started_at, "finding_count": finding_count}
        for scan_id, started_at, finding_count in rows
    ]


def read_rows() -> list[list]:
    return get_graph().ro_query(LIST_SCANS_CYPHER).result_set
