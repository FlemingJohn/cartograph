from graph.connection.get_graph import get_graph
from ..queries.chokepoints_query import chokepoints_query
from ..types.tool_result import ToolResult


def chokepoints(limit: int = 10) -> dict:
    graph = get_graph()
    cypher = chokepoints_query(limit)
    res = graph.query(cypher)

    results = []
    if res.result_set:
        for row in res.result_set:
            if row[0] is not None:
                results.append(
                    {
                        "service_id": row[0],
                        "betweenness": float(row[1]),
                    }
                )

    return ToolResult(result=results, cypher=cypher, path=[]).to_dict()

