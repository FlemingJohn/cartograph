from agents.reporting.describe_score import describe_score
from agents.reporting.rank_findings import rank_findings as rank_scores
from cartograph_mcp.triage.rank_findings import DEFAULT_SCAN_ID
from cartograph_mcp.triage.score_scan import score_scan


async def explain_finding(finding_id: str, scan_id: str = DEFAULT_SCAN_ID) -> dict:
    scanned = await score_scan(scan_id)
    measurement = scanned["measurements"].get(finding_id)
    if measurement is None:
        return {"error": f"No finding {finding_id} in scan {scan_id}"}
    score = scanned["scores"][finding_id]
    ranked_ids = [finding["finding_id"] for finding in rank_scores(scanned["scores"], [])]
    return {
        "finding": measurement["finding"],
        "rank": ranked_ids.index(finding_id) + 1,
        "of": len(ranked_ids),
        "score": score["total"],
        "status": score["status"],
        "score_parts": score["parts"],
        "summary": describe_score(score),
        "route_from_internet": measurement["attack_paths"]["path"],
        "data_stores_nearby": measurement["blast_radius"]["result"],
        "attacker_groups": measurement["actors_for"]["result"],
        "log_gaps": [gap["result"] for gap in measurement["detection_gap"]],
    }
