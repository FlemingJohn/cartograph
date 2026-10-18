import random


def make_log_sources():
    random.seed(42)
    sources = [
        {"id": "log-web-gateway", "name": "Web Gateway Access Log"},
        {"id": "log-auth", "name": "Auth Service Audit Log"},
        {"id": "log-checkout", "name": "Checkout Transaction Log"},
        {"id": "log-card-vault", "name": "Card Vault Cryptographic Log"},
        {"id": "log-billing", "name": "Billing Operations Log"},
        {"id": "log-user", "name": "User Profile Access Log"},
        {"id": "log-inventory", "name": "Inventory Event Log"},
        {"id": "log-notification", "name": "Notification Dispatch Log"},
        {"id": "log-audit-logger", "name": "Central Audit Stream Log"},
        {"id": "log-sysmon", "name": "WinEventLog:Sysmon"},
        {"id": "log-security", "name": "WinEventLog:Security"},
    ]

    service_writes = [
        ("web-gateway", "log-web-gateway"),
        ("auth-service", "log-auth"),
        ("checkout-service", "log-checkout"),
        ("card-vault-service", "log-card-vault"),
        ("billing-service", "log-billing"),
        ("user-service", "log-user"),
        ("inventory-service", "log-inventory"),
        ("notification-service", "log-notification"),
        ("audit-logger", "log-audit-logger"),
        ("payments-service", "log-security"),
    ]

    return {"sources": sources, "writes": service_writes}

