#!/usr/bin/python3
# file: mini_frame.py
# Created by Guang at 19-7-19
# description:

# *-* coding:utf8 *-*
import time


def login():
    return "Welcome xxx login website!  %s" % time.ctime()


def register():
    return "Welcome xxx register on our website!  %s" % time.ctime()


def profile():
    return "你来到了一片荒原之上..."


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html'), ("Content-Type", "text/html;charset=utf-8")])
    if env["FILE_PATH"] == "/login.py":
        return login()
    elif env["FILE_PATH"] == "/register.py":
        return register()
    else:
        return profile()
