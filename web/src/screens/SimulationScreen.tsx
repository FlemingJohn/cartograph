import { Button } from "../components/Button";
import { FindingList } from "../components/FindingList";
import { Pane } from "../components/Pane";
import type { FindingsReport } from "../types/FindingsReport";
import type { RunStream } from "../types/RunStream";

const watchedServiceId = "report-generator";

export function SimulationScreen({ run, report }: { run: RunStream; report: FindingsReport | null }) {
  const findings = report?.findings ?? [];
  const watchedFindings = findings.filter((finding) => finding.service_id === watchedServiceId);
  const isBusy = run.runStatus === "running" || run.runStatus === "paused";
  return (
    <main className="screen">
      <div className="screen-head">
        <h1 className="screen-title">What if the report generator faced the internet?</h1>
        <Button isPrimary isDisabled={isBusy} onClick={run.startRun}>
          Rerun triage
        </Button>
      </div>
      <p className="screen-note">
        Add a link from the front door to the report generator, rerun, and watch its rank move.
      </p>
      <Pane title={`Flaws in ${watchedServiceId}`}>
        <FindingList findings={watchedFindings} selectedId={null} onSelect={() => undefined} />
      </Pane>
    </main>
  );
}
