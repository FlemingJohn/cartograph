import type { AgentStep } from "../types/AgentStep";

export function makeFailedStep(scanId: string, error: unknown): AgentStep {
  return {
    scan_id: scanId,
    node: "dashboard",
    kind: "failed",
    finding_id: null,
    message: error instanceof Error ? error.message : String(error),
    at: new Date().toISOString(),
  };
}
