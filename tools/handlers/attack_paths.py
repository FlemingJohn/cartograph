from graph.connection.get_graph import get_graph
from ..queries.attack_paths_query import attack_paths_query
from ..types.tool_result import ToolResult


def attack_paths(service_id: str, max_hops: int = 6) -> dict:
    graph = get_graph()
    cypher = attack_paths_query(max_hops)
    res = graph.query(cypher, {"service_id": service_id})

    path_nodes = []
    hop_count = None
    is_reachable = False

    if res.result_set and res.result_set[0][0] is not None:
        path_nodes = res.result_set[0][0]
        hop_count = res.result_set[0][1]
        is_reachable = True

    result = {
        "is_reachable": is_reachable,
        "hop_count": hop_count,
    }
    return ToolResult(result=result, cypher=cypher, path=path_nodes).to_dict()

