from agents.prompts.describe_measurements import describe_measurements
from agents.state.measurement import Measurement


def make_attacker_checker_prompt(measurements: list[Measurement]) -> str:
    facts = describe_measurements(measurements, ["actors_for"])
    return (
        "You link scanner flaws to the MITRE ATT&CK techniques they let an attacker use.\n"
        "Keep the techniques the scanner already linked. If it linked none, choose the ones "
        "the flaw title points to. Give technique ids only, such as T1190.\n"
        "Then say which attacker groups from the facts use them.\n"
        "Return exactly one verdict per finding, with its finding_id.\n\n"
        f"Graph facts:\n{facts}"
    )
