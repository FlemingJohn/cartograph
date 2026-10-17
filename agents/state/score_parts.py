from typing import TypedDict


class ScoreParts(TypedDict):
    severity: float
    reachable: int
    personal_data: int
    attacker_groups: int
    cannot_be_spotted: int
