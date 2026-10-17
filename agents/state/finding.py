from typing import TypedDict


class Finding(TypedDict):
    finding_id: str
    title: str
    severity: float
    service_id: str
    technique_ids: list[str]
