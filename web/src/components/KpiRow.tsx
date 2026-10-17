import type { Finding } from "../types/Finding";
import { SummaryTile } from "./SummaryTile";

export function KpiRow({ findings }: { findings: Finding[] }) {
  const countWith = (status: Finding["status"]) =>
    findings.filter((finding) => finding.status === status).length;
  return (
    <section className="summary-row" aria-label="Summary">
      <SummaryTile label="Flaws ranked" value={findings.length} />
      <SummaryTile label="Fix now" value={countWith("fix_now")} status="fix_now" />
      <SummaryTile label="Watch" value={countWith("watch")} status="watch" />
      <SummaryTile label="Accept" value={countWith("accept")} status="accept" />
    </section>
  );
}
