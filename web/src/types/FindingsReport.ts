import type { Finding } from "./Finding";
import type { PlannedAction } from "./PlannedAction";
import type { RunStatus } from "./RunStatus";

export interface FindingsReport {
  scan_id: string;
  run_status: RunStatus;
  findings: Finding[];
  plan: PlannedAction[];
  report: string;
}
