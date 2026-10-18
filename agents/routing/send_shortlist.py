from langgraph.types import Send

from agents.state.triage_state import TriageState

CHECKERS = ["check_routes", "check_attackers", "check_logs"]


def send_shortlist(state: TriageState) -> list[Send]:
    measurements = [state["measurements"][finding_id] for finding_id in state["shortlist"]]
    return [Send(checker, {"measurements": measurements}) for checker in CHECKERS]
