from storage.storage import Storage
from flask import Flask, request, jsonify
import sys

app = Flask(__name__)
storage = Storage()

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

@app.route("/<collection>/<item_id>", methods=["POST"])
def publish(collection, item_id):
    data = request.json
    storage.save(collection, item_id, data)
    return jsonify({"status": "ok"})

@app.route("/<collection>/<item_id>", methods=["GET"])
def fetch(collection, item_id):
    data = storage.load(collection, item_id)
    if data:
        return jsonify(data)
    return jsonify({"status": "not found"}), 404

if __name__ == "__main__":
    print(f"Starting server on port {PORT}...")
    app.run(port=PORT)