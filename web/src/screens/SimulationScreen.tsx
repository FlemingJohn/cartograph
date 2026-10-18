import { Button } from "../components/Button";
import { Pane } from "../components/Pane";
import { RankChange } from "../components/RankChange";
import { useLinkSimulation } from "../hooks/useLinkSimulation";
import { getServiceRank } from "../lib/getServiceRank";
import { simulatedLink } from "../lib/simulatedLink";
import type { FindingsReport } from "../types/FindingsReport";
import type { RunStream } from "../types/RunStream";

export function SimulationScreen({ run, report }: { run: RunStream; report: FindingsReport | null }) {
  const findings = report?.findings ?? [];
  const current = getServiceRank(findings, simulatedLink.target_id);
  const simulation = useLinkSimulation(run, current?.rank ?? null);
  const isBusy = run.runStatus === "running";

  return (
    <main className="screen">
      <div className="screen-head">
        <div>
          <h1 className="screen-title">What if the report generator faced the internet?</h1>
          <p className="screen-note">
            Link {simulatedLink.source_id} to {simulatedLink.target_id}, rerun the triage, and
            watch its rank move.
          </p>
        </div>
        <span className="approval-actions">
          <Button isDisabled={isBusy} onClick={simulation.disconnect}>
            Undo the link
          </Button>
          <Button isPrimary isDisabled={isBusy} onClick={simulation.connect}>
            Link and rerun
          </Button>
        </span>
      </div>
      <Pane title={`Rank of ${simulatedLink.target_id}`}>
        <RankChange rankBefore={simulation.rankBefore} current={current} total={findings.length} />
      </Pane>
    </main>
  );
}
