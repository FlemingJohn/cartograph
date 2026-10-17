import type { IconName } from "../types/IconName";

const pathByName: Record<IconName, string> = {
  dashboard: "M4 13h6V4H4zM14 20h6v-9h-6zM14 4v4h6V4zM4 20h6v-3H4z",
  approvals: "M9 12l2 2 4-4M12 3l7 3v5c0 4.5-3 8.2-7 10-4-1.8-7-5.5-7-10V6z",
  simulation: "M5 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM19 9a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM7 17h4a4 4 0 0 0 4-4v-2a4 4 0 0 1 2-3.4",
  play: "M7 5l12 7-12 7z",
  arrow: "M5 12h14M13 6l6 6-6 6",
};

export function Icon({ name }: { name: IconName }) {
  return (
    <svg className="icon" viewBox="0 0 24 24" aria-hidden="true">
      <path d={pathByName[name]} />
    </svg>
  );
}
