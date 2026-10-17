from fastapi import APIRouter

from api.requests.start_run_request import StartRunRequest
from api.runs.start_background_run import start_background_run
from api.services.services_dependency import ServicesDependency

router = APIRouter()


@router.post("/runs")
async def start_run(request: StartRunRequest, services: ServicesDependency) -> dict:
    await services.checkpointer.adelete_thread(request.scan_id)
    await services.run_events.clear(request.scan_id)
    start_background_run(services, request.scan_id, {"scan_id": request.scan_id})
    return {"scan_id": request.scan_id}
