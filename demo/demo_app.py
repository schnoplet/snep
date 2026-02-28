# demo/demo_app.py

import json
import hashlib
from sdk.pyclient.snep_client import SNEPClient
from utils.crypto import generate_key

def main():
    key = generate_key()
    client = SNEPClient(key=key)

    example_data = {"recipe": "pumpkin soup", "steps": ["cut pumpkin", "boil", "blend"]}

    print("Publishing data...")
    res = client.publish("recipes", "42", example_data)
    print("Published:", res)

    print("Fetching data...")
    fetched = client.fetch("recipes", "42")
    print("Fetched:", fetched)

    print("SHA256 hash of fetched data:", hashlib.sha256(json.dumps(fetched).encode()).hexdigest())

if __name__ == "__main__":
    main()