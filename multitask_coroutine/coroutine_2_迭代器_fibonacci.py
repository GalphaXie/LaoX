#!/usr/bin/python3
# file: coroutine_1_迭代器_1.py
# Created by Guang at 19-7-21
# description:

# *-* coding:utf8 *-*
import time
from collections import Iterable
from collections import Iterator


class Fibonacci(object):

    def __init__(self, all_num):
        self.all_num = all_num
        self.a = 1
        self.b = 1
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return self.a
        else:
            raise StopIteration


fibonacci = Fibonacci(10)
for i in fibonacci:
    print(i)
