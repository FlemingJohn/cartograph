import { useState } from "react";
import { ActivityLog } from "../components/ActivityLog";
import { FindingList } from "../components/FindingList";
import { KpiRow } from "../components/KpiRow";
import { Pane } from "../components/Pane";
import { RouteLegend } from "../components/RouteLegend";
import { RouteMap } from "../components/RouteMap";
import { WhyPanel } from "../components/WhyPanel";
import { useRoute } from "../hooks/useRoute";
import type { FindingsReport } from "../types/FindingsReport";
import type { RunStream } from "../types/RunStream";

export function DashboardScreen({
  scanId,
  run,
  report,
  changeCount,
}: {
  scanId: string;
  run: RunStream;
  report: FindingsReport | null;
  changeCount: number;
}) {
  const findings = report?.findings ?? [];
  const [pickedId, setPickedId] = useState<string | null>(null);
  const selectedId = pickedId ?? findings[0]?.finding_id ?? null;
  const selectedFinding = findings.find((finding) => finding.finding_id === selectedId) ?? null;
  const route = useRoute(scanId, selectedId, changeCount);

  return (
    <main className="screen">
      <div className="screen-head">
        <h1 className="screen-title">Attack paths</h1>
        <p className="screen-note">Ranked by what an attacker can actually reach.</p>
      </div>
      <KpiRow findings={findings} />
      <div className="dashboard-panes">
        <Pane title="Ranked flaws">
          <FindingList findings={findings} selectedId={selectedId} onSelect={setPickedId} />
        </Pane>
        <Pane title={`Route · ${selectedFinding?.service_id ?? "none"}`} aside={<RouteLegend />}>
          <RouteMap route={route} />
        </Pane>
        <Pane title="Why this rank">
          <WhyPanel finding={selectedFinding} route={route} />
        </Pane>
      </div>
      <div className="activity-pane">
        <Pane title="Agent activity">
          <ActivityLog steps={run.steps} />
        </Pane>
      </div>
    </main>
  );
}
