import json
from pathlib import Path

from ..connection.get_graph import get_graph
from .make_sample_scan import make_sample_scan


def load_scan(scan_file=None):
    if scan_file is None:
        scan_file = Path("data/sample-scan.json")
        if not scan_file.exists():
            make_sample_scan()

    with open(scan_file, "r", encoding="utf-8") as f:
        scan = json.load(f)

    graph = get_graph()

    graph.query(
        "MERGE (s:Scan {id: $id}) "
        "SET s.started_at = $started_at",
        {"id": scan["id"], "started_at": scan["started_at"]},
    )

    batch_size = 50
    flaws = scan["flaws"]

    for i in range(0, len(flaws), batch_size):
        chunk = flaws[i : i + batch_size]
        findings = [
            {
                "id": f["id"],
                "title": f["title"],
                "severity": f["severity"],
                "scan_id": scan["id"],
                "service_id": f["service_id"],
                "lib_id": f["library"]["id"],
                "lib_name": f["library"]["name"],
                "lib_ver": f["library"]["version"],
                "technique_id": f.get("technique_id"),
            }
            for f in chunk
        ]

        graph.query(
            "UNWIND $batch AS item "
            "MERGE (l:Library {id: item.lib_id}) "
            "SET l.name = item.lib_name, l.version = item.lib_ver "
            "WITH item, l "
            "MATCH (svc:Service {id: item.service_id}) "
            "MERGE (svc)-[:USES_LIBRARY]->(l)",
            {"batch": findings},
        )

        graph.query(
            "UNWIND $batch AS item "
            "MERGE (f:Finding {id: item.id}) "
            "SET f.title = item.title, f.severity = item.severity, f.scan_id = item.scan_id "
            "WITH item, f "
            "MATCH (sc:Scan {id: item.scan_id}) "
            "MERGE (f)-[:FOUND_IN]->(sc) "
            "WITH item, f "
            "MATCH (l:Library {id: item.lib_id}) "
            "MERGE (f)-[:AFFECTS]->(l)",
            {"batch": findings},
        )

        tech_items = [f for f in findings if f.get("technique_id")]
        if tech_items:
            graph.query(
                "UNWIND $batch AS item "
                "MATCH (f:Finding {id: item.id}) "
                "MATCH (t:Technique {id: item.technique_id}) "
                "MERGE (f)-[:ENABLES]->(t)",
                {"batch": tech_items},
            )

