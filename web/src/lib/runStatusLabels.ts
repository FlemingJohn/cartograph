import type { RunStatus } from "../types/RunStatus";

export const runStatusLabels: Record<RunStatus, string> = {
  not_started: "No run yet",
  running: "Running",
  paused: "Waiting for approval",
  finished: "Finished",
  failed: "Failed",
};
