from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# загрузка пользорваетелей с файла тхт
def load_users():
    users = {}
    with open('users.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:  
                parts = line.split(':')
                if len(parts) == 2:  
                    username, password = parts
                    users[username] = password
                else:
                    print(f"Неправильний формат рядка: {line}")
    return users

users = load_users()

@auth.verify_password
def verify_password(username, password):
    if username in users and users.get(username) == password:
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
