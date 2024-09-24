# 模板 jinja2 模板
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name': '张三',
        'age': 18,
        'mylist': [1, 2, 3, 4]
    }
    return render_template('index2.html', data=data)


li = [1, 2, 3, 4, 5]


def list_step(li):
    """自定义过滤器"""
    return li[::2]


# 注册过滤器 第一个值函数的名字,第二个值 写你要用的时候的名字
app.add_template_filter(list_step, 'li2')

print(list_step(li))

if __name__ == '__main__':
    app.run(debug=True)
