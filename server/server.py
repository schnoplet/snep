# server/server.py
# Demo SNEP server — no venv needed, works directly

import sys, os
# Ensure server folder is in path so storage.py is found
sys.path.append(os.path.dirname(__file__))

from storage import Storage
from flask import Flask, request, jsonify

app = Flask(__name__)
storage = Storage()

@app.route('/<collection>/<id>', methods=['POST'])
def save_data(collection, id):
    data = request.get_json()
    storage.save(collection, id, data)
    return jsonify({"status": "ok"}), 200

@app.route('/<collection>/<id>', methods=['GET'])
def get_data(collection, id):
    data = storage.fetch(collection, id)
    if data is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(data), 200

if __name__ == "__main__":
    print("Starting SNEP demo server on http://127.0.0.1:5000/")
    app.run(host="127.0.0.1", port=5000)