import { statusLabels } from "../lib/statusLabels";
import type { Finding } from "../types/Finding";
import { StatusChip } from "./StatusChip";

export function FindingRow({
  finding,
  rank,
  isSelected,
  onSelect,
}: {
  finding: Finding;
  rank: number;
  isSelected: boolean;
  onSelect: () => void;
}) {
  return (
    <button type="button" className="finding-row" aria-pressed={isSelected} onClick={onSelect}>
      <span className="finding-rank">{rank}</span>
      <span className="finding-title" title={finding.title}>
        {finding.title}
      </span>
      <span className="finding-score">{finding.score}</span>
      <span className="finding-service">{finding.service_id}</span>
      <StatusChip status={finding.status} label={statusLabels[finding.status]} />
    </button>
  );
}
