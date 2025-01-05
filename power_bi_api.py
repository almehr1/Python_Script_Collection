from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample dataset (replace with a database connection if needed)
data = [
    {"id": 1, "name": "Product A", "price": 100},
    {"id": 2, "name": "Product B", "price": 150},
    {"id": 3, "name": "Product C", "price": 200},
]

# Endpoint to fetch all data
@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(data)

# Endpoint to fetch a specific item by ID
@app.route("/api/data/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Endpoint to add new data
@app.route("/api/data", methods=["POST"])
def add_data():
    if not request.json or not "name" in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_item = {
        "id": len(data) + 1,
        "name": request.json["name"],
        "price": request.json.get("price", 0),
    }
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)
