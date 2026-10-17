import json

from agents.state.measurement import Measurement


def make_attacker_checker_prompt(measurement: Measurement) -> str:
    facts = {
        "finding": measurement["finding"],
        "attacker_groups": measurement["actors_for"],
    }
    return (
        "You link a scanner flaw to the MITRE ATT&CK techniques it lets an attacker use.\n"
        "Keep the techniques the scanner already linked. If it linked none, choose the ones "
        "the flaw title points to. Give technique ids only, such as T1190.\n"
        "Then say which attacker groups from the facts use them.\n\n"
        f"Graph facts:\n{json.dumps(facts, indent=2)}"
    )
