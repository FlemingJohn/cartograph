import type { AgentStep } from "../types/AgentStep";

export function ActivityLog({ steps }: { steps: AgentStep[] }) {
  if (steps.length === 0) {
    return <p className="empty-note">Agent steps show here as they happen.</p>;
  }
  const newestFirst = [...steps].reverse();
  return (
    <ol className="activity-list" aria-live="polite">
      {newestFirst.map((step, position) => (
        <li key={steps.length - position} className="activity-item" data-kind={step.kind}>
          <span className="activity-node">
            {step.node}
            {step.finding_id && ` · ${step.finding_id}`}
          </span>
          <span className="activity-message">{step.message}</span>
        </li>
      ))}
    </ol>
  );
}
