import random


def make_data_stores():
    random.seed(42)
    stores = [
        {"id": "customer-cards", "name": "Customer Credit Cards DB", "has_personal_data": True},
        {"id": "user-accounts-db", "name": "User Accounts Database", "has_personal_data": True},
        {"id": "session-cache", "name": "User Session Redis Cache", "has_personal_data": True},
        {"id": "product-catalog-db", "name": "Product Catalog DB", "has_personal_data": False},
        {"id": "inventory-db", "name": "Inventory Database", "has_personal_data": False},
        {"id": "analytics-warehouse", "name": "Analytics BigQuery Warehouse", "has_personal_data": False},
        {"id": "audit-archive", "name": "System Audit S3 Archive", "has_personal_data": False},
        {"id": "notification-queue", "name": "Notification Event Queue", "has_personal_data": False},
    ]
    return stores

