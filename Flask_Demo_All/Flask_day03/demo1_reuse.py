from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# 宏
@app.route('/demo1')
def demo1():
    return render_template('temp1_macro.html')


# 继承
@app.route('/demo2')
def demo2():
    return render_template('temp2_extend.html')


@app.route('/news_index')
def demo3():
    return render_template('index.html')


@app.route('/news_detail')
def demo4():
    return render_template('detail.html')


# 包含
@app.route('/demo5')
def demo5():
    return render_template('temp3_include.html')

if __name__ == '__main__':
    app.run(debug=True)
