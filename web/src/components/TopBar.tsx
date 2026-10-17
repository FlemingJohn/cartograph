import { runStatusLabels } from "../lib/runStatusLabels";
import type { RunStatus } from "../types/RunStatus";
import type { ScreenName } from "../types/ScreenName";
import { Button } from "./Button";
import { Icon } from "./Icon";
import { ScreenDock } from "./ScreenDock";
import { StatusChip } from "./StatusChip";

export function TopBar({
  scanId,
  runStatus,
  currentScreen,
  onPickScreen,
  onStartRun,
}: {
  scanId: string;
  runStatus: RunStatus;
  currentScreen: ScreenName;
  onPickScreen: (screen: ScreenName) => void;
  onStartRun: () => void;
}) {
  const isBusy = runStatus === "running" || runStatus === "paused";
  return (
    <header className="top-bar">
      <div className="top-bar-brand">
        <span className="brand-mark" aria-hidden="true" />
        <span className="top-bar-name">CartoGraph</span>
        <span className="scan-label">{scanId}</span>
      </div>
      <ScreenDock currentScreen={currentScreen} onPickScreen={onPickScreen} />
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
