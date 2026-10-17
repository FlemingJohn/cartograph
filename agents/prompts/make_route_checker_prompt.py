import json

from agents.state.measurement import Measurement


def make_route_checker_prompt(measurement: Measurement) -> str:
    facts = {
        "finding": measurement["finding"],
        "route_from_internet": measurement["attack_paths"],
        "data_stores_nearby": measurement["blast_radius"],
    }
    return (
        "You check whether an attacker on the internet can reach a security flaw, "
        "and what data they could touch from there.\n"
        "Use only the graph facts below. Do not invent services or routes.\n"
        "Name the services along the route, in order, and the closest store of personal data.\n\n"
        f"Graph facts:\n{json.dumps(facts, indent=2)}"
    )
