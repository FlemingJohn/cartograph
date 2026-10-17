import { useState, type ReactNode } from "react";
import { SidePanel } from "./components/SidePanel";
import { TopBar } from "./components/TopBar";
import { useFindings } from "./hooks/useFindings";
import { useRunStream } from "./hooks/useRunStream";
import { useSidePanel } from "./hooks/useSidePanel";
import { countFindingsChanges } from "./lib/countFindingsChanges";
import { getScanId } from "./lib/getScanId";
import { ApprovalsScreen } from "./screens/ApprovalsScreen";
import { DashboardScreen } from "./screens/DashboardScreen";
import { SimulationScreen } from "./screens/SimulationScreen";
import type { ScreenName } from "./types/ScreenName";

const scanId = getScanId();

export function App() {
  const [screen, setScreen] = useState<ScreenName>("dashboard");
  const { isFolded, toggleFolded } = useSidePanel();
  const run = useRunStream(scanId);
  const changeCount = countFindingsChanges(run.steps);
  const report = useFindings(scanId, changeCount);

  const screenByName: Record<ScreenName, ReactNode> = {
    dashboard: (
      <DashboardScreen scanId={scanId} run={run} report={report} changeCount={changeCount} />
    ),
    approvals: <ApprovalsScreen run={run} report={report} />,
    simulation: <SimulationScreen run={run} report={report} />,
  };

  return (
    <div className="app" data-folded={isFolded}>
      <TopBar scanId={scanId} runStatus={run.runStatus} onStartRun={run.startRun} />
      <div className="app-body">
        <SidePanel
          currentScreen={screen}
          isFolded={isFolded}
          onPickScreen={setScreen}
          onToggleFolded={toggleFolded}
        />
        {screenByName[screen]}
      </div>
    </div>
  );
}
