import type { Finding } from "../types/Finding";
import type { ServiceRank } from "../types/ServiceRank";

export function getServiceRank(findings: Finding[], serviceId: string): ServiceRank | null {
  const position = findings.findIndex((finding) => finding.service_id === serviceId);
  return position === -1 ? null : { rank: position + 1, finding: findings[position] };
}
