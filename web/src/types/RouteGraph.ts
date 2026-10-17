import type { Evidence } from "./Evidence";
import type { PlannedAction } from "./PlannedAction";
import type { RouteLink } from "./RouteLink";
import type { RouteNode } from "./RouteNode";

export interface RouteGraph {
  finding_id: string;
  nodes: RouteNode[];
  links: RouteLink[];
  evidence: Evidence[];
  plan: PlannedAction | null;
}
