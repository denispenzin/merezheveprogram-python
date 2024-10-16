from bottle import route, run, request, response

@route("/currency", method=["GET"])
def get_currency():
    content_type = request.get_header('Content-Type')

    data = {"currency": "USD", "rate": "41.5"}

    if content_type == 'application/json':
        response.content_type = 'application/json'
        return {"currency": data["currency"], "rate": data["rate"]}
    elif content_type == 'application/xml':
        response.content_type = 'application/xml'
        return f'<response><currency>{data["currency"]}</currency><rate>{data["rate"]}</rate></response>'
    else:
        return "Currency: USD, Rate: 41.5"

if __name__ == "__main__":
    run(host='localhost', port=8000)
