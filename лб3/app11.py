from flask import Flask, jsonify, request
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "admin": generate_password_hash("admin_pass"),
    "user": generate_password_hash("user_pass")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

catalog = {
    1: {"name": "Laptop", "price": 1000, "quantity": 5},
    2: {"name": "Smartphone", "price": 500, "quantity": 10},
    3: {"name": "Headphones", "price": 150, "quantity": 15},
}

@app.route('/items', methods=['GET'])
@auth.login_required
def get_items():
    return jsonify(catalog), 200

@app.route('/items/<int:item_id>', methods=['GET'])
@auth.login_required
def get_item(item_id):
    item = catalog.get(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
# для того щоб зайти Логін: admin, пароль: admin_pass 