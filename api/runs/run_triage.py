from typing import Any

from api.runs.get_run_status import get_run_status
from api.runs.make_run_configuration import make_run_configuration
from api.services.app_services import AppServices
from api.steps.make_agent_step import make_agent_step, make_closing_step

MESSAGE_LIMIT = 400
CLOSING_STEP_BY_STATUS = {
    "finished": ("finished", "Run finished"),
    "paused": ("step", "Run paused for approval"),
    "running": ("step", "Run stopped early"),
    "not_started": ("failed", "Run did not start"),
}


async def run_triage(services: AppServices, scan_id: str, graph_input: Any) -> None:
    try:
        await stream_steps(services, scan_id, graph_input)
    except Exception as error:
        await services.run_events.add(
            make_closing_step(scan_id, "failed", str(error)[:MESSAGE_LIMIT])
        )
        raise


async def stream_steps(services: AppServices, scan_id: str, graph_input: Any) -> None:
    configuration = make_run_configuration(scan_id)
    updates = services.graph.astream(
        graph_input, configuration, context=services.context, stream_mode="updates"
    )
    async for update in updates:
        for node, change in update.items():
            await services.run_events.add(make_agent_step(scan_id, node, change))
    snapshot = await services.graph.aget_state(configuration)
    kind, message = CLOSING_STEP_BY_STATUS[get_run_status(snapshot)]
    await services.run_events.add(make_closing_step(scan_id, kind, message))
