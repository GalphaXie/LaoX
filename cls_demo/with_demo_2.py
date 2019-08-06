#!/usr/bin/python3
# file: with_demo_2.py
# Created by Guang at 19-8-6
# description:

# *-* coding:utf8 *-*

from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()


# 调用
with my_open('out.txt', 'w') as f:
    f.write("hello python, the simple production of context manager")
