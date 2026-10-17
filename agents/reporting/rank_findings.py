from agents.reporting.describe_score import describe_score
from agents.state.planned_action import PlannedAction
from agents.state.ranked_finding import RankedFinding
from agents.state.score import Score


def rank_findings(scores: dict[str, Score], plan: list[PlannedAction]) -> list[RankedFinding]:
    reason_by_finding = {action["finding_id"]: action["reason"] for action in plan}
    ranked_scores = sorted(scores.values(), key=lambda score: score["total"], reverse=True)
    return [
        {
            "finding_id": score["finding_id"],
            "score": score["total"],
            "status": score["status"],
            "reason": reason_by_finding.get(score["finding_id"]) or describe_score(score),
        }
        for score in ranked_scores
    ]
