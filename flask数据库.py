import json

from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'  # 密码
# 协议：mysql+pymysql
# 用户名：selfsiteuser
# 密码：selfsiteuserpassword1QASW2
# IP地址：10.24.46.117
# 端口：3306
# 数据库名：flask_db #这里的数据库需要提前建好
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://selfsiteuser:selfsiteuserpassword1QASW2@10.24.46.117:3306/flask_db?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


# 新建表Role
class Role(db.Model):
    __tablename__ = 'roles'  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id字段，int类型，主键
    name = db.Column(db.String(64), unique=True)  # name字段，字符串类型，唯一
    users = db.relationship('User', backref='role', lazy='dynamic')  # 外键关系，动态更新

    def to_dict(self):
        return {'id': self.id,
                'name': self.name}

    def __repr__(self):
        return '<Role(id="%s", name="%s")>' % (self.id, self.name)


# 新建表User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)  # 索引
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 外键

    def __repr__(self):
        return "<User(id='%s', username='%s')>" % (self.id, self.username)


@app.route('/initDb', methods=['GET', 'POST'])
def initDb():
    print("Starting the application...")
    print("Before creating tables...")
    db.drop_all()
    print("Tables dropped successfully!")
    db.create_all()
    print("Tables created successfully!")
    return 'ok'


@app.route('/addRole', methods=['POST', 'GET'])
def add_role():
    role = Role(name='管理员1')
    db.session.add(role)
    db.session.commit()
    return 'add success'


@app.route('/queryRoles', methods=['GET', 'POST'])
def queryRoles():
    role_all = db.session.query(Role).all()
    roles_list = [role.to_dict() for role in role_all]
    response_json = json.dumps(roles_list, ensure_ascii=False)
    return Response(response_json, content_type='application/json;charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True)
