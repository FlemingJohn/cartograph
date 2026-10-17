from collections import Counter

from agents.reporting.rank_findings import rank_findings
from agents.state.ranked_finding import RankedFinding
from agents.state.triage_output import TriageOutput
from agents.state.triage_state import TriageState


def write_report(state: TriageState) -> TriageOutput:
    ranked_findings = rank_findings(state["scores"], state.get("plan", []))
    return {
        "ranked_findings": ranked_findings,
        "report": make_report_text(state, ranked_findings),
    }


def make_report_text(state: TriageState, ranked_findings: list[RankedFinding]) -> str:
    counts = Counter(finding["status"] for finding in ranked_findings)
    decision = "approved and saved" if state.get("is_approved") else "not approved, nothing saved"
    top_lines = [
        f"{finding['finding_id']} scored {finding['score']}: {finding['reason']}"
        for finding in ranked_findings[:5]
    ]
    return "\n".join(
        [
            f"Scan {state['scan_id']}: {len(ranked_findings)} flaws ranked.",
            f"{counts['fix_now']} fix now, {counts['watch']} watch, {counts['accept']} accept.",
            f"The plan was {decision}.",
            *top_lines,
        ]
    )
