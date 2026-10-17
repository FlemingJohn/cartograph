import type { Evidence } from "../types/Evidence";

export function EvidenceItem({ evidence }: { evidence: Evidence }) {
  return (
    <div className="evidence-item">
      <span className="label">
        {evidence.agent} · {evidence.tool}
      </span>
      <p className="detail-text">{evidence.claim}</p>
      <pre className="cypher">{evidence.cypher}</pre>
    </div>
  );
}
