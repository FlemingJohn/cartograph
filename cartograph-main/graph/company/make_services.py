import random


def make_services():
    random.seed(42)
    service_names = [
        ("web-gateway", False, "team-platform"),
        ("api-gateway", False, "team-platform"),
        ("auth-service", True, "team-identity"),
        ("checkout-service", True, "team-payments"),
        ("payments-service", True, "team-payments"),
        ("card-vault-service", True, "team-payments"),
        ("billing-service", True, "team-payments"),
        ("ledger-service", True, "team-payments"),
        ("user-service", True, "team-identity"),
        ("profile-service", True, "team-identity"),
        ("search-service", True, "team-platform"),
        ("catalog-service", True, "team-platform"),
        ("cart-service", True, "team-platform"),
        ("order-service", True, "team-payments"),
        ("shipping-service", True, "team-platform"),
        ("inventory-service", True, "team-platform"),
        ("warehouse-service", True, "team-platform"),
        ("notification-service", True, "team-platform"),
        ("email-service", True, "team-platform"),
        ("sms-service", True, "team-platform"),
        ("recommendation-service", True, "team-analytics"),
        ("pricing-service", True, "team-platform"),
        ("fraud-detection-service", True, "team-payments"),
        ("ratings-service", True, "team-platform"),
        ("comments-service", True, "team-platform"),
        ("media-service", True, "team-platform"),
        ("assets-cdn-origin", True, "team-platform"),
        ("metrics-collector", True, "team-security"),
        ("audit-logger", True, "team-security"),
        ("report-generator", True, "team-analytics"),
    ]
    services = [
        {
            "id": s[0],
            "name": s[0].replace("-", " ").title(),
            "is_internal": s[1],
            "team_id": s[2],
        }
        for s in service_names
    ]

    calls = [
        ("web-gateway", "checkout-service"),
        ("web-gateway", "cart-service"),
        ("web-gateway", "catalog-service"),
        ("web-gateway", "auth-service"),
        ("checkout-service", "payments-service"),
        ("payments-service", "card-vault-service"),
        ("payments-service", "billing-service"),
        ("payments-service", "fraud-detection-service"),
        ("billing-service", "ledger-service"),
        ("checkout-service", "order-service"),
        ("order-service", "shipping-service"),
        ("order-service", "inventory-service"),
        ("inventory-service", "warehouse-service"),
        ("order-service", "notification-service"),
        ("notification-service", "email-service"),
        ("notification-service", "sms-service"),
        ("cart-service", "pricing-service"),
        ("catalog-service", "search-service"),
        ("catalog-service", "recommendation-service"),
        ("catalog-service", "ratings-service"),
        ("catalog-service", "media-service"),
        ("ratings-service", "comments-service"),
        ("media-service", "assets-cdn-origin"),
        ("auth-service", "user-service"),
        ("user-service", "profile-service"),
        ("metrics-collector", "audit-logger"),
    ]

    reads = [
        ("card-vault-service", "customer-cards"),
        ("user-service", "user-accounts-db"),
        ("auth-service", "session-cache"),
        ("catalog-service", "product-catalog-db"),
        ("inventory-service", "inventory-db"),
        ("report-generator", "analytics-warehouse"),
        ("audit-logger", "audit-archive"),
        ("notification-service", "notification-queue"),
    ]

    return {"services": services, "calls": calls, "reads": reads}

