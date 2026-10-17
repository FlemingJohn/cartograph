import type { IconName } from "./IconName";
import type { ScreenName } from "./ScreenName";

export interface ScreenItem {
  screen: ScreenName;
  icon: IconName;
  label: string;
}
