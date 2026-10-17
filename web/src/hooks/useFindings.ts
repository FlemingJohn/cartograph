import { useEffect, useState } from "react";
import { getJson } from "../lib/getJson";
import type { FindingsReport } from "../types/FindingsReport";

export function useFindings(scanId: string, changeCount: number): FindingsReport | null {
  const [report, setReport] = useState<FindingsReport | null>(null);

  useEffect(() => {
    let isCurrent = true;
    getJson<FindingsReport>(`/runs/${scanId}/findings`).then((answer) => {
      if (isCurrent) setReport(answer);
    });
    return () => {
      isCurrent = false;
    };
  }, [scanId, changeCount]);

  return report;
}
