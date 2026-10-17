export function SummaryTile({
  label,
  value,
  total,
  status,
}: {
  label: string;
  value: number;
  total: number;
  status?: string;
}) {
  const share = total > 0 ? (value / total) * 100 : 0;
  return (
    <div className="summary-tile" data-status={status}>
      <span className="label">{label}</span>
      <span className="summary-number">{value}</span>
      <span className="summary-share">
        <span className="summary-share-fill" style={{ width: `${share}%` }} />
      </span>
    </div>
  );
}
