import { statusLabels } from "../lib/statusLabels";
import type { ServiceRank } from "../types/ServiceRank";
import { StatusChip } from "./StatusChip";

export function RankChange({
  rankBefore,
  current,
  total,
}: {
  rankBefore: number | null;
  current: ServiceRank | null;
  total: number;
}) {
  if (!current) {
    return <p className="empty-note">Run a triage to see where the report generator ranks.</p>;
  }
  return (
    <div className="rank-change">
      {rankBefore !== null && (
        <>
          <span className="rank-number rank-number-before">#{rankBefore}</span>
          <span className="rank-arrow" aria-hidden="true">→</span>
        </>
      )}
      <span className="rank-number">#{current.rank}</span>
      <div className="rank-details">
        <span className="label">of {total} flaws · score {current.finding.score}</span>
        <span className="detail-title">{current.finding.title}</span>
        <StatusChip status={current.finding.status} label={statusLabels[current.finding.status]} />
      </div>
    </div>
  );
}
