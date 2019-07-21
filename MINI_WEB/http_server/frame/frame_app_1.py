import time



def login():
    return "welcome xxx login website ....<br> login: %s" % time.ctime()


def logout():
    return "xxx logout website ....<br> logout: %s" % time.ctime()


def profile():
    return "----------file not found --------"


def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/logout.py":
        return logout()
    else:
        return profile()