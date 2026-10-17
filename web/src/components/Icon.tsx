import type { IconName } from "../types/IconName";

const pathByName: Record<IconName, string> = {
  dashboard: "M4 4h7v7H4zM13 4h7v4h-7zM13 10h7v10h-7zM4 13h7v7H4z",
  approvals: "M4 4h16v16H4zM8 12l3 3 5-6",
  simulation: "M6 20V4M6 9h7l5 5v6M15 4h5v5",
  fold: "M15 6l-6 6 6 6",
  unfold: "M9 6l6 6-6 6",
  play: "M7 5l12 7-12 7z",
};

export function Icon({ name }: { name: IconName }) {
  return (
    <svg className="icon" viewBox="0 0 24 24" aria-hidden="true">
      <path d={pathByName[name]} />
    </svg>
  );
}
