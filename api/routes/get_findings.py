from fastapi import APIRouter, HTTPException

from api.runs.get_run_status import get_run_status
from api.runs.make_run_configuration import make_run_configuration
from api.services.services_dependency import ServicesDependency
from api.views.make_findings_view import make_findings_view

router = APIRouter()


@router.get("/runs/{scan_id}/findings")
async def get_findings(scan_id: str, services: ServicesDependency) -> dict:
    snapshot = await services.graph.aget_state(make_run_configuration(scan_id))
    if "scores" not in snapshot.values:
        raise HTTPException(status_code=404, detail="No scores for this scan yet")
    return {
        "scan_id": scan_id,
        "run_status": get_run_status(snapshot),
        "findings": make_findings_view(snapshot.values),
        "plan": snapshot.values.get("plan", []),
        "report": snapshot.values.get("report", ""),
    }
