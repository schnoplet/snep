from .storage import Storage
from flask import Flask, request, jsonify

app = Flask(__name__)
store = Storage()

@app.route("/<collection>/<id>", methods=["GET"])
def get_object(collection, id):
    obj = store.get(f"{collection}/{id}")
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj)

@app.route("/<collection>/<id>", methods=["POST"])
def put_object(collection, id):
    data = request.json
    store.put(f"{collection}/{id}", data)
    return jsonify({"status": "ok"}), 201

if __name__ == "__main__":
    app.run(port=5000)