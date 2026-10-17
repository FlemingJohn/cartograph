import asyncio

from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.state.evidence import Evidence
from agents.state.planned_action import PlannedAction
from agents.state.triage_state import TriageState
from agents.tickets.write_tickets import write_tickets
from agents.tools.call_tool import call_tool


async def take_actions(state: TriageState, runtime: Runtime[AppContext]) -> dict:
    await asyncio.gather(
        *[record_decision(runtime.context, action, state["evidence"]) for action in state["plan"]]
    )
    urgent_actions = [action for action in state["plan"] if action["status"] == "fix_now"]
    write_tickets(state["scan_id"], urgent_actions)
    return {}


async def record_decision(
    context: AppContext, action: PlannedAction, evidence: list[Evidence]
) -> None:
    evidence_ids = [item["id"] for item in evidence if item["finding_id"] == action["finding_id"]]
    arguments = {
        "finding_id": action["finding_id"],
        "status": action["status"],
        "score": action["score"],
        "reason": action["reason"],
        "evidence_ids": evidence_ids,
    }
    await call_tool(context, "record_decision", arguments)
