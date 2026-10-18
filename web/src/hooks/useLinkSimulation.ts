import { useState } from "react";
import { sendJson } from "../lib/sendJson";
import { simulatedLink } from "../lib/simulatedLink";
import type { RunStream } from "../types/RunStream";

export function useLinkSimulation(run: RunStream, currentRank: number | null) {
  const [rankBefore, setRankBefore] = useState<number | null>(null);

  async function changeLink(method: "POST" | "DELETE") {
    setRankBefore(currentRank);
    await sendJson(method, "/simulations/link", simulatedLink).then(run.startRun, run.reportFailure);
  }

  return {
    rankBefore,
    connect: () => changeLink("POST"),
    disconnect: () => changeLink("DELETE"),
  };
}
