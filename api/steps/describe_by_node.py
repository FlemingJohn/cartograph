from collections.abc import Callable

DESCRIBE_BY_NODE: dict[str, Callable] = {
    "load_scan": lambda change: f"Loaded {len(change['findings'])} flaws from the scan",
    "measure_findings": lambda change: (
        f"Measured {len(change['measurements'])} flaws against the graph"
    ),
    "score_findings": lambda change: (
        f"Scored every flaw and kept the top {len(change['shortlist'])}"
    ),
    "check_routes": lambda change: change["verdicts"][0]["answer"]["explanation"],
    "check_attackers": lambda change: change["verdicts"][0]["answer"]["explanation"],
    "check_logs": lambda change: change["verdicts"][0]["answer"]["explanation"],
    "plan_actions": lambda change: f"Planned fixes for {len(change['plan'])} flaws",
    "__interrupt__": lambda change: "Waiting for a person to approve the plan",
    "ask_approval": lambda change: "Plan approved" if change["is_approved"] else "Plan turned down",
    "take_actions": lambda change: "Saved the decisions and wrote tickets",
    "write_report": lambda change: change["report"].splitlines()[1],
}
