import type { AgentStep } from "./AgentStep";
import type { RunStatus } from "./RunStatus";

export interface RunStream {
  steps: AgentStep[];
  runStatus: RunStatus;
  startRun: () => Promise<void>;
  answerApproval: (isApproved: boolean) => Promise<void>;
  reportFailure: (error: unknown) => void;
}
