from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 创建manager与app进行关联
manager = Manager(app)
# 需求：可以通过命令行在运行的时候指定运行的端口


@app.route('/')
def index():
    return 'index222222'


if __name__ == '__main__':
    # 使用 manager 去运行
    manager.run()
