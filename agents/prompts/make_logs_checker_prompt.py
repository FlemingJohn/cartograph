import json

from agents.state.measurement import Measurement


def make_logs_checker_prompt(measurement: Measurement) -> str:
    facts = {
        "finding": measurement["finding"],
        "log_coverage": measurement["detection_gap"],
    }
    return (
        "You check whether the security team would notice an attack through this flaw.\n"
        "Use only the graph facts below. Compare the logs each detection needs with the logs "
        "the service writes, and name the missing ones.\n\n"
        f"Graph facts:\n{json.dumps(facts, indent=2)}"
    )
