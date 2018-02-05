# app.py

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods = ['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign in</button></p>
              </form>'''

# button中最后字符串部分不能有空格，否则会显示异常，也就是sign in后面”

@app.route('/signin', methods = ['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == '123':
        return '<h3>hello, admin</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()
              
