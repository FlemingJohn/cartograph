import json
from pathlib import Path

from ..connection.get_graph import get_graph


def load_mitigations():
    graph = get_graph()
    path = Path("vendor/cyber-mcp-tools/data/attack/mitigations.json")
    with open(path, "r", encoding="utf-8") as f:
        mitigations = json.load(f)

    batch_size = 100
    for i in range(0, len(mitigations), batch_size):
        chunk = mitigations[i : i + batch_size]
        items = [
            {
                "entry_id": f"{m['id']}_{idx}",
                "id": m["id"],
                "name": m.get("name", ""),
                "technique_id": m.get("techniqueId", ""),
            }
            for idx, m in enumerate(chunk, start=i)
        ]
        graph.query(
            "UNWIND $batch AS item "
            "CREATE (m:Mitigation {id: item.id, entry_id: item.entry_id, name: item.name})",
            {"batch": items},
        )
        graph.query(
            "UNWIND $batch AS item "
            "MATCH (m:Mitigation {entry_id: item.entry_id}) "
            "MATCH (t:Technique {id: item.technique_id}) "
            "MERGE (m)-[:MITIGATES]->(t)",
            {"batch": items},
        )

