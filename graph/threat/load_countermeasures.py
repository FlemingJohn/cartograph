import json
from pathlib import Path

from ..connection.get_graph import get_graph


def load_countermeasures():
    graph = get_graph()
    path = Path("vendor/cyber-mcp-tools/data/defend/countermeasures.json")
    with open(path, "r", encoding="utf-8") as f:
        countermeasures = json.load(f)

    items = []
    links = []
    seen = set()

    for technique_id, cm_list in countermeasures.items():
        for cm in cm_list:
            name = cm.get("name", "")
            tactic = cm.get("tactic", "")
            if name not in seen:
                seen.add(name)
                items.append({"name": name, "tactic": tactic})
            links.append({"name": name, "technique_id": technique_id})

    batch_size = 100
    for i in range(0, len(items), batch_size):
        chunk = items[i : i + batch_size]
        graph.query(
            "UNWIND $batch AS item "
            "MERGE (c:Countermeasure {name: item.name}) "
            "SET c.tactic = item.tactic",
            {"batch": chunk},
        )

    for i in range(0, len(links), batch_size):
        chunk = links[i : i + batch_size]
        graph.query(
            "UNWIND $batch AS item "
            "MATCH (c:Countermeasure {name: item.name}) "
            "MATCH (t:Technique {id: item.technique_id}) "
            "MERGE (c)-[:COUNTERS]->(t)",
            {"batch": chunk},
        )

