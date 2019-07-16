#!/usr/bin/env python3
# file: thread_demo_1.py
# Created by Guang at 19-7-15
# description:

# *-* coding:utf8 *-*


import threading
import time
import sys


g_num = 0
# count = 100000
count = int(sys.argv[1])

def _sum_1(count):
    global g_num
    for i in range(count):
        g_num += 1
        # time.sleep(0.0001)


def _sum_2(count):
    global g_num
    for i in range(count):
        g_num += 1
        # time.sleep(0.0001)


if __name__ == '__main__':
    t1 = threading.Thread(target=_sum_1, args=(count, ))
    t2 = threading.Thread(target=_sum_2, args=(count, ))

    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("主函数执行结束: {}".format(time.ctime()))
    print("当前g_num的值：{}".format(g_num))



########################################################
"""
笔记：
1.使用多线程并发的操作，花费时间要短很多
2.当调用start()时，才会真正的创建线程，并且开始执行

3.主线程会等待所有的子线程结束后才结束

4.一般工程中更多的是封装 MyThread(threading.Thread) , 重写 run() 方法来实现 多线程; 当执行 线程实例.start() 时，python解释器自动去实现每个线程实例都去执行 run()
    - 当线程的run()方法结束时该线程完成

5.多线程的执行顺序是不确定的。
    - 无法控制线程调度程序，但可以通过别的方式来影响线程调度的方式

6.每一个线程可以指定名字， 如果不指定默认是： Thread-N

7.在一个进程内的所有线程共享全局变量，很方便在多个线程间共享数据， 但是会引发 “资源竞争” 问题， python是线程不安全的, 通过线程同步来解决
8.缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）


"""