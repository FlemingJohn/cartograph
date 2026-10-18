import os

REQUIRED_SETTINGS = ["FALKORDB_HOST", "FALKORDB_PORT", "FALKORDB_PASSWORD", "GOOGLE_API_KEY"]


def check_settings() -> None:
    missing = [name for name in REQUIRED_SETTINGS if not os.environ.get(name)]
    if missing:
        raise RuntimeError(f"Fill these in .env before starting: {', '.join(missing)}")
