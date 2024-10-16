from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

def get_currency_rate(date_str):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date_str}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']  
    return None

@app.route("/currency", methods=["GET"])
def currency():
    param = request.args.get('param')

    if param == "today":
        date_str = datetime.now().strftime("%Y%m%d")
        rate = get_currency_rate(date_str)
        if rate:
            return jsonify({"date": "today", "currency": "USD", "rate": rate})
        else:
            return jsonify({"error": "Unable to retrieve today's rate"}), 500

    elif param == "yesterday":
        yesterday = datetime.now() - timedelta(days=1)
        date_str = yesterday.strftime("%Y%m%d")
        rate = get_currency_rate(date_str)
        if rate:
            return jsonify({"date": "yesterday", "currency": "USD", "rate": rate})
        else:
            return jsonify({"error": "Unable to retrieve yesterday's rate"}), 500

    else:

        return jsonify({"error": "Invalid param. Use 'today' or 'yesterday'"}), 400

if __name__ == "__main__":
    app.run(port=8000)
