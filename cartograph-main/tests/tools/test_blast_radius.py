from tools.handlers.blast_radius import blast_radius


def test_blast_radius():
    res = blast_radius("payments-service", max_hops=3)
    data_stores = res["result"]
    assert len(data_stores) > 0
    card_store = next((d for d in data_stores if d["data_store_id"] == "customer-cards"), None)
    assert card_store is not None
    assert card_store["has_personal_data"] is True
    assert card_store["hop_count"] == 2

