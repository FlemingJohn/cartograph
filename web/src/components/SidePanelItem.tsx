import type { IconName } from "../types/IconName";
import { Icon } from "./Icon";

export function SidePanelItem({
  icon,
  label,
  isCurrent,
  onClick,
}: {
  icon: IconName;
  label: string;
  isCurrent: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      className="side-panel-item"
      aria-current={isCurrent ? "page" : undefined}
      title={label}
      onClick={onClick}
    >
      <Icon name={icon} />
      <span className="side-panel-label">{label}</span>
    </button>
  );
}
