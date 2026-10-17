export function StatusChip({ status, label }: { status: string; label: string }) {
  return (
    <span className="status-chip" data-status={status}>
      {label}
    </span>
  );
}
