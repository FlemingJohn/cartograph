from typing import TypedDict

from agents.state.finding_status import FindingStatus


class PlannedAction(TypedDict):
    finding_id: str
    status: FindingStatus
    score: int
    reason: str
    fix_steps: list[str]
