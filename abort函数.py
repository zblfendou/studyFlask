# raise 主动抛出异常
# abort 在网页中抛出异常
from flask import Flask, abort, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == '张三' and password == '123':
            print('登录成功')
            return render_template('success.html')
        else:
            print('登录失败')
            abort(404)
    return None


# 自定义错误处理方法
@app.errorhandler(404)
def handle_404_error(err):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
