import json
from pathlib import Path


def load_test_data():
    credentials_path = Path(__file__).resolve().parents[1] / "TestData" / "creds.json"
    with credentials_path.open(encoding="utf-8") as data:
        return json.load(data)
