#!/usr/bin/python3
# file: coroutine_1_迭代器_1.py
# Created by Guang at 19-7-21
# description:

# *-* coding:utf8 *-*
import time
from collections import Iterable
from collections import Iterator


class ClassMate(object):
    def __init__(self):
        self.names = list()
        self.count = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个　可以迭代的对象，即可以使用for遍历取值，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.count < len(self.names):
            ret = self.names[self.count]
            self.count += 1
            return ret
        else:
            raise StopIteration


class_mate = ClassMate()
class_mate.add("张三")
class_mate.add("李四")
class_mate.add("黑匣子")

# print("判断class_mate是否是可迭代对象: %s" % isinstance(class_mate, Iterable))
# class_mate_iter = iter(class_mate)
#
# print("判断class_mate是否是迭代器: %s" % isinstance(class_mate_iter, Iterator))
# print(next(class_mate_iter))

for name in class_mate:
    print(name)
    time.sleep(1)

"""笔记：
1.for循环本质:
- 1. 判断被遍历的对象是否是 可迭代对象
- 2. iter(可迭代对象) 实质上是调用 可迭代对象.__iter__() 方法， 判断该方法的返回值是否是 迭代器
- 3. next(迭代器) 实质上上是 调用上述 iter() 的返回的迭代器的 __next__() 方法， 依次获取next()的返回值
- 4. 当迭代到最后一个元素， 则 抛出 StopIteration 异常， 该异常能自动被 for...in... 捕获， 然后终止遍历操作。

"""