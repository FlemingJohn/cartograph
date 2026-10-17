from langchain_core.tools import tool

from agents.fakes.fake_service_ids import FAKE_SERVICE_IDS
from agents.state.tool_result import ToolResult

ATTACK_PATHS_CYPHER = (
    "MATCH p = shortestPath((:Internet)-[:REACHES|CALLS*..6]->(:Service {id: $service_id})) "
    "RETURN p"
)
FIXED_ROUTES = {
    "payments-service": ["internet", "web-gateway", "payments-service"],
    "report-generator": [],
    "web-gateway": ["internet", "web-gateway"],
}


@tool("attack_paths")
def fake_attack_paths(service_id: str, max_hops: int = 6) -> ToolResult:
    """Find the shortest route from the internet to a service."""
    path = FIXED_ROUTES.get(service_id) or make_other_route(service_id)
    return {
        "result": {"is_reachable": bool(path), "hop_count": max(len(path) - 1, 0)},
        "cypher": ATTACK_PATHS_CYPHER,
        "path": path,
    }


def make_other_route(service_id: str) -> list[str]:
    is_reachable = FAKE_SERVICE_IDS.index(service_id) % 3 == 0
    return ["internet", "web-gateway", service_id] if is_reachable else []
