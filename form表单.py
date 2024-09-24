from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单数据
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)
        return render_template('success.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
