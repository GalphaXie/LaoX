#!/usr/bin/python3
# file: mini_frame.py
# Created by Guang at 19-7-19
# description:

# *-* coding:utf8 *-*


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return 'Hello World!'


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     # return 'Hello World!'
#     # 编码问题
#     return 'Hello World!  中国...'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html'), ("Content-Type", "text/html;charset=utf-8")])
    # return 'Hello World!'
    # 编码问题
    return 'Hello World!  中国...'