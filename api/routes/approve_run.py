from fastapi import APIRouter, HTTPException
from langgraph.types import Command

from api.requests.approve_run_request import ApproveRunRequest
from api.runs.get_run_status import get_run_status
from api.runs.make_run_configuration import make_run_configuration
from api.runs.start_background_run import start_background_run
from api.services.services_dependency import ServicesDependency

router = APIRouter()


@router.post("/runs/{scan_id}/approve")
async def approve_run(
    scan_id: str, request: ApproveRunRequest, services: ServicesDependency
) -> dict:
    snapshot = await services.graph.aget_state(make_run_configuration(scan_id))
    if get_run_status(snapshot) != "paused":
        raise HTTPException(status_code=409, detail="This run is not waiting for approval")
    answer = Command(resume={"is_approved": request.is_approved})
    start_background_run(services, scan_id, answer)
    return {"scan_id": scan_id, "is_approved": request.is_approved}
