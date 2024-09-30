import os
import sys

import click
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

# 初始化 Flask 应用
app = Flask(__name__)

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 配置数据库连接
dev_db = prefix + os.path.join(app.root_path, 'student.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', dev_db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev key')

# bp = Blueprint('bp', __name__)
# 注册蓝图
# app.register_blueprint(bp, url_prefix='/student', static_folder='static', template_folder='templates')

# 初始化数据库连接
db = SQLAlchemy(app)

students = [
    {'name': '张三', 'chinese': 80, 'math': 90, 'english': 100},
    {'name': '王五', 'chinese': 92, 'math': 87, 'english': 80},
    {'name': '赵六', 'chinese': 80, 'math': 88, 'english': 95},
    {'name': '李四', 'chinese': 86, 'math': 94, 'english': 60}
]


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    chinese = db.Column(db.Integer, nullable=False)
    math = db.Column(db.Integer, nullable=False)
    english = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Student(name='%s', math='%s', chinese='%s', english='%s')>" % (
            self.name, self.math, self.chinese, self.english)


@app.cli.command('init')
@click.option('--drop', is_flag=True, help='Create after drop.')
def init(drop):
    """初始化数据库并插入数据"""
    if drop:
        db.drop_all()  # 删除所有表
    db.create_all()  # 创建所有表

    # 将字典数据转化为 Student 模型对象
    for student in students:
        new_student = Student(
            name=student['name'],
            chinese=student['chinese'],
            math=student['math'],
            english=student['english']
        )
        db.session.add(new_student)

    db.session.commit()  # 提交更改
    click.echo('Initialized the database and added student data.')
