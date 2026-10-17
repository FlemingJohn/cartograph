from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.state.triage_input import TriageInput
from agents.tools.call_tool import call_tool


async def load_scan(state: TriageInput, runtime: Runtime[AppContext]) -> dict:
    scan = await call_tool(runtime.context, "list_findings", {"scan_id": state["scan_id"]})
    return {"findings": scan["result"]}
