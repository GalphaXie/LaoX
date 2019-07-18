#!/usr/bin/env python3
# file: thread_demo_1.py
# Created by Guang at 19-7-15
# description:

# *-* coding:utf8 *-*


import multiprocessing
import time

num = 100
nums = [11, 22, 33]


def func1(num, nums):
    num = 200
    nums.append(44)


def func2(num, nums):
    print(num)
    print(nums)


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=func1, args=(num, nums))
    t2 = multiprocessing.Process(target=func2, args=(num, nums))
    t1.start()
    t2.start()

    time.sleep(5)



########################################################
"""
笔记：
1.使用多线程并发的操作，花费时间要短很多
2.当调用start()时，才会真正的创建线程，并且开始执行

3.主线程会等待所有的子线程结束后才结束


"""