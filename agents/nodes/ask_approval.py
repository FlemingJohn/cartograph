from typing import Literal

from langgraph.types import Command, interrupt

from agents.state.triage_state import TriageState

NEXT_STEP_BY_APPROVAL = {True: "take_actions", False: "write_report"}


def ask_approval(state: TriageState) -> Command[Literal["take_actions", "write_report"]]:
    answer = interrupt({"scan_id": state["scan_id"], "plan": state["plan"]})
    is_approved = bool(answer["is_approved"])
    return Command(update={"is_approved": is_approved}, goto=NEXT_STEP_BY_APPROVAL[is_approved])
