#!/usr/bin/python3
# file: package.py
# Created by Guang at 19-9-17
# description:

# *-* coding:utf8 *-*


# 程序性能分析包
import random
import cProfile


# 测试函数
def f1(li):
    li_1 = sorted(li)
    li_2 = [i for i in li_1 if i < 0.5]
    return [i * i for i in li_2]


def f2(li):
    li_1 = [i for i in li if i < 0.5]
    li_2 = sorted(li_1)
    return [i * i for i in li_2]


def f3(li):
    li_1 = [i * i for i in li]
    li_2 = sorted(li_1)
    return [i for i in li_2 if i < (0.5*0.5)]


lIn = [random.random() for i in range(10000000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')


# 结果 f2, f1, f3
