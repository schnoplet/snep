class Storage:
    def __init__(self):
        self.db = {}

    def save(self, collection, item_id, data):
        if collection not in self.db:
            self.db[collection] = {}
        self.db[collection][item_id] = data
        return True

    def load(self, collection, item_id):
        try:
            return self.db[collection][item_id]
        except KeyError:
            return None