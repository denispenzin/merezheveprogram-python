from bottle import route, run
@route('/')
def hello():
    return "Hello, Bottle!"

if __name__ == '__main__':
    run(host='localhost', port=8000)