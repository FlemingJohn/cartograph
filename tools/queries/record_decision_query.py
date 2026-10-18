def record_decision_query():
    return (
        "MATCH (f:Finding {id: $finding_id})-[:FOUND_IN]->(s:Scan) "
        "CREATE (d:TriageDecision {id: $decision_id, status: $status, score: $score, reason: $reason, decided_at: $decided_at}) "
        "CREATE (d)-[:ABOUT]->(f) "
        "CREATE (d)-[:IN_SCAN]->(s) "
        "RETURN d.id AS decision_id"
    )

