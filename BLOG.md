# CartoGraph: Why CVSS Scores Lie and Graphs Tell the Truth

Security teams drown in vulnerability scanner alerts. A traditional scanner looks at a machine or container, finds a vulnerable package, and stamps it with a CVSS severity score. A CVSS 9.8 critical vulnerability sounds terrifying on paper, triggering emergency weekend pages and hasty deployments. But what if that vulnerable service sits isolated in a private VPC, unreachable from the public internet? Meanwhile, a moderate CVSS 6.5 flaw in your checkout flow might sit three hops away from your plaintext credit card database, reachable directly through your public web gateway.

This fundamental disconnect is why we built **CartoGraph** for Graph Hacks 2026.

## The Core Idea: Attack Path Intelligence

CartoGraph ranks security flaws not by isolated vulnerability metrics, but by **what an adversary can actually reach and execute**. We model infrastructure, threat intelligence, and vulnerability scan data together inside **FalkorDB**:

1. **Topology & Connectivity**: Services, public entry points (`Internet`), inter-service RPC (`CALLS`), and backend databases (`READS`).
2. **Threat Intelligence**: Over 900 ATT&CK techniques, 1,200+ threat actors, 2,000+ mitigations, and D3FEND countermeasures.
3. **Detection Telemetry**: Which services write to which log sources, and what logs each technique requires for detection.
4. **Vulnerability Scans**: Flaws discovered on services, linked to specific libraries and the ATT&CK techniques they enable.

## The Power of the Graph

By uniting these four domains into a single graph in FalkorDB Cloud, answering critical security questions becomes a matter of graph algorithms:

- **Reachability & Route Verification**: Running `shortestPath((Internet)-[:REACHES|CALLS*]->(Target))` tells us within milliseconds if a service is exposed to the outside world and provides the exact route an attacker would traverse.
- **Blast Radius Analysis**: Finding which `DataStore` nodes with `has_personal_data: true` lie within 2–3 hops of a compromised service.
- **Chokepoint Identification**: Running betweenness centrality (`algo.betweenness`) over service call graphs highlights architectural bottlenecks that require extra defensive hardening.
- **Detection Gap Auditing**: Comparing the log sources required by an attack technique against the logs actually produced by the vulnerable service reveals blind spots before an incident occurs.

## The Agent & MCP Architecture

Rather than forcing security analysts to write Cypher queries, CartoGraph exposes six targeted tools via the **Model Context Protocol (MCP)**:
`attack_paths`, `blast_radius`, `chokepoints`, `actors_for`, `detection_gap`, and `record_decision`.

A LangGraph agent calls these tools to inspect top vulnerabilities, calculate contextual risk scores, and assemble defensible remediation plans—complete with graph paths and Cypher evidence behind every recommendation.

When infrastructure changes—such as an engineer mistakenly opening an internal reporting service to the public gateway—CartoGraph simulations instantly reflect the new attack paths, reprioritizing flaws in real time.

