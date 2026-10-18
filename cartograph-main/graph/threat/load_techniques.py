import json
from pathlib import Path

from ..connection.get_graph import get_graph


def load_techniques():
    graph = get_graph()
    path = Path("vendor/cyber-mcp-tools/data/attack/techniques.json")
    with open(path, "r", encoding="utf-8") as f:
        techniques = json.load(f)

    batch_size = 100
    for i in range(0, len(techniques), batch_size):
        chunk = techniques[i : i + batch_size]
        items = []
        for t in chunk:
            items.append(
                {
                    "id": t["id"],
                    "name": t.get("name", ""),
                    "tactics": t.get("tactics", []),
                    "parentId": t.get("parentId"),
                }
            )
        graph.query(
            "UNWIND $batch AS item "
            "MERGE (t:Technique {id: item.id}) "
            "SET t.name = item.name, t.tactics = item.tactics",
            {"batch": items},
        )

    for i in range(0, len(techniques), batch_size):
        chunk = techniques[i : i + batch_size]
        sub_items = [
            {"id": t["id"], "parentId": t["parentId"]}
            for t in chunk
            if t.get("isSubtechnique") and t.get("parentId")
        ]
        if sub_items:
            graph.query(
                "UNWIND $batch AS item "
                "MATCH (sub:Technique {id: item.id}) "
                "MATCH (parent:Technique {id: item.parentId}) "
                "MERGE (sub)-[:SUBTECHNIQUE_OF]->(parent)",
                {"batch": sub_items},
            )

