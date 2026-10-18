import json
from pathlib import Path

from ..connection.get_graph import get_graph


def load_detections():
    graph = get_graph()
    path = Path("vendor/cyber-mcp-tools/data/attack/detections.json")
    with open(path, "r", encoding="utf-8") as f:
        detections = json.load(f)

    batch_size = 100
    for i in range(0, len(detections), batch_size):
        chunk = detections[i : i + batch_size]
        items = [
            {
                "id": d["id"],
                "name": d.get("name", ""),
                "technique_id": d.get("techniqueId", ""),
            }
            for d in chunk
        ]
        graph.query(
            "UNWIND $batch AS item "
            "MERGE (d:Detection {id: item.id}) "
            "SET d.name = item.name",
            {"batch": items},
        )
        graph.query(
            "UNWIND $batch AS item "
            "MATCH (d:Detection {id: item.id}) "
            "MATCH (t:Technique {id: item.technique_id}) "
            "MERGE (d)-[:DETECTS]->(t)",
            {"batch": items},
        )

    log_links = []
    for d in detections:
        for a in d.get("analytics", []):
            for ls in a.get("logSources", []):
                ls_name = ls.get("name", "")
                if "Sysmon" in ls_name:
                    log_links.append({"det_id": d["id"], "log_id": "log-sysmon"})
                elif "Security" in ls_name:
                    log_links.append({"det_id": d["id"], "log_id": "log-security"})
                elif "WebServer" in ls_name or "IIS" in ls_name:
                    log_links.append({"det_id": d["id"], "log_id": "log-web-gateway"})

    deduped_links = [dict(t) for t in {tuple(d.items()) for d in log_links}]
    for i in range(0, len(deduped_links), batch_size):
        chunk = deduped_links[i : i + batch_size]
        graph.query(
            "UNWIND $batch AS item "
            "MATCH (d:Detection {id: item.det_id}) "
            "MATCH (l:LogSource {id: item.log_id}) "
            "MERGE (d)-[:NEEDS_LOG]->(l)",
            {"batch": chunk},
        )

