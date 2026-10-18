from agents.prompts.describe_measurements import describe_measurements
from agents.state.measurement import Measurement


def make_logs_checker_prompt(measurements: list[Measurement]) -> str:
    facts = describe_measurements(measurements, ["detection_gap"])
    return (
        "You check whether the security team would notice an attack through each flaw.\n"
        "Use only the graph facts below. Compare the logs each detection needs with the logs "
        "the service writes, and name the missing ones.\n"
        "Return exactly one verdict per finding, with its finding_id.\n\n"
        f"Graph facts:\n{facts}"
    )
