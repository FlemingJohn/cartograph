from graph.connection.get_graph import get_graph
from ..queries.blast_radius_query import blast_radius_query
from ..types.tool_result import ToolResult


def blast_radius(service_id: str, max_hops: int = 3) -> dict:
    graph = get_graph()
    cypher = blast_radius_query(max_hops)
    res = graph.query(cypher, {"service_id": service_id})

    results = []
    if res.result_set:
        for row in res.result_set:
            if row[0] is not None:
                results.append(
                    {
                        "data_store_id": row[0],
                        "has_personal_data": row[1],
                        "hop_count": row[2],
                    }
                )

    return ToolResult(result=results, cypher=cypher, path=[]).to_dict()

