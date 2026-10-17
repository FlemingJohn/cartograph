import type { Data } from "@falkordb/canvas";
import type { RouteGraph } from "../types/RouteGraph";
import type { RouteNodeKind } from "../types/RouteNodeKind";
import { getThemeToken } from "./getThemeToken";

const colourTokenByKind: Record<RouteNodeKind, string> = {
  internet: "system",
  service: "copper",
  data_store: "red",
};

const labelByKind: Record<RouteNodeKind, string> = {
  internet: "Internet",
  service: "Service",
  data_store: "DataStore",
};

export function toCanvasData(routeGraph: RouteGraph): Data {
  const numberById = new Map(routeGraph.nodes.map((node, position) => [node.id, position]));
  return {
    nodes: routeGraph.nodes.map((node, position) => ({
      id: position,
      labels: [labelByKind[node.kind]],
      color: getThemeToken(colourTokenByKind[node.kind]),
      visible: true,
      shape: "square",
      data: { name: node.id },
    })),
    links: routeGraph.links.map((link, position) => ({
      id: position,
      relationship: "",
      color: getThemeToken("faint"),
      source: numberById.get(link.source) ?? 0,
      target: numberById.get(link.target) ?? 0,
      visible: true,
      data: {},
    })),
  };
}
