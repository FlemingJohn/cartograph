import "@falkordb/canvas";
import type { FalkorDBCanvas } from "@falkordb/canvas";
import { useEffect, useRef } from "react";
import { drawRouteNode, drawRouteNodeArea } from "../lib/drawRouteNode";
import { getThemeToken } from "../lib/getThemeToken";
import { toCanvasData } from "../lib/toCanvasData";
import type { RouteGraph } from "../types/RouteGraph";

export function RouteMap({ route }: { route: RouteGraph | null }) {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<FalkorDBCanvas>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    canvas?.setConfig(makeCanvasConfiguration(() => canvas.zoomToFit(1.4)));
  }, []);

  useEffect(() => {
    if (route) canvasRef.current?.setData(toCanvasData(route));
  }, [route]);

  useEffect(() => {
    const wrapper = wrapperRef.current;
    if (!wrapper) return;
    const observer = new ResizeObserver(() => fitCanvas(wrapper, canvasRef.current));
    observer.observe(wrapper);
    return () => observer.disconnect();
  }, []);

  return (
    <div className="route-map" ref={wrapperRef}>
      <falkordb-canvas ref={canvasRef} />
    </div>
  );
}

function makeCanvasConfiguration(onLayoutDone: () => void) {
  return {
    backgroundColor: getThemeToken("background"),
    foregroundColor: getThemeToken("ink"),
    layoutMode: "tree" as const,
    layoutOptions: { tree: { direction: "lr" as const, levelDistance: 70, nodeSpacing: 50 } },
    node: { nodeCanvasObject: drawRouteNode, nodePointerAreaPaint: drawRouteNodeArea },
    eventHandlers: { onEngineStop: onLayoutDone },
  };
}

function fitCanvas(wrapper: HTMLDivElement, canvas: FalkorDBCanvas | null) {
  canvas?.setWidth(wrapper.clientWidth);
  canvas?.setHeight(wrapper.clientHeight);
  canvas?.zoomToFit(1.4);
}
