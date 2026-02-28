from storage import Storage  # updated import
from flask import Flask, request, jsonify

app = Flask(__name__)
storage = Storage()

@app.route("/recipes/<recipe_id>", methods=["GET", "POST"])
def handle_recipe(recipe_id):
    if request.method == "POST":
        storage.save(recipe_id, request.json)
        return jsonify({"status": 200})
    else:
        return jsonify(storage.load(recipe_id) or {})

if __name__ == "__main__":
    print("Starting server on port 5001...")
    app.run(port=5001)