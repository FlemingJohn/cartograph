from typing import TypedDict

from api.steps.agent_step_kind import AgentStepKind


class AgentStep(TypedDict):
    scan_id: str
    node: str
    kind: AgentStepKind
    finding_id: str | None
    message: str
    at: str
