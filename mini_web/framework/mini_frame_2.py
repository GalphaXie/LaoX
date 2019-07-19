#!/usr/bin/python3
# file: mini_frame.py
# Created by Guang at 19-7-19
# description:

# *-* coding:utf8 *-*
import time


def login():
    return "Welcome xxx to website!  %s" % time.ctime()


def register():
    return "Welcome xxx register on our website!  %s" % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "not found you page ..."
    # return "application"

