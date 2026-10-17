import type { CSSProperties } from "react";

const legendItems = [
  { label: "Internet", colour: "var(--system)" },
  { label: "Service", colour: "var(--accent)" },
  { label: "Data", colour: "var(--urgent)" },
];

export function RouteLegend() {
  return (
    <span className="route-legend">
      {legendItems.map((item) => (
        <span
          key={item.label}
          className="route-legend-item label"
          style={{ "--legend-colour": item.colour } as CSSProperties}
        >
          {item.label}
        </span>
      ))}
    </span>
  );
}
