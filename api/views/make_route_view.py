from itertools import pairwise

from agents.state.measurement import Measurement
from agents.state.triage_state import TriageState

INTERNET_ID = "Internet"


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
    data_store_ids = get_data_store_ids(measurement)
    service_nodes = [{"id": node_id, "kind": get_node_kind(node_id)} for node_id in route]
    data_nodes = [{"id": store_id, "kind": "data_store"} for store_id in data_store_ids]
    return service_nodes + data_nodes


def make_route_links(measurement: Measurement) -> list[dict]:
    service_id = measurement["finding"]["service_id"]
    route_links = [
        {"source": source, "target": target}
        for source, target in pairwise(measurement["attack_paths"]["path"])
    ]
    data_links = [
        {"source": service_id, "target": store_id} for store_id in get_data_store_ids(measurement)
    ]
    return route_links + data_links


def get_data_store_ids(measurement: Measurement) -> list[str]:
    return [store["data_store_id"] for store in measurement["blast_radius"]["result"]]


def get_node_kind(node_id: str) -> str:
    return "internet" if node_id == INTERNET_ID else "service"
