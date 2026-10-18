from typing import List

from graph.connection.get_graph import get_graph
from ..queries.actors_for_query import actors_for_query
from ..types.tool_result import ToolResult


def actors_for(technique_ids: List[str], limit: int = 10) -> dict:
    graph = get_graph()
    cypher = actors_for_query(limit)
    res = graph.query(cypher, {"technique_ids": technique_ids})

    actor_count = 0
    actors = []

    if res.result_set and res.result_set[0][0] is not None:
        actor_count = res.result_set[0][0]
        raw_actors = res.result_set[0][1] or []
        for a in raw_actors:
            actors.append({"id": a["id"], "name": a["name"]})

    result = {
        "actor_count": actor_count,
        "actors": actors,
    }
    return ToolResult(result=result, cypher=cypher, path=[]).to_dict()

