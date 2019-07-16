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
try:
    count = int(sys.argv[1])
except Exception as e:
    count = 100000

class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        # mutexA.acquire()
        mutexA.acquire()

        # mutexA上锁后，延时1秒，等待另外那个线程 把mutexB上锁
        print(self.name+'----do1---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name+'----do1---down----')
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        mutexB.acquire()

        # mutexB上锁后，延时1秒，等待另外那个线程 把mutexA上锁
        print(self.name+'----do2---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()
        print(self.name+'----do2---down----')
        mutexA.release()

        # 对mutexB解锁
        mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
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
- 锁定  ： mutex.acquire()
- 释放  ： mutex.release()
注意： 
- 如果这个锁之前是没有上锁的，那么acquire不会堵塞
- 如果在调用acquire对这个锁上锁之前 它已经被 其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止

10.解决死锁问题:
- 银行家算法
- 超时时间



"""