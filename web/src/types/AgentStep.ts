import type { AgentStepKind } from "./AgentStepKind";

export interface AgentStep {
  scan_id: string;
  node: string;
  kind: AgentStepKind;
  finding_id: string | null;
  message: string;
  at: string;
}
