import type { ScreenItem } from "../types/ScreenItem";
import type { ScreenName } from "../types/ScreenName";
import { SidePanelItem } from "./SidePanelItem";

const screenItems: ScreenItem[] = [
  { screen: "dashboard", icon: "dashboard", label: "Dashboard" },
  { screen: "approvals", icon: "approvals", label: "Approvals" },
  { screen: "simulation", icon: "simulation", label: "Simulation" },
];

export function SidePanel({
  currentScreen,
  isFolded,
  onPickScreen,
  onToggleFolded,
}: {
  currentScreen: ScreenName;
  isFolded: boolean;
  onPickScreen: (screen: ScreenName) => void;
  onToggleFolded: () => void;
}) {
  return (
    <nav className="side-panel" aria-label="Screens">
      {screenItems.map((item) => (
        <SidePanelItem
          key={item.screen}
          icon={item.icon}
          label={item.label}
          isCurrent={item.screen === currentScreen}
          onClick={() => onPickScreen(item.screen)}
        />
      ))}
      <span className="side-panel-gap" />
      <SidePanelItem
        icon={isFolded ? "unfold" : "fold"}
        label={isFolded ? "Open panel" : "Fold panel"}
        isCurrent={false}
        onClick={onToggleFolded}
      />
    </nav>
  );
}
