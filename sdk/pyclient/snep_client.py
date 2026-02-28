# sdk/pyclient/snep_client.py

import requests
import json
from utils.crypto import encrypt_message, decrypt_message

class SNEPClient:
    def __init__(self, key):
        self.key = key
        self.nodes = ["http://localhost:5000", "http://localhost:5001"]

    def publish(self, collection, id, data):
        encrypted = encrypt_message(self.key, json.dumps(data))
        results = []
        for node_url in self.nodes:
            try:
                r = requests.post(f"{node_url}/{collection}/{id}", json={"data": encrypted})
                results.append({"node": node_url, "status": r.status_code})
            except Exception as e:
                results.append({"node": node_url, "error": str(e)})
        return results

    def fetch(self, collection, id):
        for node_url in self.nodes:
            try:
                r = requests.get(f"{node_url}/{collection}/{id}")
                if r.status_code == 200:
                    decrypted = decrypt_message(self.key, r.json()["data"])
                    return json.loads(decrypted)
            except:
                continue
        return None