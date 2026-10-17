from agents.state.score import Score

OPENING_BY_REACHABLE = {
    True: "Reachable from the internet",
    False: "Not reachable from the internet",
}
PHRASE_BY_PART = {
    "personal_data": "close to personal data",
    "attacker_groups": "used by known attacker groups",
    "cannot_be_spotted": "missing the logs to spot it",
}


def describe_score(score: Score) -> str:
    opening = OPENING_BY_REACHABLE[bool(score["parts"]["reachable"])]
    phrases = [phrase for part, phrase in PHRASE_BY_PART.items() if score["parts"][part]]
    return ", ".join([opening, *phrases])
