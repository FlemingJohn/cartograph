from graph.connection.get_graph import get_graph
from ..queries.detection_gap_query import detection_gap_query
from ..types.tool_result import ToolResult


def detection_gap(service_id: str, technique_id: str) -> dict:
    graph = get_graph()
    cypher = detection_gap_query()
    res = graph.query(
        cypher, {"service_id": service_id, "technique_id": technique_id}
    )

    needed_logs = []
    written_logs = []
    if res.result_set:
        needed_logs = res.result_set[0][0] or []
        written_logs = res.result_set[0][1] or []

    needed_set = set(needed_logs)
    written_set = set(written_logs)
    missing_logs = sorted(list(needed_set - written_set))

    result = {
        "needed_logs": sorted(needed_logs),
        "written_logs": sorted(written_logs),
        "missing_logs": missing_logs,
    }
    return ToolResult(result=result, cypher=cypher, path=[]).to_dict()

