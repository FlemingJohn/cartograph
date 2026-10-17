from typing import TypedDict

from agents.state.finding_status import FindingStatus


class RankedFinding(TypedDict):
    finding_id: str
    score: int
    status: FindingStatus
    reason: str
