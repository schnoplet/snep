# demo/demo_app.py
import sys
import os

# make sure project root is on sys.path so "sdk", "storage", "utils" packages resolve
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import json
import hashlib
from sdk.pyclient.snep_client import SNEPClient

def main():
    key = "supersecretkey"  # demo symmetric key (replace for real use)
    nodes = ["http://localhost:5000", "http://localhost:5001"]  # <-- pass nodes list
    client = SNEPClient(key=key, nodes=nodes)

    example_data = {"recipe": "pumpkin soup", "steps": ["cut pumpkin", "boil", "blend"]}

    print("Publishing data...")
    published = client.publish("recipes", "42", example_data)
    print("Published:", published)

    print("Fetching data...")
    fetched = client.fetch("recipes", "42")
    print("Fetched:", fetched)

    print("SHA256 hash of fetched data:", hashlib.sha256(json.dumps(fetched).encode()).hexdigest())

if __name__ == "__main__":
    main()