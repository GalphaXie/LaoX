#!/usr/bin/python3
# file: 03-顺序表反转.py
# Created by Guang at 19-10-7
# description: 根据顺序表的原理,设计一个 时间复杂度在O(N)以内, 空间复杂度在O(N)以内的 算法实现

# *-* coding:utf8 *-*


class OrderList(object):

    def __init__(self, count, head):
        """
        :param count: 顺序表中元素的个数. 这里对 顺序表的 容量和元素个数 做了简单处理, 统一成 元素个数
        :param head: 顺序表中表头里面 指向 数据体起始位置的内存地址
        """
        self.count = count
        self.head = head
        self.temp = None  # 建立一个临时变量

    def reverse(self):
        """顺序表反转"""
        i = 0
        while i <= self.count // 2:
            self.temp = self.head + i * 4  # 32位的操作系统中,int占4个字节
            self.head = self.head + (self.count - i - 1) * 4
            self.head + (self.count - i - 1) * 4 = 100
            i += 1

