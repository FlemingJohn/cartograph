from ..connection.get_graph import get_graph


def add_link(source_id: str, target_id: str, relationship_type: str = "CALLS"):
    graph = get_graph()
    cypher = (
        f"MATCH (src:Service {{id: $source_id}}), (dst:Service {{id: $target_id}}) "
        f"MERGE (src)-[r:{relationship_type}]->(dst) "
        f"RETURN type(r) AS rel_type"
    )
    res = graph.query(cypher, {"source_id": source_id, "target_id": target_id})
    return res.result_set

