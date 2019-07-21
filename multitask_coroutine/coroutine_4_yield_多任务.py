# !/usr/bin/python3
#  file: coroutine_4_yield_多任务.py
#  Created by Guang at 19-7-21
#  description:
#
#  *-* coding:utf8 *-*
import time


def worker_1():
    while True:
        time.sleep(0.1)
        print("----------1------------")
        yield


def worker_2():
    while True:
        time.sleep(0.1)
        print("----------2------------")
        yield


if __name__ == '__main__':
    # 要进行一个管理
    t1 = worker_1()  # 注意: 这里不是调用函数, 这里是创建 生成器模板对象.
    t2 = worker_2()
    # 先让t1运行一会，当t1中遇到yield的时候，再返回到24行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中
    # 这样t1/t2/t1/t2的交替运行，最终实现了多任务....协程
    while True:
        next(t1)
        next(t2)
