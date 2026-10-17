import type { FindingStatus } from "./FindingStatus";
import type { ScoreParts } from "./ScoreParts";

export interface Finding {
  finding_id: string;
  title: string;
  severity: number;
  service_id: string;
  score: number;
  status: FindingStatus;
  reason: string;
  parts: ScoreParts;
  is_shortlisted: boolean;
}
