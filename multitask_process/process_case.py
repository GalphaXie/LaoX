#!/usr/bin/python3
# file: process_case.py
# Created by Guang at 19-7-21
# description:

# *-* coding:utf8 *-*

from multiprocessing import Manager, Pool
import os
import time


def handle_copy(queue, file_name, old_folder_name, new_folder_name):
    """处理具体的文件copy"""
    # 注意： 子进程如果出现异常, 不会正常完成任务, 也不会提示.
    # 解决方案： 写程序是一步一步的去实现。从主体到细节
    # print("模拟 从 %s 到 %s 的文件 %s 拷贝" % (old_folder_name, new_folder_name, file_name))

    try:
        with open(old_folder_name + "/" + file_name, 'rb') as f:
            content = f.read()
    except Exception as e:
        print("读取文件失败")
    else:
        with open(new_folder_name + "/" + file_name, 'wb') as f:
            f.write(content)
        # 拷贝结束就将文件名放入队列中
        queue.put(file_name)


def main():
    """主程序"""
    # 1.获取用户要copy的文件夹的名字
    old_folder_name = input("请输入待拷贝的文件夹的名字：")
    if not os.path.isdir(old_folder_name):
        print("待拷贝的文件夹不存在")
        return
    # 2.创建一个新的文件夹
    new_folder_name = old_folder_name + "复件"
    try:
        os.mkdir(new_folder_name)
    except FileExistsError:
        pass

    # 3.查看原文件夹下有那些文件
    file_names = os.listdir(old_folder_name)

    # 4 通过进程池来进行子进程的创建和管理
    po = Pool(10)
    # 5. 增加进程的消息队列, 让子进程向主进程汇报完成copy的文件名
    queue = Manager().Queue()

    for file_name in file_names:
        po.apply_async(handle_copy, args=(queue, file_name, old_folder_name, new_folder_name))
    po.close()
    # po.join()  # 通过下面的 while True 来实现

    # 5.主进程 人性化 的显示进度条
    # 进程间通信： 子进程 和 主进程 间进行通信
    # queue = Manager().Queue()
    all_file_len = len(file_names)
    while True:
        file_name = queue.get()
        # print("已经完成%s的拷贝" % file_name)
        file_names.remove(file_name)
        res = (all_file_len - len(file_names)) / all_file_len * 100
        print("\r当前拷贝进度：%.2f%%" % res, end='')
        if not file_names:
            break
    print()


if __name__ == '__main__':
    main()

"""
思想：
1. 程序不是一蹴而就的， 要先设计后开发， 先整体框架再具体的细节， 同时积累开发过程中调试的经验， 边写边调试
"""