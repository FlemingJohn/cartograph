def chokepoints_query(limit=10):
    return (
        f"CALL algo.betweenness({{nodeLabels: ['Service'], relationshipTypes: ['CALLS']}}) "
        f"YIELD node, score "
        f"RETURN node.id AS service_id, score AS betweenness "
        f"ORDER BY betweenness DESC "
        f"LIMIT {limit}"
    )

