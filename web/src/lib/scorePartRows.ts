import type { ScorePartRow } from "../types/ScorePartRow";

export const scorePartRows: ScorePartRow[] = [
  { part: "severity", label: "Severity", maximum: 30 },
  { part: "reachable", label: "Reachable from the internet", maximum: 30 },
  { part: "personal_data", label: "Close to personal data", maximum: 20 },
  { part: "attacker_groups", label: "Attacker groups", maximum: 15 },
  { part: "cannot_be_spotted", label: "Cannot be spotted", maximum: 10 },
];
