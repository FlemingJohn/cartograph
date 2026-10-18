from agents.prompts.describe_measurements import describe_measurements
from agents.state.measurement import Measurement


def make_route_checker_prompt(measurements: list[Measurement]) -> str:
    facts = describe_measurements(measurements, ["attack_paths", "blast_radius"])
    return (
        "You check whether an attacker on the internet can reach security flaws, "
        "and what data they could touch from there.\n"
        "Use only the graph facts below. Do not invent services or routes.\n"
        "For every finding, name the services along the route in order, or say there is no "
        "route, and name the closest store of personal data.\n"
        "Return exactly one verdict per finding, with its finding_id.\n\n"
        f"Graph facts:\n{facts}"
    )
