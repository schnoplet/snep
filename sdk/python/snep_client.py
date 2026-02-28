import requests
import hashlib
import json

class SNEPClient:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def fetch(self, collection, id):
        r = requests.get(f"{self.server_url}/{collection}/{id}")
        r.raise_for_status()
        return r.json()

    def publish(self, collection, id, data):
        r = requests.post(f"{self.server_url}/{collection}/{id}", json=data)
        r.raise_for_status()
        return r.json()

    @staticmethod
    def hash_content(data):
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()