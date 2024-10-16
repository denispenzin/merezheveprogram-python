import sqlite3
from flask import Flask, request

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit_data():
    text_data = request.form['text_data']
    
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO texts (text_data) VALUES (?)', (text_data,))
    conn.commit()
    conn.close()
    
    return 'Дані збережені в базі даних'

if __name__ == '__main__':
    init_db()
    app.run(port=8000, debug=True)
