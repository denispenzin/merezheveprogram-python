from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    text_data = request.form['text_data']
    with open('data.txt', 'w') as file:
        file.write(text_data)
    
    return 'Дані збережені на сервері'

if __name__ == '__main__':
    app.run(port=8000, debug=True)