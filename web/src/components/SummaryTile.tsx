export function SummaryTile({
  label,
  value,
  status,
}: {
  label: string;
  value: number;
  status?: string;
}) {
  return (
    <div className="summary-tile" data-status={status}>
      <span className="label">{label}</span>
      <span className="summary-number">{value}</span>
    </div>
  );
}
