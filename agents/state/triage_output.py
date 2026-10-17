from typing import TypedDict

from agents.state.ranked_finding import RankedFinding


class TriageOutput(TypedDict):
    ranked_findings: list[RankedFinding]
    report: str
