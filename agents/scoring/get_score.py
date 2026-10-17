from agents.scoring.get_status import get_status
from agents.state.measurement import Measurement
from agents.state.score import Score
from agents.state.score_parts import ScoreParts

UNREACHABLE_CAP = 39
TOTAL_CAP = 100


def get_score(measurement: Measurement) -> Score:
    parts = get_score_parts(measurement)
    is_reachable = measurement["attack_paths"]["result"]["is_reachable"]
    cap = TOTAL_CAP if is_reachable else UNREACHABLE_CAP
    total = min(round(sum(parts.values())), cap)
    return {
        "finding_id": measurement["finding"]["finding_id"],
        "total": total,
        "status": get_status(total),
        "parts": parts,
    }


def get_score_parts(measurement: Measurement) -> ScoreParts:
    return {
        "severity": round(min(measurement["finding"]["severity"] * 3, 30), 1),
        "reachable": 30 if measurement["attack_paths"]["result"]["is_reachable"] else 0,
        "personal_data": get_personal_data_points(measurement),
        "attacker_groups": min(measurement["actors_for"]["result"]["actor_count"], 15),
        "cannot_be_spotted": 10 if has_missing_logs(measurement) else 0,
    }


def get_personal_data_points(measurement: Measurement) -> int:
    hop_counts = [
        data_store["hop_count"]
        for data_store in measurement["blast_radius"]["result"]
        if data_store["has_personal_data"]
    ]
    nearest = min(hop_counts, default=None)
    points_by_hop_count = {1: 20, 2: 20, 3: 10}
    return points_by_hop_count.get(nearest, 0)


def has_missing_logs(measurement: Measurement) -> bool:
    return any(gap["result"]["missing_logs"] for gap in measurement["detection_gap"])
