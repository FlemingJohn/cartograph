import { useState, type ReactNode } from "react";
import { ScreenDock } from "./components/ScreenDock";
import { TopBar } from "./components/TopBar";
import { useFindings } from "./hooks/useFindings";
import { useRunStream } from "./hooks/useRunStream";
import { countFindingsChanges } from "./lib/countFindingsChanges";
import { getScanId } from "./lib/getScanId";
import { ApprovalsScreen } from "./screens/ApprovalsScreen";
import { DashboardScreen } from "./screens/DashboardScreen";
import { IntroScreen } from "./screens/IntroScreen";
import { SimulationScreen } from "./screens/SimulationScreen";
import type { ScreenName } from "./types/ScreenName";

const scanId = getScanId();

export function App() {
  const [hasStarted, setHasStarted] = useState(false);
  const [screen, setScreen] = useState<ScreenName>("dashboard");
  const run = useRunStream(scanId);
  const changeCount = countFindingsChanges(run.steps);
  const report = useFindings(scanId, changeCount);

  if (!hasStarted) {
    return <IntroScreen onStart={() => setHasStarted(true)} />;
  }

  const screenByName: Record<ScreenName, ReactNode> = {
    dashboard: (
      <DashboardScreen scanId={scanId} run={run} report={report} changeCount={changeCount} />
    ),
    approvals: <ApprovalsScreen run={run} report={report} />,
    simulation: <SimulationScreen run={run} report={report} />,
  };

  return (
    <div className="app">
      <TopBar scanId={scanId} runStatus={run.runStatus} onStartRun={run.startRun} />
      {screenByName[screen]}
      <div className="dock-area">
        <ScreenDock currentScreen={screen} onPickScreen={setScreen} />
      </div>
    </div>
  );
}
