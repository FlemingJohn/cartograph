import { useEffect, useState } from "react";
import { getJson } from "../lib/getJson";
import type { RouteGraph } from "../types/RouteGraph";

export function useRoute(
  scanId: string,
  findingId: string | null,
  changeCount: number,
): RouteGraph | null {
  const [route, setRoute] = useState<RouteGraph | null>(null);

  useEffect(() => {
    let isCurrent = true;
    const path = `/runs/${scanId}/findings/${findingId}/route`;
    const request = findingId ? getJson<RouteGraph>(path) : Promise.resolve(null);
    request.then((answer) => {
      if (isCurrent) setRoute(answer);
    });
    return () => {
      isCurrent = false;
    };
  }, [scanId, findingId, changeCount]);

  return route;
}
