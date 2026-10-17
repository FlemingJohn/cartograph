import type { Finding } from "../types/Finding";
import { SummaryTile } from "./SummaryTile";

export function KpiRow({ findings }: { findings: Finding[] }) {
  const total = findings.length;
  const countWith = (status: Finding["status"]) =>
    findings.filter((finding) => finding.status === status).length;
  return (
    <section className="summary-row" aria-label="Summary">
      <SummaryTile label="Flaws ranked" value={total} total={total} />
      <SummaryTile label="Fix now" value={countWith("fix_now")} total={total} status="fix_now" />
      <SummaryTile label="Watch" value={countWith("watch")} total={total} status="watch" />
      <SummaryTile label="Accept" value={countWith("accept")} total={total} status="accept" />
    </section>
  );
}
