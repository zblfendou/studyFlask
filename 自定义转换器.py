# <int:id> int 转换器
# 自定义转换器 <> 提取参数
import typing as t

from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类方法
        super(RegexConverter, self).__init__(url_map)
        # 保存正则表达式属性
        self.regex = regex

    def to_python(self, value):
        print('to_python 方法被调用')
        return value


# 将自定义的转换器类添加到flask应用中去
app.url_map.converters['re'] = RegexConverter


@app.route('/index/<re("123"):value>')
def index(value):
    return 'hello'


app.url_map.converters['re'] = RegexConverter
