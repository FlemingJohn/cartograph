import { ActivityLog } from "../components/ActivityLog";
import { ApprovalActions } from "../components/ApprovalActions";
import { ApprovalPanel } from "../components/ApprovalPanel";
import { Pane } from "../components/Pane";
import type { FindingsReport } from "../types/FindingsReport";
import type { RunStream } from "../types/RunStream";

export function ApprovalsScreen({ run, report }: { run: RunStream; report: FindingsReport | null }) {
  const isWaiting = run.runStatus === "paused";
  return (
    <main className="screen">
      <div className="screen-head">
        <h1 className="screen-title">Approve the plan</h1>
        <ApprovalActions isWaiting={isWaiting} onAnswer={run.answerApproval} />
      </div>
      <p className="screen-note">
        Nothing is saved and no ticket is written until a person approves.
      </p>
      <div className="two-panes">
        <Pane title={`Planned actions · ${report?.plan.length ?? 0}`}>
          <ApprovalPanel plan={report?.plan ?? []} findings={report?.findings ?? []} />
        </Pane>
        <Pane title="Agent activity">
          <ActivityLog steps={run.steps} />
        </Pane>
      </div>
    </main>
  );
}
