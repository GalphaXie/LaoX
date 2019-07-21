import re


def index():
    with open("./templates/index.html") as f:
        content = f.read()
    add_content = "<h1>这是要添加的内容</h1><br><h2>上次看到一堆垃圾代码恶心到我了...</h2>"
    content = re.sub(r"\{%content%\}", add_content, content)
    return content


def center():
    with open("./templates/center.html") as f:
        content = f.read()
        add_content = "\r\n这是要添加的内容\r\n上次看到一堆垃圾代码\r\n恶心到我了..."
        content = re.sub(r"\{%content%\}", add_content, content)
        return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'
