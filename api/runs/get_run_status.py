from langgraph.types import StateSnapshot

from api.runs.run_status import RunStatus


def get_run_status(snapshot: StateSnapshot) -> RunStatus:
    if not snapshot.values:
        return "not_started"
    if snapshot.interrupts:
        return "paused"
    return "running" if snapshot.next else "finished"
