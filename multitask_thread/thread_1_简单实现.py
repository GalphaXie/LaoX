#!/usr/bin/env python3
# file: thread_demo_1.py
# Created by Guang at 19-7-15
# description:

# *-* coding:utf8 *-*


import threading
import time


def func1():
    for i in range(5):
        print("这是一个线程测试函数func1")
        time.sleep(1)


def func2():
    for i in range(5):
        print("这是一个线程测试函数func2")
        time.sleep(1)


if __name__ == '__main__':
    print("-------主线程执行开始:{}-----------------".format(time.ctime()))
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()  #启动线程，即让线程开始执行
    t2.start()

    time.sleep(5)
    print("-------主线程执行结束:{}-----------------".format(time.ctime()))


########################################################
"""
笔记：
1.使用多线程并发的操作，花费时间要短很多
2.当调用start()时，才会真正的创建线程，并且开始执行

3.主线程会等待所有的子线程结束后才结束


"""