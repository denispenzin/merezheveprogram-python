import sqlite3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)',
                   (username, generate_password_hash(password)))
    conn.commit()
    conn.close()

@auth.verify_password
def verify_password(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[0], password):
        return username

init_db()
add_user("admin", "admin_pass")
add_user("user", "user_pass")

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
