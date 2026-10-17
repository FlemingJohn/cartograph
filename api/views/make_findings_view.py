from agents.reporting.rank_findings import rank_findings
from agents.state.ranked_finding import RankedFinding
from agents.state.triage_state import TriageState


def make_findings_view(values: TriageState) -> list[dict]:
    ranked_findings = values.get("ranked_findings") or rank_findings(
        values.get("scores", {}), values.get("plan", [])
    )
    return [add_finding_details(finding, values) for finding in ranked_findings]


def add_finding_details(finding: RankedFinding, values: TriageState) -> dict:
    measurement = values["measurements"][finding["finding_id"]]
    return {
        **finding,
        "title": measurement["finding"]["title"],
        "severity": measurement["finding"]["severity"],
        "service_id": measurement["finding"]["service_id"],
        "parts": values["scores"][finding["finding_id"]]["parts"],
        "is_shortlisted": finding["finding_id"] in values.get("shortlist", []),
    }
