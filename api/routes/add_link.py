import asyncio

from fastapi import APIRouter

from api.requests.link_request import LinkRequest
from graph.simulation.add_link import add_link as add_graph_link

router = APIRouter()


@router.post("/simulations/link")
async def add_link(request: LinkRequest) -> dict:
    await asyncio.to_thread(add_graph_link, request.source_id, request.target_id)
    return {"source_id": request.source_id, "target_id": request.target_id, "is_linked": True}
