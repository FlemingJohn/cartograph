import type { Finding } from "../types/Finding";
import type { PlannedAction } from "../types/PlannedAction";
import { PlanItem } from "./PlanItem";

export function ApprovalPanel({ plan, findings }: { plan: PlannedAction[]; findings: Finding[] }) {
  if (plan.length === 0) {
    return <p className="empty-note">The plan shows here once the agents have checked the top flaws.</p>;
  }
  const titleById = new Map(findings.map((finding) => [finding.finding_id, finding.title]));
  return (
    <ol className="plan-list">
      {plan.map((action) => (
        <PlanItem
          key={action.finding_id}
          action={action}
          title={titleById.get(action.finding_id) ?? action.finding_id}
        />
      ))}
    </ol>
  );
}
