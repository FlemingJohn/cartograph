from agents.nodes.load_scan import load_scan
from agents.nodes.measure_findings import measure_findings
from agents.nodes.score_findings import score_findings
from cartograph_mcp.connection.make_graph_runtime import make_graph_runtime


async def score_scan(scan_id: str) -> dict:
    runtime = make_graph_runtime()
    loaded = await load_scan({"scan_id": scan_id}, runtime)
    measured = await measure_findings(loaded, runtime)
    return {**measured, **score_findings(measured)}
