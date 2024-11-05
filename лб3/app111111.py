from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
def load_users():
    users = {}
    with open('users.txt', 'r') as f:
        for line in f:
            line = line.strip() 
            if line: 
                username, password = line.split(':')  
                users[username] = password
    return users

users = load_users()

@auth.verify_password
def verify_password(username, password):
    return username in users and users[username] == password


catalog = {
    1: {"name": "Laptop", "price": 1000, "quantity": 5},
    2: {"name": "Smartphone", "price": 500, "quantity": 10},
    3: {"name": "Headphones", "price": 150, "quantity": 15},
}

@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def manage_items():
    if request.method == 'GET':
        return jsonify(catalog), 200  

    if request.method == 'POST':
        new_item = request.json  
        new_id = max(catalog.keys()) + 1  
        catalog[new_id] = new_item
        return jsonify({"id": new_id, "item": new_item}), 201  
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
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
            catalog[item_id] = updated_item
            return jsonify({"id": item_id, "item": updated_item}), 200  #
        else:
            return jsonify({"error": "Item not found"}), 404

    if request.method == 'DELETE':
        if item_id in catalog:
            del catalog[item_id]
            return jsonify({"message": "Item deleted"}), 200 
        else:
            return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
