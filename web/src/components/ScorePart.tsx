export function ScorePart({
  label,
  points,
  maximum,
}: {
  label: string;
  points: number;
  maximum: number;
}) {
  const filledShare = `${Math.min(points / maximum, 1) * 100}%`;
  return (
    <div className="score-part">
      <span>{label}</span>
      <span className="score-part-points">
        {Math.round(points)}/{maximum}
      </span>
      <span className="score-part-track">
        <span className="score-part-fill" style={{ width: filledShare }} />
      </span>
    </div>
  );
}
