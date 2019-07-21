#!/usr/bin/env python3
# file: thread_demo_1.py
# Created by Guang at 19-7-15
# description:

# *-* coding:utf8 *-*
from multiprocessing import Pool
import random
import time
import os


def worker(msg):
    t_start = time.time()
    print("%s 开始执行， 进程号 %d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


if __name__ == '__main__':
    # 1.创建进程池
    po = Pool(3)  # 当有任务的时候， 才开始创建进程池， 然后同时开始执行3个进程
    for i in range(10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        po.apply_async(worker, (i, ))

    print("--------start--------------")
    po.close()  # 关闭进程池， 关闭后 po 不再接收新的请求
    po.join()  # 等待po中所有的子进程执行完成， 必须放在 close() 方法之后
    print("--------end--------------")


########################################################
"""
笔记：
1.po = Pool(3)  # 当添加任务任务 apply_async 的时候， 才开始创建进程池， 然后同时开始执行3个子进程
 - 在执行po = Pool(3)的时候 并为创建 进程池
 - apply_async 才开始真正的调度和执行多进程。
2.注意事项： 不同于前面的主进程会等子进程全部执行结束之后才会结束； 由Poll()创建的多进程， 主进程不会等待， 所有必须要 po.join()
3.po.close()  # 关闭进程池， 关闭后 po 不再接收新的请求
4.po.join()  # 等待po中所有的子进程执行完成， 必须放在 close() 方法之后

"""