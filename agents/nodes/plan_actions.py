from langgraph.runtime import Runtime

from agents.context.app_context import AppContext
from agents.prompts.make_fixer_prompt import make_fixer_prompt
from agents.schemas.action_plan import ActionPlan
from agents.schemas.action_plans import ActionPlans
from agents.state.planned_action import PlannedAction
from agents.state.score import Score
from agents.state.triage_state import TriageState


async def plan_actions(state: TriageState, runtime: Runtime[AppContext]) -> dict:
    scores = [state["scores"][finding_id] for finding_id in state["shortlist"]]
    model = runtime.context.model.with_structured_output(ActionPlans)
    answer = await model.ainvoke(make_fixer_prompt(scores, state["verdicts"]))
    plans_by_finding = {plan.finding_id: plan for plan in answer.plans}
    return {"plan": [make_planned_action(score, plans_by_finding) for score in scores]}


def make_planned_action(score: Score, plans_by_finding: dict[str, ActionPlan]) -> PlannedAction:
    missing_plan = ActionPlan(finding_id=score["finding_id"], reason="", fix_steps=[])
    plan = plans_by_finding.get(score["finding_id"], missing_plan)
    return {
        "finding_id": score["finding_id"],
        "status": score["status"],
        "score": score["total"],
        "reason": plan.reason,
        "fix_steps": plan.fix_steps,
    }
