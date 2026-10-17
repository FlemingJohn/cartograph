from typing import TypedDict

from agents.state.finding_status import FindingStatus
from agents.state.score_parts import ScoreParts


class Score(TypedDict):
    finding_id: str
    total: int
    status: FindingStatus
    parts: ScoreParts
