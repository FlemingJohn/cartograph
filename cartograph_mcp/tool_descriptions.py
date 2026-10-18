TOOL_DESCRIPTIONS = {
    "list_scans": "List every vulnerability scan in the graph with its date and number of flaws.",
    "rank_findings": (
        "Rank every flaw in a scan by what an attacker can reach, not by severity alone. "
        "Scores out of 100 from severity, internet reachability, nearby personal data, "
        "attacker groups and missing logs. Returns the top flaws and status counts."
    ),
    "explain_finding": (
        "Explain one flaw: its rank, score breakdown, the route from the internet, the data "
        "stores nearby, the attacker groups using its method and the logs that are missing."
    ),
    "get_decisions": (
        "Read the triage decisions people approved, newest first. "
        "Pass a finding id to see the decisions for one flaw."
    ),
    "attack_paths": "Find the shortest route from the internet to a service, if there is one.",
    "blast_radius": "List the data stores a service can reach within a few steps.",
    "chokepoints": "List the services that sit on the most routes, by betweenness centrality.",
    "actors_for": "Name the attacker groups known to use any of these MITRE ATT&CK techniques.",
    "detection_gap": (
        "Compare the logs needed to spot a technique with the logs a service writes, "
        "and list the missing ones."
    ),
}
