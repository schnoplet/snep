# nodes/node1.py
# Node 1 server — ensures project root is on sys.path before imports

import sys
import os

# ensure project root is on sys.path so imports work regardless of how the script is started
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from storage.storage import Storage
from flask import Flask, request, jsonify

app = Flask(__name__)
storage = Storage()

@app.route("/recipes/<id>", methods=["POST"])
def add_recipe(id):
    data = request.get_json()
    storage.save(id, data)
    return jsonify({"status": 200})

@app.route("/recipes/<id>", methods=["GET"])
def get_recipe(id):
    data = storage.load(id)
    if data is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(data)

if __name__ == "__main__":
    print("Starting server on port 5000...")
    app.run(port=5000)