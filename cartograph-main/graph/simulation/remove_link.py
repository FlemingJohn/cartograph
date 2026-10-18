from ..connection.get_graph import get_graph


def remove_link(source_id: str, target_id: str, relationship_type: str = "CALLS"):
    graph = get_graph()
    cypher = (
        f"MATCH (src:Service {{id: $source_id}})-[r:{relationship_type}]->(dst:Service {{id: $target_id}}) "
        f"DELETE r "
        f"RETURN count(r) AS deleted_count"
    )
    res = graph.query(cypher, {"source_id": source_id, "target_id": target_id})
    return res.result_set

