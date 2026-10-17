import asyncio

from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.measuring.measure_finding import measure_finding
from agents.state.triage_state import TriageState


async def measure_findings(state: TriageState, runtime: Runtime[AppContext]) -> dict:
    measurements = await asyncio.gather(
        *[measure_finding(runtime.context, finding) for finding in state["findings"]]
    )
    return {
        "measurements": {
            measurement["finding"]["finding_id"]: measurement for measurement in measurements
        }
    }
