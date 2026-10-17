import { runStatusLabels } from "../lib/runStatusLabels";
import type { RunStatus } from "../types/RunStatus";
import { Button } from "./Button";
import { Icon } from "./Icon";
import { StatusChip } from "./StatusChip";

export function TopBar({
  scanId,
  runStatus,
  onStartRun,
}: {
  scanId: string;
  runStatus: RunStatus;
  onStartRun: () => void;
}) {
  const isBusy = runStatus === "running" || runStatus === "paused";
  return (
    <header className="top-bar">
      <div className="top-bar-brand">
        <span className="top-bar-name">CartoGraph</span>
        <span className="scan-label">{scanId}</span>
      </div>
      <div className="top-bar-actions">
        <StatusChip status={runStatus} label={runStatusLabels[runStatus]} />
        <Button isPrimary isDisabled={isBusy} onClick={onStartRun}>
          <Icon name="play" />
          Start triage
        </Button>
      </div>
    </header>
  );
}
