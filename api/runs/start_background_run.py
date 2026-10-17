import asyncio
from typing import Any

from api.runs.run_triage import run_triage
from api.services.app_services import AppServices


def start_background_run(services: AppServices, scan_id: str, graph_input: Any) -> None:
    task = asyncio.create_task(run_triage(services, scan_id, graph_input))
    services.running_tasks.add(task)
    task.add_done_callback(services.running_tasks.discard)
