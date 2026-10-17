from itertools import pairwise

from agents.state.measurement import Measurement
from agents.state.triage_state import TriageState

INTERNET_ID = "internet"


def make_route_view(values: TriageState, finding_id: str) -> dict:
    measurement = values["measurements"][finding_id]
    evidence = [item for item in values.get("evidence", []) if item["finding_id"] == finding_id]
    plan = [action for action in values.get("plan", []) if action["finding_id"] == finding_id]
    return {
        "finding_id": finding_id,
        "nodes": make_route_nodes(measurement),
        "links": make_route_links(measurement),
        "evidence": evidence,
        "plan": plan[0] if plan else None,
    }


def make_route_nodes(measurement: Measurement) -> list[dict]:
    route = measurement["attack_paths"]["path"] or [measurement["finding"]["service_id"]]
    data_route = measurement["blast_radius"]["path"]
    data_store_ids = {store["data_store_id"] for store in measurement["blast_radius"]["result"]}
    node_ids = list(dict.fromkeys([*route, *data_route]))
    return [{"id": node_id, "kind": get_node_kind(node_id, data_store_ids)} for node_id in node_ids]


def make_route_links(measurement: Measurement) -> list[dict]:
    paths = [measurement["attack_paths"]["path"], measurement["blast_radius"]["path"]]
    return [
        {"source": source, "target": target} for path in paths for source, target in pairwise(path)
    ]


def get_node_kind(node_id: str, data_store_ids: set[str]) -> str:
    if node_id == INTERNET_ID:
        return "internet"
    return "data_store" if node_id in data_store_ids else "service"
