from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    first = "hello World Mr. Zhang."
    return first.capitalize()


# string 接收任何不包含斜杠的文本
# int 接收整数
# float 接收浮点数
# path 接收任何包含斜杠的文本

@app.route('/user/<float:id>', methods=['GET', 'POST'])
def hi(id):
    if id == 1:
        return 'java'
    if id == 2:
        return 'python'
    if id == 3:
        return 'php'
    return 'hi hi'


if __name__ == '__main__':
    app.run(debug=True)
