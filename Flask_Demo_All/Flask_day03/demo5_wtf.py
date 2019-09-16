from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo

app = Flask(__name__)
# 关闭csrf验证
app.config['WTF_CSRF_ENABLED'] = True
app.secret_key = "aasdfsdf"


# 自定义注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名：', validators=[InputRequired('请输入用户名')], render_kw={'placeholder': "我是占位文字"})
    password = PasswordField('密码：', validators=[InputRequired('请输入密码')])
    password2 = PasswordField('确认密码：', validators=[InputRequired('请输入确认密码'), EqualTo('password', '两次密码要一致')])
    submit = SubmitField('注册')


@app.route('/')
def index():
    return 'index'


@app.route('/register_wtf', methods=['POST', 'GET'])
def register_wtf():
    register_form = RegisterForm()

    # 使用 wtf表单帮我们做验证
    if register_form.validate_on_submit():
        # 执行注册逻辑
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # 取值方式2
        # username = register_form.username.data

        # 假装做注册操作
        print(username, password, password2)
        return "success"
    else:
        if request.method == "POST":
            flash('参数错误')
    return render_template('temp5_wtf.html', form=register_form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一致")
        else:
            # 假装做注册操作
            print(username, password, password2)
            return "success"
    return render_template('temp5_wtf.html')


if __name__ == '__main__':
    app.run(debug=True)
