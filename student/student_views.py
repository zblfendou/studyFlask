from flask import render_template, request, redirect
from . import students
from . import bp


@bp.route('/')
def index():
    return redirect('/login')


@bp.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)
        return redirect('/admin')
    return render_template('login.html')


@bp.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', students=students)


# 新增
@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        chinese = request.form.get('chinese')
        english = request.form.get('english')
        math = request.form.get('math')
        students.append({'name': name, 'chinese': chinese, 'english': english, 'math': math})
        return redirect('/admin')
    return render_template('add.html')


# 删除
@bp.route('/del', methods=['GET', 'POST'])
def del_stu():
    name = request.args.get('name')
    for stu in students:
        if stu['name'] == name:
            students.remove(stu)
    return redirect('/admin')


# 编辑
@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        name = request.args.get('name')
        for stu in students:
            if stu['name'] == name:
                return render_template('edit.html', stu=stu)
    else:
        name = request.form.get('name')
        chinese = request.form.get('chinese')
        english = request.form.get('english')
        math = request.form.get('math')
        for stu in students:
            if stu['name'] == name:
                stu['chinese'] = chinese
                stu['english'] = english
                stu['math'] = math
        return redirect('/admin')
