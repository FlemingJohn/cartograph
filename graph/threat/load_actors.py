import json
from pathlib import Path

from ..connection.get_graph import get_graph


def load_actors():
    graph = get_graph()
    path = Path("vendor/cyber-mcp-tools/data/attack/actors.json")
    with open(path, "r", encoding="utf-8") as f:
        actors = json.load(f)

    batch_size = 100
    for i in range(0, len(actors), batch_size):
        chunk = actors[i : i + batch_size]
        items = [
            {
                "id": f"{a['id']}_{idx}",
                "actor_id": a["id"],
                "name": a.get("name", ""),
                "kind": a.get("kind", ""),
            }
            for idx, a in enumerate(chunk, start=i)
        ]
        graph.query(
            "UNWIND $batch AS item "
            "CREATE (a:Actor {id: item.actor_id, entry_id: item.id, name: item.name, kind: item.kind})",
            {"batch": items},
        )

    for i in range(0, len(actors), batch_size):
        chunk = actors[i : i + batch_size]
        links = []
        for idx, a in enumerate(chunk, start=i):
            for tid in a.get("techniqueIds", []):
                links.append({"entry_id": f"{a['id']}_{idx}", "technique_id": tid})
        if links:
            graph.query(
                "UNWIND $batch AS item "
                "MATCH (a:Actor {entry_id: item.entry_id}) "
                "MATCH (t:Technique {id: item.technique_id}) "
                "MERGE (a)-[:USES]->(t)",
                {"batch": links},
            )

