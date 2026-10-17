import json
from pathlib import Path

from agents.state.planned_action import PlannedAction

TICKETS_PATH = Path("data/tickets.jsonl")


def write_tickets(scan_id: str, actions: list[PlannedAction]) -> None:
    TICKETS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TICKETS_PATH.open("a", encoding="utf-8") as tickets:
        tickets.writelines(json.dumps(make_ticket(scan_id, action)) + "\n" for action in actions)


def make_ticket(scan_id: str, action: PlannedAction) -> dict:
    return {
        "ticket_id": f"{scan_id}-{action['finding_id']}",
        "finding_id": action["finding_id"],
        "score": action["score"],
        "title": action["reason"],
        "steps": action["fix_steps"],
    }
