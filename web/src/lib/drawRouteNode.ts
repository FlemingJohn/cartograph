import type { GraphNode } from "@falkordb/canvas";
import { getThemeToken } from "./getThemeToken";

const squareSize = 14;
const labelGap = 6;
const labelSize = 6;

export function drawRouteNode(node: GraphNode, context: CanvasRenderingContext2D) {
  const x = node.x ?? 0;
  const y = node.y ?? 0;
  context.fillStyle = node.color;
  context.fillRect(x - squareSize / 2, y - squareSize / 2, squareSize, squareSize);
  context.fillStyle = getThemeToken("ink");
  context.font = `600 ${labelSize}px ${getThemeToken("font-mono")}`;
  context.textAlign = "center";
  context.textBaseline = "top";
  context.fillText(String(node.data.name), x, y + squareSize / 2 + labelGap);
}

export function drawRouteNodeArea(
  node: GraphNode,
  colour: string,
  context: CanvasRenderingContext2D,
) {
  context.fillStyle = colour;
  context.fillRect(
    (node.x ?? 0) - squareSize / 2,
    (node.y ?? 0) - squareSize / 2,
    squareSize,
    squareSize,
  );
}
