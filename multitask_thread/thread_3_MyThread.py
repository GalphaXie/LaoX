#!/usr/bin/env python3
# file: thread_demo_1.py
# Created by Guang at 19-7-15
# description:

# *-* coding:utf8 *-*


import threading
import time


class MyThread(threading.Thread):
    """自定义的多线程类"""
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + " > " + str(i)  # name属性中保存的是当前线程的名字
            print(msg)

    def other_func(self):
        """在这里定义其他方法"""
        pass


def main():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    main()


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


"""