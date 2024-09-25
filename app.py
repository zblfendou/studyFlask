from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return redirect('/admin')
    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')


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
