from langchain_core.tools import tool

from agents.fakes.fake_service_ids import FAKE_SERVICE_IDS
from agents.state.tool_result import ToolResult

DETECTION_GAP_CYPHER = (
    "MATCH (:Technique {id: $technique_id})<-[:DETECTS]-(:Detection)-[:NEEDS_LOG]->(l:LogSource) "
    "OPTIONAL MATCH (:Service {id: $service_id})-[w:WRITES]->(l) "
    "RETURN l.id, w IS NOT NULL"
)
NEEDED_LOGS = ["web-request-logs", "process-logs"]


@tool("detection_gap")
def fake_detection_gap(service_id: str, technique_id: str) -> ToolResult:
    """Compare the logs needed to spot an attack method with the logs a service writes."""
    written_logs = get_written_logs(service_id)
    missing_logs = [log for log in NEEDED_LOGS if log not in written_logs]
    return {
        "result": {
            "needed_logs": NEEDED_LOGS,
            "written_logs": written_logs,
            "missing_logs": missing_logs,
        },
        "cypher": DETECTION_GAP_CYPHER,
        "path": [service_id, technique_id],
    }


def get_written_logs(service_id: str) -> list[str]:
    is_payments = service_id == "payments-service"
    is_fully_logged = FAKE_SERVICE_IDS.index(service_id) % 2 == 1 and not is_payments
    return NEEDED_LOGS if is_fully_logged else NEEDED_LOGS[:1]
