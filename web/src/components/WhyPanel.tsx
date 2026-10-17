import { scorePartRows } from "../lib/scorePartRows";
import type { Finding } from "../types/Finding";
import type { RouteGraph } from "../types/RouteGraph";
import { EvidenceItem } from "./EvidenceItem";
import { ScorePart } from "./ScorePart";

export function WhyPanel({ finding, route }: { finding: Finding | null; route: RouteGraph | null }) {
  if (!finding) {
    return <p className="empty-note">Pick a flaw to see why it ranks where it does.</p>;
  }
  const fixSteps = route?.plan?.fix_steps ?? [];
  return (
    <>
      <section className="detail-section">
        <h3 className="detail-title">{finding.title}</h3>
        <p className="detail-text">{finding.reason}</p>
      </section>
      <section className="detail-section" aria-label="Score">
        <span className="label">Score {finding.score} of 100</span>
        {scorePartRows.map((row) => (
          <ScorePart
            key={row.part}
            label={row.label}
            points={finding.parts[row.part]}
            maximum={row.maximum}
          />
        ))}
      </section>
      {fixSteps.length > 0 && (
        <section className="detail-section" aria-label="Fix steps">
          <span className="label">Fix steps</span>
          <ol className="step-list">
            {fixSteps.map((step) => (
              <li key={step}>{step}</li>
            ))}
          </ol>
        </section>
      )}
      {route?.evidence.map((evidence) => (
        <section className="detail-section" key={evidence.id}>
          <EvidenceItem evidence={evidence} />
        </section>
      ))}
    </>
  );
}
