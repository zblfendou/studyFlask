# flask 数据库
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)


# 数据模型
class User(db.Model):
    '''用户表'''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Movie(db.Model):
    '''电影表'''
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    # 表关系 ForeignKey 用来关联到另外一张表
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


if __name__ == '__main__':
    # 清除所有的表
    db.drop_all()
    # 创建所有的表
    db.create_all()

    # 创建对象插入数据
    user1 = User(name='zhangsan', email='123@qq.com')
    user2 = User(name='lisi', email='456@qq.com')
    db.session.add_all([user1, user2])

    movie1 = Movie(title='霸王别姬', user_id=user1.id)
    movie2 = Movie(title='大话西游', user_id=user2.id)
    db.session.add_all([movie1, movie2])
    # 提交事务
    db.session.commit()
