from flask import Flask, jsonify
from flask import json
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    return 'demo1'


# 给路由添加参数，格式就是 <参数名>
# 并且视图函数需要接收这个参数
@app.route('/user/<int:user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id


@app.route('/demo3', methods=['GET', 'POST'])
def demo3():
    return 'demo3 %s' % request.method


@app.route('/json')
def demo4():
    json_dict = {
        "name": "laowang",
        "age": 18
    }
    # 使用JSON.dumps将字典转成JSON字符串
    # result = json.dumps(json_dict)
    # 使用JSON.loads将JSON字符串转成字典
    # test_dict = json.loads('{"age": 18, "name": "laowang"}')

    # with open('aaaa.json', 'w') as fp:
    #     json.dump(json_dict, fp)
    return json.dumps(json_dict)
    # jsonify会指定响应内容的数据格式(告诉客户端我返回给你的数据格式是什么)
    return jsonify(json_dict)


@app.route('/redirect')
def demo5():
    # 重定向到自己写的视图函数
    # url_for：取到指定视图函数所对应的路由URL，并且可以携带参数
    return redirect(url_for('demo2', user_id=123))
    # 重定向到黑马
    # return redirect('http://www.itheima.com')


# 返回自定义的状态码
@app.route('/demo6')
def demo6():
    return 'demo6', 666


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
