import requests
import hashlib
import json

class SNEPClient:
    def __init__(self, key, nodes):
        self.key = key
        self.nodes = nodes

    def publish(self, collection, id, data):
        results = []
        for node in self.nodes:
            try:
                r = requests.post(f"{node}/{collection}/{id}", json=data)
                results.append({"node": node, "status": r.status_code})
            except Exception as e:
                results.append({"node": node, "error": str(e)})
        return results

    def fetch(self, collection, id):
        for node in self.nodes:
            try:
                r = requests.get(f"{node}/{collection}/{id}")
                if r.status_code == 200:
                    return r.json()
            except:
                continue
        return {}