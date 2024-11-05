from flask import Flask, jsonify, request
import os

app = Flask(__name__)

ITEMS_FILE = 'items.txt'

def load_catalog():
    catalog = {}
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    item_id, name, price, quantity = line.split(',')
                    catalog[int(item_id)] = {
                        "name": name,
                        "price": float(price),
                        "quantity": int(quantity)
                    }
    return catalog

def save_catalog(catalog):
    with open(ITEMS_FILE, 'w') as f:
        for item_id, item in catalog.items():
            f.write(f"{item_id},{item['name']},{item['price']},{item['quantity']}\n")

catalog = load_catalog()

@app.route('/items', methods=['GET', 'POST'])
def manage_items():
    if request.method == 'GET':
        return jsonify(catalog), 200

    if request.method == 'POST':
        new_id = max(catalog.keys(), default=0) + 1 
        new_item = request.json
        catalog[new_id] = {
            "name": new_item['name'],
            "price": new_item['price'],
            "quantity": new_item['quantity']
        }
        save_catalog(catalog) 
        return jsonify({"id": new_id, "item": catalog[new_id]}), 201

@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_detail(item_id):
    if request.method == 'GET':
        item = catalog.get(item_id)
        if item:
            return jsonify(item), 200
        else:
            return jsonify({"error": "Item not found"}), 404

    if request.method == 'PUT':
        if item_id in catalog:
            updated_item = request.json
            catalog[item_id] = {
                "name": updated_item['name'],
                "price": updated_item['price'],
                "quantity": updated_item['quantity']
            }
            save_catalog(catalog) 
            return jsonify({"id": item_id, "item": catalog[item_id]}), 200
        else:
            return jsonify({"error": "Item not found"}), 404

    if request.method == 'DELETE':
        if item_id in catalog:
            del catalog[item_id]
            save_catalog(catalog)  
            return jsonify({"message": "Item deleted"}), 200
        else:
            return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
