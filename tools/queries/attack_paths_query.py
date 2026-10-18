def attack_paths_query(max_hops=6):
    return (
        f"MATCH (i:Internet {{id: 'Internet'}}), (target:Service {{id: $service_id}}) "
        f"WITH shortestPath((i)-[:REACHES|CALLS*1..{max_hops}]->(target)) AS p "
        f"RETURN [n IN nodes(p) | n.id] AS path_nodes, length(p) AS hop_count"
    )

