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


class DoubleLinkList(object):
    """双向链表(双链表)"""
    def __init__(self, head_node=None):
        """对于链表而言,只需要保存其一个节点即可,这里还是保存头节点"""
        self.__head = head_node

    def is_empty(self):
        """判断链表是否是空链表"""
        return self.__head is None

    def length(self):
        """判断链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1

        return count

    def travel(self):
        """双向链表的遍历操作"""
        cur = self.__head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def add(self, obj):
        """链表头插法"""
        # 构建 新节点
        node = Node(obj)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self, obj):
        """双向链表 尾插法"""
        node = Node(obj)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, index, obj):
        """双向链表的插入操作"""
        assert isinstance(index, int)
        if index <= 0:
            self.add(obj)
        elif index >= self.length():
            self.append(obj)
        else:
            node = Node(obj)
            cur = self.__head
            for i in range(index):
                cur = cur.next
            cur.pre.next = node
            node.pre = cur.pre
            cur.pre = node
            node.next = cur

    def remove(self, obj):
        """移除双向链表中的元素"""
        if self.is_empty():
            return

        cur = self.__head

        while cur is not None:
            if cur.data == obj:
                # 找到了要删除的节点
                if self.length() == 1:
                    # 只有一个节点
                    self.__head = None
                if cur.pre is not None and cur.next is not None:
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre  # 可能不存在 pre 尾节点
                    # 要将这个节点回收
                    del cur
                elif cur.pre is not None:
                    # 表示要删除的是尾节点
                    cur.pre.next = None
                    del cur
                elif cur.pre is None:
                    self.__head = cur.next
                    cur.next.pre = None
                    del cur
                # 如果找到了, 退出循环
                break

            cur = cur.next

    def search(self, obj):
        """查找某个节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.data == obj:
                return True
            cur = cur.next

        # 默认不存在
        return False

    def reverse(self):
        """双链表反转"""
        cur = self.__head
        while cur is not None:
            # 如果只有一个元素
            if self.length() == 1:
                break
            else:
                if cur.pre is None:
                    cur.next.pre = cur
                    cur.next = None

            cur = cur.next













