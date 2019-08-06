#!/usr/bin/python3
# file: with_demo_1.py
# Created by Guang at 19-8-6
# description:

# *-* coding:utf8 *-*


class File(object):

    def __init__(self, file_name, handle_model='rt'):
        self.file_name = file_name
        self.handle_model = handle_model

    def __enter__(self):  # 必须要return 资源对象
        print("entering")
        self.f = open(self.file_name, self.handle_model)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("will exit")
        self.f.close()


"""
__enter__() 方法返回资源对象，这里就是你将要打开的那个文件对象，__exit__() 方法处理一些清除工作。

因为 File 类实现了上下文管理器，现在就可以使用 with 语句

"""

with File('note.md', 'w') as f:
    print("writting")
    f.write("hello world")
