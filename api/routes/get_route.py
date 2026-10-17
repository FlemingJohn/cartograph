from fastapi import APIRouter, HTTPException

from api.runs.make_run_configuration import make_run_configuration
from api.services.services_dependency import ServicesDependency
from api.views.make_route_view import make_route_view

router = APIRouter()


@router.get("/runs/{scan_id}/findings/{finding_id}/route")
async def get_route(scan_id: str, finding_id: str, services: ServicesDependency) -> dict:
    snapshot = await services.graph.aget_state(make_run_configuration(scan_id))
    if finding_id not in snapshot.values.get("measurements", {}):
        raise HTTPException(status_code=404, detail="No route for this flaw")
    return make_route_view(snapshot.values, finding_id)
