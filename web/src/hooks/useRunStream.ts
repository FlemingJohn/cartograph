import { useCallback, useEffect, useRef, useState } from "react";
import { getApiUrl } from "../lib/getApiUrl";
import { getRunStatus } from "../lib/getRunStatus";
import { postJson } from "../lib/postJson";
import type { AgentStep } from "../types/AgentStep";
import type { RunStream } from "../types/RunStream";

export function useRunStream(scanId: string): RunStream {
  const [steps, setSteps] = useState<AgentStep[]>([]);
  const sourceRef = useRef<EventSource | null>(null);

  const openStream = useCallback(() => {
    sourceRef.current?.close();
    const source = new EventSource(getApiUrl(`/runs/${scanId}/stream`));
    source.onopen = () => setSteps([]);
    source.onmessage = (event) => {
      const step = JSON.parse(event.data) as AgentStep;
      setSteps((current) => [...current, step]);
      if (step.kind === "finished") source.close();
    };
    sourceRef.current = source;
  }, [scanId]);

  useEffect(() => {
    openStream();
    return () => sourceRef.current?.close();
  }, [openStream]);

  const startRun = useCallback(async () => {
    sourceRef.current?.close();
    setSteps([]);
    await postJson("/runs", { scan_id: scanId });
    openStream();
  }, [scanId, openStream]);

  const answerApproval = useCallback(
    async (isApproved: boolean) => {
      await postJson(`/runs/${scanId}/approve`, { is_approved: isApproved });
    },
    [scanId],
  );

  return { steps, runStatus: getRunStatus(steps), startRun, answerApproval };
}
