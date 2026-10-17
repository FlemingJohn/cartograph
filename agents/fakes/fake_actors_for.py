from langchain_core.tools import tool

from agents.state.tool_result import ToolResult

ACTORS_FOR_CYPHER = (
    "MATCH (a:Actor)-[:USES]->(t:Technique) WHERE t.id IN $technique_ids "
    "RETURN count(DISTINCT a), collect(DISTINCT a)[..$limit]"
)
ACTOR_COUNT_BY_TECHNIQUE = {"T1190": 14, "T1059": 11, "T1078": 9, "T1210": 4, "T1552": 6}


@tool("actors_for")
def fake_actors_for(technique_ids: list[str], limit: int = 10) -> ToolResult:
    """Name the attacker groups known to use any of these attack methods."""
    actor_count = sum(ACTOR_COUNT_BY_TECHNIQUE.get(technique, 2) for technique in technique_ids)
    actors = [{"id": f"G{1000 + number}", "name": f"Group {number}"} for number in range(limit)]
    return {
        "result": {"actor_count": actor_count, "actors": actors[:actor_count]},
        "cypher": ACTORS_FOR_CYPHER,
        "path": technique_ids,
    }
