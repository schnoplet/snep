from flask import Flask, request, jsonify
from storage.storage import Storage
import requests

app = Flask(__name__)
db = Storage()

# peers for automatic replication (node2 -> node1)
peers = ["http://localhost:5000"]

@app.route("/<collection>/<item_id>", methods=["POST"])
def publish(collection, item_id):
    data = request.json
    db.save(collection, item_id, data)

    # replicate to peers
    for peer in peers:
        try:
            requests.post(f"{peer}/{collection}/{item_id}", json=data, timeout=1)
        except:
            pass  # ignore if peer offline

    return jsonify({"status": "ok"})

@app.route("/<collection>/<item_id>", methods=["GET"])
def fetch(collection, item_id):
    data = db.get(collection, item_id)
    if data:
        return jsonify(data)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    print(f"Starting node2 server on port {port}...")
    app.run(port=port)