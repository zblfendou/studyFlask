from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from statsmodels.sandbox.distributions.genpareto import method

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'  # 密码
# 协议：mysql+pymysql
# 用户名：selfsiteuser
# 密码：selfsiteuserpassword1QASW2
# IP地址：10.24.46.117
# 端口：3306
# 数据库名：flask_db #这里的数据库需要提前建好
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://selfsiteuser:selfsiteuserpassword1QASW2@10.24.46.117:3306/flask_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


# 新建表Role
class Role(db.Model):
    __tablename__ = 'roles'  # 表名
    id = db.Column(db.Integer, primary_key=True)  # id字段，int类型，主键
    name = db.Column(db.String(64), unique=True)  # name字段，字符串类型，唯一
    users = db.relationship('User', backref='role', lazy='dynamic')  # 外键关系，动态更新

    def __repr__(self):  # 相当于toString
        return '<Role %r>' % self.name


# 新建表User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)  # 索引
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 外键

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/initDb', methods=['GET', 'POST'])
def initDb():
    print("Starting the application...")
    print("Before creating tables...")
    db.drop_all()
    print("Tables dropped successfully!")
    db.create_all()
    print("Tables created successfully!")
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
