# demo/demo_app.py
# Simple SNEP client demo

import sys, os
import hashlib
import requests

# Ensure sdk folder is in path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sdk', 'python'))

try:
    from snep_client import SNEPClient
except ImportError:
    # Simple fallback demo client
    class SNEPClient:
        def __init__(self, server_url):
            self.server_url = server_url

        def publish(self, collection, id, data):
            r = requests.post(f"{self.server_url}/{collection}/{id}", json=data)
            return r.json()

        def fetch(self, collection, id):
            r = requests.get(f"{self.server_url}/{collection}/{id}")
            return r.json()

# Demo run
client = SNEPClient("http://127.0.0.1:5000")
example_data = {"recipe": "pumpkin soup", "steps": ["cut pumpkin", "boil", "blend"]}

# Publish
res = client.publish("recipes", "42", example_data)
print("Published:", res)

# Fetch
fetched = client.fetch("recipes", "42")
print("Fetched:", fetched)

# Print SHA256 hash
hash_val = hashlib.sha256(str(fetched).encode()).hexdigest()
print("SHA256 hash of fetched data:", hash_val)