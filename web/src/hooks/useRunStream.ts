import { useCallback, useEffect, useRef, useState } from "react";
import { getApiUrl } from "../lib/getApiUrl";
import { getRunStatus } from "../lib/getRunStatus";
import { makeFailedStep } from "../lib/makeFailedStep";
import { sendJson } from "../lib/sendJson";
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

  const reportFailure = useCallback(
    (error: unknown) => setSteps((current) => [...current, makeFailedStep(scanId, error)]),
    [scanId],
  );

  const startRun = useCallback(async () => {
    sourceRef.current?.close();
    setSteps([]);
    await sendJson("POST", "/runs", { scan_id: scanId }).then(openStream, reportFailure);
  }, [scanId, openStream, reportFailure]);

  const answerApproval = useCallback(
    async (isApproved: boolean) => {
      const body = { is_approved: isApproved };
      await sendJson("POST", `/runs/${scanId}/approve`, body).catch(reportFailure);
    },
    [scanId, reportFailure],
  );

  return { steps, runStatus: getRunStatus(steps), startRun, answerApproval, reportFailure };
}
