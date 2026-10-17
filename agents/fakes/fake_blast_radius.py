from langchain_core.tools import tool

from agents.fakes.fake_service_ids import FAKE_SERVICE_IDS
from agents.state.tool_result import ToolResult

BLAST_RADIUS_CYPHER = (
    "MATCH p = (:Service {id: $service_id})-[:CALLS|READS*1..3]->(d:DataStore) "
    "RETURN d.id, d.has_personal_data, length(p)"
)
FIXED_REACH = {
    "payments-service": (
        [{"data_store_id": "customer-cards", "has_personal_data": True, "hop_count": 2}],
        ["payments-service", "card-vault", "customer-cards"],
    ),
    "report-generator": (
        [{"data_store_id": "report-archive", "has_personal_data": False, "hop_count": 1}],
        ["report-generator", "report-archive"],
    ),
}


@tool("blast_radius")
def fake_blast_radius(service_id: str, max_hops: int = 3) -> ToolResult:
    """List the data stores a service can reach within a few steps."""
    data_stores, path = FIXED_REACH.get(service_id) or make_other_reach(service_id)
    return {"result": data_stores, "cypher": BLAST_RADIUS_CYPHER, "path": path}


def make_other_reach(service_id: str) -> tuple[list[dict], list[str]]:
    hop_count = FAKE_SERVICE_IDS.index(service_id) % 4
    data_store = {
        "data_store_id": "customer-profiles",
        "has_personal_data": True,
        "hop_count": hop_count,
    }
    has_data_store = hop_count > 0
    return ([data_store], [service_id, "customer-profiles"]) if has_data_store else ([], [])
