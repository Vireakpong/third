#\app.py
from bottle import route, run

@route('/')
def mainn():
    return "Hello world"

run (host = 'localhost', port=9000, debug = True, reloader = True)