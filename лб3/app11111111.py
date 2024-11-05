import sqlite3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

def init_db():
    conn = sqlite3.connect('catalog.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_catalog():
    conn = sqlite3.connect('catalog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = c.fetchall()
    conn.close()
    return {item[0]: {"name": item[1], "price": item[2], "quantity": item[3]} for item in items}

def add_item(name, price, quantity):
    conn = sqlite3.connect('catalog.db')
    c = conn.cursor()
    c.execute('INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    conn.close()

init_db() 

@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def manage_items():
    if request.method == 'GET':
        catalog = get_catalog()
        return jsonify(catalog), 200

    if request.method == 'POST':
        new_item = request.json
        add_item(new_item['name'], new_item['price'], new_item['quantity'])  # Додаємо новий товар
        return jsonify({"message": "Item added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=8000)
