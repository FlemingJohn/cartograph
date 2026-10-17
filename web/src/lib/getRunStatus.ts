import type { AgentStep } from "../types/AgentStep";
import type { RunStatus } from "../types/RunStatus";

const runStatusByStepKind: Record<AgentStep["kind"], RunStatus> = {
  step: "running",
  paused: "paused",
  finished: "finished",
  failed: "failed",
};

export function getRunStatus(steps: AgentStep[]): RunStatus {
  const lastMeaningfulStep = steps.findLast((step) => step.node !== "run" || step.kind !== "step");
  return lastMeaningfulStep ? runStatusByStepKind[lastMeaningfulStep.kind] : "not_started";
}
