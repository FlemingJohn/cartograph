import asyncio

from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.measuring.make_cached_tool_caller import make_cached_tool_caller
from agents.measuring.measure_finding import measure_finding
from agents.state.triage_state import TriageState


async def measure_findings(state: TriageState, runtime: Runtime[AppContext]) -> dict:
    call_once = make_cached_tool_caller(runtime.context)
    measurements = await asyncio.gather(
        *[measure_finding(call_once, finding) for finding in state["findings"]]
    )
    return {
        "measurements": {
            measurement["finding"]["finding_id"]: measurement for measurement in measurements
        }
    }
