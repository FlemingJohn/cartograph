import asyncio

from fastapi import APIRouter

from api.requests.link_request import LinkRequest
from graph.simulation.remove_link import remove_link as remove_graph_link

router = APIRouter()


@router.delete("/simulations/link")
async def remove_link(request: LinkRequest) -> dict:
    await asyncio.to_thread(remove_graph_link, request.source_id, request.target_id)
    return {"source_id": request.source_id, "target_id": request.target_id, "is_linked": False}
