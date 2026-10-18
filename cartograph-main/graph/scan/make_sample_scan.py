import json
import random
from pathlib import Path


def make_sample_scan():
    random.seed(42)
    flaws = []

    flaws.append(
        {
            "id": "flaw-payments-001",
            "title": "Spring Framework Remote Code Execution in Payment Gateway Integration",
            "severity": 6.5,
            "service_id": "payments-service",
            "library": {"id": "lib-spring-web", "name": "spring-web", "version": "5.3.18"},
            "technique_id": "T1190",
        }
    )

    flaws.append(
        {
            "id": "flaw-report-001",
            "title": "Log4j Remote Code Execution in Internal Reporting Template Processor",
            "severity": 9.8,
            "service_id": "report-generator",
            "library": {"id": "lib-log4j-core", "name": "log4j-core", "version": "2.14.1"},
            "technique_id": "T1190",
        }
    )

    all_services = [
        "web-gateway",
        "api-gateway",
        "auth-service",
        "checkout-service",
        "card-vault-service",
        "billing-service",
        "ledger-service",
        "user-service",
        "profile-service",
        "search-service",
        "catalog-service",
        "cart-service",
        "order-service",
        "shipping-service",
        "inventory-service",
        "warehouse-service",
        "notification-service",
        "email-service",
        "sms-service",
        "recommendation-service",
        "pricing-service",
        "fraud-detection-service",
        "ratings-service",
        "comments-service",
        "media-service",
        "assets-cdn-origin",
        "metrics-collector",
        "audit-logger",
    ]

    sample_libs = [
        ("lib-jackson", "jackson-databind", "2.12.3", "T1190"),
        ("lib-netty", "netty-codec-http", "4.1.65.Final", "T1190"),
        ("lib-struts", "struts2-core", "2.5.26", "T1190"),
        ("lib-commons-text", "commons-text", "1.9", "T1190"),
        ("lib-json-jwt", "jjwt", "0.9.1", None),
        ("lib-grpc", "grpc-netty", "1.38.0", None),
        ("lib-postgresql", "postgresql", "42.2.20", None),
        ("lib-redis-client", "lettuce-core", "6.1.2.RELEASE", None),
    ]

    for i in range(2, 214):
        svc = random.choice(all_services)
        lib_choice = random.choice(sample_libs)
        sev = round(random.uniform(2.0, 9.5), 1)
        flaw_id = f"flaw-{i:03d}"
        flaws.append(
            {
                "id": flaw_id,
                "title": f"Security Vulnerability CVE-2026-{1000 + i} in {lib_choice[1]}",
                "severity": sev,
                "service_id": svc,
                "library": {
                    "id": lib_choice[0],
                    "name": lib_choice[1],
                    "version": lib_choice[2],
                },
                "technique_id": lib_choice[3],
            }
        )

    scan_data = {
        "id": "scan-2026-10-18-001",
        "started_at": "2026-10-18T00:00:00Z",
        "flaw_count": len(flaws),
        "flaws": flaws,
    }

    Path("data").mkdir(exist_ok=True)
    with open("data/sample-scan.json", "w", encoding="utf-8") as f:
        json.dump(scan_data, f, indent=2)

    return scan_data

