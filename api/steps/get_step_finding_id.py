def get_step_finding_id(change) -> str | None:
    verdicts = change.get("verdicts", []) if isinstance(change, dict) else []
    return verdicts[0]["finding_id"] if verdicts else None
