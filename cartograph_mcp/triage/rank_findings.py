from agents.reporting.rank_findings import rank_findings as rank_scores
from cartograph_mcp.triage.score_scan import score_scan

DEFAULT_SCAN_ID = "scan-2026-10-18-001"


async def rank_findings(scan_id: str = DEFAULT_SCAN_ID, limit: int = 20) -> dict:
    scanned = await score_scan(scan_id)
    ranked = rank_scores(scanned["scores"], [])
    return {
        "scan_id": scan_id,
        "finding_count": len(ranked),
        "status_counts": count_statuses(ranked),
        "top_findings": [
            {**finding, **describe_finding(scanned, finding["finding_id"]), "rank": position + 1}
            for position, finding in enumerate(ranked[:limit])
        ],
    }


def describe_finding(scanned: dict, finding_id: str) -> dict:
    finding = scanned["measurements"][finding_id]["finding"]
    return {"title": finding["title"], "service_id": finding["service_id"]}


def count_statuses(ranked: list[dict]) -> dict[str, int]:
    statuses = [finding["status"] for finding in ranked]
    return {status: statuses.count(status) for status in ["fix_now", "watch", "accept"]}
