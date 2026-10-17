import json

from agents.state.checker_verdict import CheckerVerdict
from agents.state.score import Score


def make_fixer_prompt(scores: list[Score], verdicts: list[CheckerVerdict]) -> str:
    cases = [
        {
            "score": score,
            "checker_answers": get_answers_for(score["finding_id"], verdicts),
        }
        for score in scores
    ]
    return (
        "You plan fixes for the most dangerous security flaws in a company.\n"
        "Each case has a score from the graph and the answers of three checkers: "
        "route, attackers and logs. The status in the score is final.\n"
        "For every case write one plan with the same finding_id: a one sentence reason "
        "that names the route and the data at risk, and up to three fix steps.\n\n"
        f"Cases:\n{json.dumps(cases, indent=2)}"
    )


def get_answers_for(finding_id: str, verdicts: list[CheckerVerdict]) -> dict:
    return {
        verdict["agent"]: verdict["answer"]
        for verdict in verdicts
        if verdict["finding_id"] == finding_id
    }
