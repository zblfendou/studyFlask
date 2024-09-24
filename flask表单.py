from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'


# 创建表单类
class Register(FlaskForm):
    user_name = StringField(label='用户名', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField(label="密码", validators=[DataRequired(message='密码不能为空')])
    rePassword = PasswordField(label="二次密码", validators=[DataRequired(message='密码不能为空'),
                                                             EqualTo('password', message='两次密码不一致')])
    submit = SubmitField(label="提交")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 实例化表单
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit(): # 表单验证器
            username = form.user_name.data
            password = form.password.data
            rePassword = form.rePassword.data
            print('提交了表单,用户名是:', username, '密码是:', password, '确认密码是:', rePassword)
        else:
            print('表单验证失败')
        return render_template('register.html', form=form)

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
