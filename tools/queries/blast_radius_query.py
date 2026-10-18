def blast_radius_query(max_hops=3):
    return (
        f"MATCH (s:Service {{id: $service_id}}), (d:DataStore) "
        f"WITH d, shortestPath((s)-[:CALLS|READS*1..{max_hops}]->(d)) AS p "
        f"WHERE p IS NOT NULL "
        f"RETURN d.id AS data_store_id, d.has_personal_data AS has_personal_data, length(p) AS hop_count"
    )

