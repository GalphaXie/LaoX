#!/usr/bin/python3
# file: 01-双链表实现.py
# Created by Guang at 19-10-8
# description: 双向链表的实现

# *-* coding:utf8 *-*


class Node(object):
    """抽象出节点类"""
    def __init__(self, obj):
        self.pre = None  # 指向上一个节点,初始为None
        self.data = obj  # 指向
        self.next = None

