#!/usr/bin/python3
# file: traversal _dirs.py
# Created by Guang at 19-9-19
# description: 用python写一个列举当前目录及所有子目录下的文件, 并打印出绝对路径

# *-* coding:utf8 *-*

import os


def handle(path):
    # 判断当前的路径是否存在
    if not os.path.exists(path):
        print("传入路径不正确")
        return
    # 如果传入的路径是目录
    dirs = [os.path.join(path, item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

    files = [os.path.join(path, item) for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]

    for d in dirs:
        # 递归调用
        handle(d)

    for f in files:
        print(f)


if __name__ == '__main__':

    path = "/home/guang/Desktop/WorkSpace/LaoX"

    handle(path)






