from flask import Flask

# 应用上下文的变量
from flask import current_app
from flask import g

# 请求上下文中的变量
from flask import request
from flask import session

app = Flask(__name__)

print(request.url)
# print(session.get('user_id',''))


@app.route('/')
def index():
    # print(request.method)
    print(current_app.config.get('DEBUG'))
    return 'index'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
