def detection_gap_query():
    return (
        "OPTIONAL MATCH (d:Detection)-[:DETECTS]->(t:Technique {id: $technique_id}) "
        "OPTIONAL MATCH (d)-[:NEEDS_LOG]->(needed:LogSource) "
        "WITH collect(DISTINCT needed.id) AS needed_logs "
        "OPTIONAL MATCH (s:Service {id: $service_id})-[:WRITES]->(written:LogSource) "
        "WITH needed_logs, collect(DISTINCT written.id) AS written_logs "
        "RETURN needed_logs, written_logs"
    )

