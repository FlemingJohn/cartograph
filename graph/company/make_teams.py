import random


def make_teams():
    random.seed(42)
    teams = [
        {"id": "team-payments", "name": "Payments Platform Team"},
        {"id": "team-platform", "name": "Core Platform & Infrastructure"},
        {"id": "team-identity", "name": "Identity & Access Team"},
        {"id": "team-analytics", "name": "Data & Analytics Team"},
        {"id": "team-security", "name": "Security Operations Team"},
    ]
    return teams

