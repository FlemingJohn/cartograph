import type { Finding } from "../types/Finding";
import { FindingRow } from "./FindingRow";

export function FindingList({
  findings,
  selectedId,
  onSelect,
}: {
  findings: Finding[];
  selectedId: string | null;
  onSelect: (findingId: string) => void;
}) {
  if (findings.length === 0) {
    return <p className="empty-note">Start a triage to rank the flaws.</p>;
  }
  return (
    <ol className="finding-list">
      {findings.map((finding, position) => (
        <li key={finding.finding_id}>
          <FindingRow
            finding={finding}
            rank={position + 1}
            isSelected={finding.finding_id === selectedId}
            onSelect={() => onSelect(finding.finding_id)}
          />
        </li>
      ))}
    </ol>
  );
}
