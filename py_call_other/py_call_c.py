#!/usr/bin/python3
# file: py_call_c.py
# Created by Guang at 19-8-16
# description:

# *-* coding:utf8 *-*

from ctypes import *


# 加载动态库
lib = cdll.LoadLibrary("./xxxx.so")


func = lib.DeadLoop
