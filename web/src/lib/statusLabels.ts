import type { FindingStatus } from "../types/FindingStatus";

export const statusLabels: Record<FindingStatus, string> = {
  fix_now: "Fix now",
  watch: "Watch",
  accept: "Accept",
};
