from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    first = "hello World Mr. Zhang."
    return first.capitalize()

if __name__ == '__main__':
    app.run()
