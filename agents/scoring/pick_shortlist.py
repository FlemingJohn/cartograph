from agents.state.score import Score

SHORTLIST_SIZE = 20


def pick_shortlist(scores: dict[str, Score]) -> list[str]:
    ranked = sorted(scores.values(), key=lambda score: score["total"], reverse=True)
    return [score["finding_id"] for score in ranked[:SHORTLIST_SIZE]]
