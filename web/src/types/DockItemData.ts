import type { ReactNode } from "react";

export interface DockItemData {
  id: string;
  label: string;
  icon: ReactNode;
  isActive: boolean;
  onClick: () => void;
}
