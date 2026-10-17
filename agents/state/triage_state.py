from operator import add
from typing import Annotated

from agents.state.checker_verdict import CheckerVerdict
from agents.state.evidence import Evidence
from agents.state.finding import Finding
from agents.state.measurement import Measurement
from agents.state.planned_action import PlannedAction
from agents.state.score import Score
from agents.state.triage_input import TriageInput
from agents.state.triage_output import TriageOutput


class TriageState(TriageInput, TriageOutput, total=False):
    findings: list[Finding]
    measurements: dict[str, Measurement]
    scores: dict[str, Score]
    shortlist: list[str]
    evidence: Annotated[list[Evidence], add]
    verdicts: Annotated[list[CheckerVerdict], add]
    plan: list[PlannedAction]
    is_approved: bool
