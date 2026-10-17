import json
from collections.abc import AsyncIterator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from api.services.app_services import AppServices
from api.services.services_dependency import ServicesDependency

router = APIRouter()


@router.get("/runs/{scan_id}/stream")
async def stream_run(scan_id: str, services: ServicesDependency):
    return StreamingResponse(
        send_steps(services, scan_id),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"},
    )


async def send_steps(services: AppServices, scan_id: str) -> AsyncIterator[str]:
    async for step in services.run_events.follow(scan_id):
        yield f"data: {json.dumps(step)}\n\n"
