from flask import Flask, request

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():
    today = request.args.get('today')
    if today is not None:
        return "USD - 41,5"
    else:
        return "Invalid request", 400

if __name__ == "__main__":
    app.run(port=8000)
