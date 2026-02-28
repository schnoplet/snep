# storage/storage.py
class Storage:
    def __init__(self):
        # simple in-memory store for demo purposes
        self._store = {}

    def save(self, key, value):
        """Save value under key"""
        self._store[key] = value
        return True

    def load(self, key):
        """Retrieve value by key"""
        return self._store.get(key)

    def delete(self, key):
        """Delete value by key"""
        if key in self._store:
            del self._store[key]
            return True
        return False