from ..connection.get_graph import get_graph
from .make_data_stores import make_data_stores
from .make_log_sources import make_log_sources
from .make_services import make_services
from .make_teams import make_teams


def load_company():
    graph = get_graph()
    teams = make_teams()
    data_stores = make_data_stores()
    services_data = make_services()
    log_data = make_log_sources()

    graph.query(
        "MERGE (i:Internet {id: 'Internet'})"
    )

    graph.query(
        "UNWIND $batch AS item "
        "MERGE (t:Team {id: item.id}) "
        "SET t.name = item.name",
        {"batch": teams},
    )

    graph.query(
        "UNWIND $batch AS item "
        "MERGE (d:DataStore {id: item.id}) "
        "SET d.name = item.name, d.has_personal_data = item.has_personal_data",
        {"batch": data_stores},
    )

    graph.query(
        "UNWIND $batch AS item "
        "MERGE (s:Service {id: item.id}) "
        "SET s.name = item.name, s.is_internal = item.is_internal",
        {"batch": services_data["services"]},
    )

    graph.query(
        "UNWIND $batch AS item "
        "MATCH (t:Team {id: item.team_id}) "
        "MATCH (s:Service {id: item.id}) "
        "MERGE (t)-[:OWNS]->(s)",
        {"batch": services_data["services"]},
    )

    graph.query(
        "UNWIND $batch AS item "
        "MATCH (src:Service {id: item[0]}) "
        "MATCH (dst:Service {id: item[1]}) "
        "MERGE (src)-[:CALLS]->(dst)",
        {"batch": services_data["calls"]},
    )

    graph.query(
        "UNWIND $batch AS item "
        "MATCH (s:Service {id: item[0]}) "
        "MATCH (d:DataStore {id: item[1]}) "
        "MERGE (s)-[:READS]->(d)",
        {"batch": services_data["reads"]},
    )

    graph.query(
        "MATCH (i:Internet {id: 'Internet'}) "
        "MATCH (s:Service {id: 'web-gateway'}) "
        "MERGE (i)-[:REACHES]->(s)"
    )

    graph.query(
        "UNWIND $batch AS item "
        "MERGE (l:LogSource {id: item.id}) "
        "SET l.name = item.name",
        {"batch": log_data["sources"]},
    )

    graph.query(
        "UNWIND $batch AS item "
        "MATCH (s:Service {id: item[0]}) "
        "MATCH (l:LogSource {id: item[1]}) "
        "MERGE (s)-[:WRITES]->(l)",
        {"batch": log_data["writes"]},
    )

