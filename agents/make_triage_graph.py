from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

from agents.context.app_context import AppContext
from agents.nodes.ask_approval import ask_approval
from agents.nodes.check_attackers import check_attackers
from agents.nodes.check_logs import check_logs
from agents.nodes.check_routes import check_routes
from agents.nodes.load_scan import load_scan
from agents.nodes.measure_findings import measure_findings
from agents.nodes.plan_actions import plan_actions
from agents.nodes.score_findings import score_findings
from agents.nodes.take_actions import take_actions
from agents.nodes.write_report import write_report
from agents.routing.send_shortlist import CHECKERS, send_shortlist
from agents.state.triage_input import TriageInput
from agents.state.triage_output import TriageOutput
from agents.state.triage_state import TriageState

TOOL_RETRY = RetryPolicy(max_attempts=3)
MODEL_RETRY = RetryPolicy(max_attempts=3, initial_interval=5.0, max_interval=30.0)


def make_triage_graph(checkpointer=None):
    builder = StateGraph(
        TriageState,
        input_schema=TriageInput,
        output_schema=TriageOutput,
        context_schema=AppContext,
    )
    builder.add_node(load_scan, retry_policy=TOOL_RETRY)
    builder.add_node(measure_findings, retry_policy=TOOL_RETRY)
    builder.add_node(score_findings)
    builder.add_node(check_routes, retry_policy=MODEL_RETRY)
    builder.add_node(check_attackers, retry_policy=MODEL_RETRY)
    builder.add_node(check_logs, retry_policy=MODEL_RETRY)
    builder.add_node(plan_actions, retry_policy=MODEL_RETRY)
    builder.add_node(ask_approval)
    builder.add_node(take_actions, retry_policy=TOOL_RETRY)
    builder.add_node(write_report)
    builder.add_edge(START, "load_scan")
    builder.add_edge("load_scan", "measure_findings")
    builder.add_edge("measure_findings", "score_findings")
    builder.add_conditional_edges("score_findings", send_shortlist, CHECKERS)
    builder.add_edge(CHECKERS, "plan_actions")
    builder.add_edge("plan_actions", "ask_approval")
    builder.add_edge("take_actions", "write_report")
    builder.add_edge("write_report", END)
    return builder.compile(checkpointer=checkpointer)
