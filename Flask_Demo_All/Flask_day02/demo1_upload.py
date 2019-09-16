from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

# Address already in use
# ubuntu: netstat -apn | grep 5000 找到5000端口所对应的pid
# kill -9 pid
# mac lsof -i:5000


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('pic')
    file.save('aaaa.png')
    return 'success'


@app.route('/data', methods=['POST'])
def data():
    data = request.data
    print(data)
    return 'ok'



if __name__ == '__main__':
    app.run(debug=True)
