from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():
    content_type = request.headers.get('Content-Type')
    
    data = {"currency": "USD", "rate": "41.5"}

    if content_type == 'application/json':
        return jsonify(data)
    elif content_type == 'application/xml':
        xml_response = f'<response><currency>{data["currency"]}</currency><rate>{data["rate"]}</rate></response>'
        return Response(xml_response, mimetype='application/xml')
    else:
        return "Currency: USD, Rate: 41.5"

if __name__ == "__main__":
    app.run(port=8000)
