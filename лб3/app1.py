from flask import Flask, jsonify, request

app = Flask(__name__)

catalog = {
    1: {"name": "Laptop", "price": 1000, "quantity": 5},
    2: {"name": "Smartphone", "price": 500, "quantity": 10},
    3: {"name": "Headphones", "price": 150, "quantity": 15},
}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(catalog), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = catalog.get(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)


# для отримання всіх товарів http://localhost:8000/items а для вибору товару http://localhost:8000/items/1 або 2 та 3