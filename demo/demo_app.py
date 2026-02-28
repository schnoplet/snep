import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # ensure SNEP root is on path

import hashlib
import json
from pyclient.snep_client import SNEPClient  # updated import
from utils.crypto import encrypt_message, decrypt_message

def main():
    key = b'mysecretkey123456'  # example symmetric key
    client = SNEPClient(key=key)  # SNEPClient init no longer uses node_urls

    example_data = {
        "recipe": "pumpkin soup",
        "steps": ["cut pumpkin", "boil", "blend"]
    }

    print("Publishing data...")
    published = client.publish("recipes", "42", example_data)
    print("Published:", published)

    print("Fetching data...")
    fetched = client.fetch("recipes", "42")
    print("Fetched:", fetched)

    print("SHA256 hash of fetched data:", hashlib.sha256(json.dumps(fetched).encode()).hexdigest())

if __name__ == "__main__":
    main()