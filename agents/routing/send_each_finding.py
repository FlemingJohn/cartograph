from langgraph.types import Send

from agents.state.triage_state import TriageState

CHECKERS = ["check_routes", "check_attackers", "check_logs"]


def send_each_finding(state: TriageState) -> list[Send]:
    return [
        Send(checker, {"measurement": state["measurements"][finding_id]})
        for finding_id in state["shortlist"]
        for checker in CHECKERS
    ]
