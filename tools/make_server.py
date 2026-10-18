import asyncio
from typing import List
from mcp.server.fastmcp import FastMCP

from .handlers.actors_for import actors_for
from .handlers.attack_paths import attack_paths
from .handlers.blast_radius import blast_radius
from .handlers.chokepoints import chokepoints
from .handlers.detection_gap import detection_gap
from .handlers.record_decision import record_decision

server = FastMCP("cartograph")


@server.tool()
def check_attack_paths(service_id: str, max_hops: int = 6) -> dict:
    return attack_paths(service_id=service_id, max_hops=max_hops)


@server.tool()
def check_blast_radius(service_id: str, max_hops: int = 3) -> dict:
    return blast_radius(service_id=service_id, max_hops=max_hops)


@server.tool()
def check_chokepoints(limit: int = 10) -> dict:
    return chokepoints(limit=limit)


@server.tool()
def check_actors_for(technique_ids: List[str], limit: int = 10) -> dict:
    return actors_for(technique_ids=technique_ids, limit=limit)


@server.tool()
def check_detection_gap(service_id: str, technique_id: str) -> dict:
    return detection_gap(service_id=service_id, technique_id=technique_id)


@server.tool()
def save_decision(
    finding_id: str,
    status: str,
    score: int,
    reason: str,
    evidence_ids: List[str] = None,
) -> dict:
    return record_decision(
        finding_id=finding_id,
        status=status,
        score=score,
        reason=reason,
        evidence_ids=evidence_ids or [],
    )


def make_server():
    return server


if __name__ == "__main__":
    server.run()

