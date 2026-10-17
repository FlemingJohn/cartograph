import { statusLabels } from "../lib/statusLabels";
import type { PlannedAction } from "../types/PlannedAction";
import { StatusChip } from "./StatusChip";

export function PlanItem({ action, title }: { action: PlannedAction; title: string }) {
  return (
    <li className="plan-item">
      <div className="detail-section-plain">
        <span className="activity-node">
          {action.finding_id} · score {action.score}
        </span>
        <h3 className="detail-title">{title}</h3>
        <p className="detail-text">{action.reason}</p>
        <ol className="step-list">
          {action.fix_steps.map((step) => (
            <li key={step}>{step}</li>
          ))}
        </ol>
      </div>
      <StatusChip status={action.status} label={statusLabels[action.status]} />
    </li>
  );
}
