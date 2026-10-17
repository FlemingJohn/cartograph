import type { Finding } from "../types/Finding";

export function DashboardHeadline({ findings }: { findings: Finding[] }) {
  const urgentCount = findings.filter((finding) => finding.status === "fix_now").length;
  if (findings.length === 0) {
    return (
      <div>
        <h1 className="screen-title">Map the routes an attacker would take.</h1>
        <p className="screen-note">Start a triage to rank every flaw by what it can reach.</p>
      </div>
    );
  }
  return (
    <div>
      <h1 className="screen-title">
        {findings.length} flaws. <span className="accent">{urgentCount} need you now.</span>
      </h1>
      <p className="screen-note">Ranked by what an attacker can actually reach, not by severity alone.</p>
    </div>
  );
}
