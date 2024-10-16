from bottle import route, run, request
@route("/currency", method=["GET"])
def get_currency():
    today = request.query.today
    if today is not None:
        return "USD - 41,5"
    else:
        return "Invalid request", 400

if __name__ == "__main__":
    run(host='localhost', port=8000)
