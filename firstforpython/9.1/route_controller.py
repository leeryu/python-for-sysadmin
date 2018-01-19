from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root=".")

run(host='127.0.0.1', port=9999)