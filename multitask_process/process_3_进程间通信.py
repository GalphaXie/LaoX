#!/usr/bin/env python3
# file: thread_demo_1.py
# Created by Guang at 19-7-15
# description:

# *-* coding:utf8 *-*


import multiprocessing
import random
import time


def download_data(q):
    for i in [10, 11, 12, 15]:
        if not q.full():
            q.put(i)
        time.sleep(random.random())


def analysis_data(q):
    container = []
    while True:
        if not q.empty():
            container.append(q.get())
            time.sleep(random.random())
        else:
            break
    print("模拟数据处理: %s" % container)


if __name__ == '__main__':
    # 1.父进程创建任务队列Queue, 并将引用传递给各个子进程
    q = multiprocessing.Queue(3)  # 参数3表示队列饱和状态下最多存入的数据， 如果不传递参数或者参数为负数，那么则存入数据无限制， 以内存上限为限制
    p1 = multiprocessing.Process(target=download_data, args=(q, ))
    p2 = multiprocessing.Process(target=analysis_data, args=(q, ))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("结束...")


########################################################
"""
笔记：
1.使用多线程并发的操作，花费时间要短很多
2.当调用start()时，才会真正的创建线程，并且开始执行

3.主线程会等待所有的子线程结束后才结束


"""