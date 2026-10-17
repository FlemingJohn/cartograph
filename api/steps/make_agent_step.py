from datetime import UTC, datetime

from api.steps.agent_step import AgentStep
from api.steps.agent_step_kind import AgentStepKind
from api.steps.describe_by_node import DESCRIBE_BY_NODE
from api.steps.get_step_finding_id import get_step_finding_id

KIND_BY_NODE: dict[str, AgentStepKind] = {"__interrupt__": "paused"}


def make_agent_step(scan_id: str, node: str, change) -> AgentStep:
    return {
        "scan_id": scan_id,
        "node": node,
        "kind": KIND_BY_NODE.get(node, "step"),
        "finding_id": get_step_finding_id(change),
        "message": DESCRIBE_BY_NODE[node](change),
        "at": datetime.now(UTC).isoformat(),
    }


def make_closing_step(scan_id: str, kind: AgentStepKind, message: str) -> AgentStep:
    return {
        "scan_id": scan_id,
        "node": "run",
        "kind": kind,
        "finding_id": None,
        "message": message,
        "at": datetime.now(UTC).isoformat(),
    }
