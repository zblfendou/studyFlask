# 重定向 302

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/index')
def index():
    return redirect(url_for('hello'))
@app.route('/')
def hello():
    return 'this is hello'


if __name__ == '__main__':
    app.run(debug=True)