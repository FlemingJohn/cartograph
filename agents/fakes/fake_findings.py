from random import Random

from agents.fakes.fake_service_ids import FAKE_SERVICE_IDS
from agents.state.finding import Finding

FINDING_COUNT = 214
TECHNIQUE_CHOICES = [["T1190"], ["T1059"], ["T1078"], ["T1210"], ["T1552"], []]


def make_fake_findings(scan_id: str) -> list[Finding]:
    randomness = Random(scan_id)
    other_findings = [
        make_other_finding(number, randomness) for number in range(3, FINDING_COUNT + 1)
    ]
    return [make_payments_finding(), make_report_finding(), *other_findings]


def make_payments_finding() -> Finding:
    return {
        "finding_id": "F-0001",
        "title": "Request smuggling in the payments HTTP library",
        "severity": 6.5,
        "service_id": "payments-service",
        "technique_ids": ["T1190"],
    }


def make_report_finding() -> Finding:
    return {
        "finding_id": "F-0002",
        "title": "Remote code execution in the PDF renderer",
        "severity": 9.8,
        "service_id": "report-generator",
        "technique_ids": ["T1059"],
    }


def make_other_finding(number: int, randomness: Random) -> Finding:
    return {
        "finding_id": f"F-{number:04d}",
        "title": f"Outdated library flaw number {number}",
        "severity": round(randomness.uniform(1.0, 9.0), 1),
        "service_id": randomness.choice(FAKE_SERVICE_IDS[2:]),
        "technique_ids": randomness.choice(TECHNIQUE_CHOICES),
    }
