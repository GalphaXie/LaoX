from flask import Flask
from flask import session

app = Flask(__name__)
# 使用 session 的话，需要配置 secret_key
app.config['SECRET_KEY'] = 'fjkasdjfklasjdfl'


@app.route('/')
def index():
    user_id = session.get('user_id', '')
    user_name = session.get('user_name', '')
    return '%s %s' % (user_id, user_name)


@app.route('/login')
def login():
    # 假装校验成功
    session['user_id'] = "1"
    session['user_name'] = "laowang"
    return 'success'


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
