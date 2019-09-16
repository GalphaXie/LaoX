from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    my_int = 10
    my_str = "<script>for (var i=0;i<10;i++){alert('哈哈')}</script>"
    my_list = [1, 4, 7, 9, 6]
    my_dict = {
        "id": "1",
        "name": "laowang"
    }
    my_dict_list = [
        {
            "good_name": "大白菜",
            "price": 18,
        },
        {
            "good_name": "白",
            "price": 10,
        }
    ]

    return render_template('demo6_template.html',
                           my_int=my_int,
                           my_str=my_str,
                           my_list=my_list,
                           my_dict=my_dict,
                           my_dict_list=my_dict_list
                           )


# 自定义过滤器
# 方式1：装饰器的形式
@app.template_filter('lireverse')
def do_lireverse(li):
    # 将传入的列表生成一个新的列表
    temp = list(li)
    # 反转
    temp.reverse()
    return temp

# 方式2：直接添加过滤器
app.add_template_filter(do_lireverse, 'lireverse')


if __name__ == '__main__':
    app.run(debug=True)
