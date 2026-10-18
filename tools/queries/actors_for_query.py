def actors_for_query(limit=10):
    return (
        f"MATCH (a:Actor)-[:USES]->(t:Technique) "
        f"WHERE t.id IN $technique_ids "
        f"WITH a.id AS actor_id, a.name AS actor_name "
        f"RETURN count(DISTINCT actor_id) AS total_count, "
        f"collect(DISTINCT {{id: actor_id, name: actor_name}})[0..{limit}] AS actors"
    )

