import type { IconName } from "../types/IconName";
import type { ScreenName } from "../types/ScreenName";
import { Icon } from "./Icon";
import { MagneticDock } from "./MagneticDock";

const screens: { screen: ScreenName; label: string }[] = [
  { screen: "dashboard", label: "Dashboard" },
  { screen: "approvals", label: "Approvals" },
  { screen: "simulation", label: "Simulation" },
];

export function ScreenDock({
  currentScreen,
  onPickScreen,
}: {
  currentScreen: ScreenName;
  onPickScreen: (screen: ScreenName) => void;
}) {
  const items = screens.map(({ screen, label }) => ({
    id: screen,
    label,
    icon: <Icon name={screen satisfies IconName} />,
    isActive: screen === currentScreen,
    onClick: () => onPickScreen(screen),
  }));
  return <MagneticDock items={items} />;
}
