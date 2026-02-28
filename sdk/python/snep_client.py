import requests
from utils.crypto import encrypt_message, decrypt_message

class SNEPClient:
    def __init__(self, key, node_urls=None):
        self.key = key
        # support multiple nodes for replication
        self.node_urls = node_urls or ["http://localhost:5000"]

    def publish(self, collection, item_id, data):
        """Try publishing to each node until successful."""
        for url in self.node_urls:
            try:
                r = requests.post(f"{url}/{collection}/{item_id}", json=data, timeout=2)
                if r.status_code == 200:
                    return {"node": url, "status": "ok"}
            except requests.RequestException:
                continue
        return {"status": "failed", "reason": "all nodes unreachable"}

    def fetch(self, collection, item_id):
        """Fetch from the first available node."""
        for url in self.node_urls:
            try:
                r = requests.get(f"{url}/{collection}/{item_id}", timeout=2)
                if r.status_code == 200:
                    return r.json()
            except requests.RequestException:
                continue
        return None

    def fetch_from_node(self, node_url, collection, item_id):
        """Fetch from a specific node (optional)."""
        try:
            r = requests.get(f"{node_url}/{collection}/{item_id}", timeout=2)
            if r.status_code == 200:
                return r.json()
        except requests.RequestException:
            return None