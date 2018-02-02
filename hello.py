# hello.py

def application(environ, start_responseN):
    start_responseN('200 OK', [('Content-Type', 'text/html')])
    #start_response是在哪里定义的
    return [b'<h1>Hello, web</h1>']
