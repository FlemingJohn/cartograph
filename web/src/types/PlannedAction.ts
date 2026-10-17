import type { FindingStatus } from "./FindingStatus";

export interface PlannedAction {
  finding_id: string;
  status: FindingStatus;
  score: number;
  reason: string;
  fix_steps: string[];
}
