from flask import Flask
from flask import flash
from flask import g
from flask import render_template
from flask import session

app = Flask(__name__)
app.secret_key = "asdfasdfasdf"


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    g.name = "xiaohua"
    session['name'] = "laowang"

    flash('我是闪现的消息')

    return render_template('temp4_special.html')


if __name__ == '__main__':
    app.run(debug=True)
