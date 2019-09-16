from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

# Address already in use
# ubuntu: netstat -apn | grep 5000 找到5000端口所对应的pid
# kill -9 pid
# mac lsof -i:5000


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(request.method)
    print(request.url)
    print(request.headers)
    # file = request.files.get('pic')
    # file.save('aaa.jpg')
    return 'success'


@app.route('/data', methods=['POST'])
def data():
    data = request.data
    print(data)
    return 'success'
    # name = request.form.get('name')
    # age = request.form.get('age')
    # data = {
    #         'name': name,
    #         'age': age
    #         }
    # return jsonify(data)


@app.route('/args')
def args():
    name = request.args.get('name')
    age = request.args.get('age')
    data = {
        'name': name,
        'age': age
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
