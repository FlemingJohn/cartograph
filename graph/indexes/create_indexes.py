from ..connection.get_graph import get_graph


def create_indexes():
    graph = get_graph()
    indexes = [
        ("Service", "id"),
        ("Library", "id"),
        ("DataStore", "id"),
        ("LogSource", "id"),
        ("Finding", "id"),
        ("Finding", "scan_id"),
        ("Scan", "id"),
        ("Technique", "id"),
        ("Actor", "id"),
        ("Mitigation", "id"),
        ("Detection", "id"),
        ("TriageDecision", "id"),
    ]
    for label, field in indexes:
        try:
            graph.query(f"CREATE INDEX FOR (n:{label}) ON (n.{field})")
        except Exception:
            pass

