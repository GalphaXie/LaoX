import time


def login():
    return "welcome xxx login website ....<br> login: %s" % time.ctime()


def logout():
    return "xxx logout website ....<br> logout: %s" % time.ctime()


def profile():
    return "----------file not found --------"


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'), ('Location', 'https://www.baidu.com/')]
    start_response(status, response_headers)

    # 由框架来实现业务逻辑
    if environ["FILE_PATH"] == "/login.py":
        return login()
    elif environ["FILE_PATH"] == "/logout.py":
        return logout()
    else:
        return profile()
