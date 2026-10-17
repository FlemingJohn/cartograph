import type { AgentStep } from "../types/AgentStep";

const nodesThatChangeFindings = new Set(["score_findings", "plan_actions", "write_report"]);

export function countFindingsChanges(steps: AgentStep[]): number {
  return steps.filter((step) => nodesThatChangeFindings.has(step.node)).length;
}
