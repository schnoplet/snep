from utils.crypto import sha256_hash

class Storage:
    def __init__(self):
        self._store = {}

    def save(self, data: dict) -> str:
        key = sha256_hash(str(data))
        self._store[key] = data
        return key

    def fetch(self, key: str):
        return self._store.get(key)