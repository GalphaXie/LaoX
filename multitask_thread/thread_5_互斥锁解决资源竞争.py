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

# 创建锁
mutex = threading.Lock()
# # 锁定
# mutex.acquire()
# # 释放
# mutex.release()


def _sum_1(count):
    global g_num
    for i in range(count):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("---—_sun_1---g_num=%d" % g_num)


def _sum_2(count):
    global g_num
    for i in range(count):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("---—_sun_2---g_num=%d" % g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=_sum_1, args=(count, ))
    t2 = threading.Thread(target=_sum_2, args=(count, ))

    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

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

9.互斥锁 -- 解决资源竞争
- 创建锁 ： mutex = threading.Lock()
- 锁定  ： mutex.acquire()  # 默认没有锁， 如果之前没有上锁， 此时上锁成功； 如果之前已经上锁， 则阻塞在这里， 直到这个锁被解开。
- 释放  ： mutex.release()
注意： 
- 如果这个锁之前是没有上锁的，那么acquire不会堵塞
- 如果在调用acquire对这个锁上锁之前 它已经被 其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止




"""