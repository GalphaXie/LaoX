"""
分析：
    随着后期的扩展性， 框架中的业务逻辑应该是可以 由开发者方便扩展的， 比如 application函数内部 的 分支语句不应该过长...
解决方法：
- 1.字典映射
- 2.装饰器


"""

import re


template_root = "./templates"

URL_FUNC_DICT = dict()


def route(url):
    def wrapper(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return wrapper


# @route("/index.py")
@route("/index.html")
def index(file_name: str):
    file_name = file_name.replace(".py", ".html")
    with open(template_root + file_name) as f:
        content = f.read()
    my_stock_info = "<h1>这是要添加的内容</h1><br><h2>上次看到一堆垃圾代码恶心到我了...</h2>"
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content


# @route("/center.py")
@route("/center.html")
def center(file_name: str):
    file_name = file_name.replace(".py", ".html")
    with open(template_root + file_name) as f:
        content = f.read()
    my_stock_info = "\r\n这是要添加的内容\r\n上次看到一堆垃圾代码\r\n恶心到我了..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content


# 配置函数引用到字典中
# URL_FUNC_DICT = {
#     "/index.py": index,
#     "/center.py": center
# }


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"
    # 这里既可以通过 if func: 来进行None判断， 也可以采用 try...except ， 采用后者还有一个好处是可以捕获 业务函数内部的异常
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # else:
    #     return 'Hello World! 我爱你中国....'
    try:
        return URL_FUNC_DICT[file_name](file_name)
    except Exception as e:
        print("异常： %s" % e)
        return 'Hello World! 我爱你中国....'



