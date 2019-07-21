# !/usr/bin/python3
#  file: coroutine_4_yield_多任务.py
#  Created by Guang at 19-7-21
#  description:
#
#  *-* coding:utf8 *-*
from greenlet import greenlet
import time


def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

# 切换到gr1中运行
gr1.switch()
