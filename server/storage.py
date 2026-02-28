# server/storage.py
# Simple in-memory storage for SNEP demo

class Storage:
    def __init__(self):
        self._data = {}

    def save(self, collection, id, data):
        if collection not in self._data:
            self._data[collection] = {}
        self._data[collection][id] = data
        return True

    def fetch(self, collection, id):
        return self._data.get(collection, {}).get(id, None)