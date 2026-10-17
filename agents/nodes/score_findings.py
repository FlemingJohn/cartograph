from agents.scoring.get_score import get_score
from agents.scoring.pick_shortlist import pick_shortlist
from agents.state.triage_state import TriageState


def score_findings(state: TriageState) -> dict:
    scores = {
        finding_id: get_score(measurement)
        for finding_id, measurement in state["measurements"].items()
    }
    return {"scores": scores, "shortlist": pick_shortlist(scores)}
