#!/usr/bin/python3
# file: 01-单链表实现.py
# Created by Guang at 19-10-7
# description: 抽象出单链表类, 节点类, 和 单链表ADT的具有功能

# *-* coding:utf8 *-*


# class Node(object):
#
#     def __init__(self, item=None, next=None):
#         self.item = item
#         self.next = next
#
#
# class SingleLinkList(object):
#
#     def __init__(self, node=None):
#         self.node = node
#
#     def travel(self):
#         while self.node.next is not None:
#             print(self.node.item)
#
#
# tail = Node(item=300, next=None)
# node2 = Node(item=200, next=tail.item)
# node1 = Node(item=100, next=node2.item)
# head = Node(next=node1.item)
#
# single_link_list = SingleLinkList(node=head)
# single_link_list.travel()


class Node(object):

    def __init__(self, data=None):
        """
        初始化操作,构造一个节点
        :param data: 当前节点要保存的数据
        """
        self.data = data  # 节点数据区,要保存的数据
        self.next = None  # 节点地址区,指向的下一个区域的地址信息; 默认可以设置为None,表示起始没有头信息


class SingleLinkList(object):
    """单向链表(单链表)"""

    def __init__(self, head_node=None):
        """对于单链表来说,只需要保存 头节点 的信息即可"""
        self.__head = head_node

    # 下面实现,单链表中封装的 操作数据的方法
    def is_empty(self):
        """链表是否为空"""
        # if self.__head is None:
        #     return True
        return self.__head is None

    def length(self):
        """链表的长度"""
        # 借助两个 辅助变量
        cur = self.__head  # 初始化游标指向头节点
        count = 0  # 初始长度设置为0
        while cur is not None:
            count += 1
            cur = cur.next  # 移动游标到下一个节点
        return count

    def travel(self):
        """链表遍历操作"""
        cur = self.__head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def add(self, obj):
        """链表添加元素 头插法"""
        # # 1.空链表
        # if self.__head is None:
        #     self.__head = item
        # # 非空链表操作
        # item.next = self.__head
        # self.__head = item

        # 迭代
        # 创建 node 节点
        node = Node(obj)
        # 合并 空链表 和 非空链表 两种情况
        # self.__head = node
        # node.next = self.__head
        # 利用python特性进行 交换
        self.__head, node.next = node, self.__head  # 这里可以进一步合并,不过可能难以理解

    def append(self, obj):
        """链表追加元素 尾插法"""
        node = Node(obj)
        # 1.空链表
        if self.is_empty():
            self.__head = node
        else:
            # 2.非空链表操作
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, obj):
        """链表插入元素"""
        # TODO 有优化空间
        assert isinstance(index, int)
        if index <= 0:
            self.add(obj)
        elif index >= self.length():
            self.append(obj)
        else:
            node = Node(obj)
            # 借助游标对象
            cur = self.__head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, obj):
        """链表移除元素"""
        cur = self.__head
        # 多引入一个辅助变量
        pre = None
        while cur is not None:
            if cur.data == obj:
                if cur == self.__head:
                    # 表示删除头结点
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                    # 提示还要释放内存;
                break
            else:
                pre = cur
                cur = cur.next
        else:
            raise ValueError("the %s does not exist in the single link list" % obj)

    def search(self, obj):
        """查询当前元素是否存在于 单链表中"""
        cur = self.__head
        while cur is not None:
            if cur.data == obj:
                return True
            else:
                cur = cur.next
        else:
            return False

    def reverse(self):
        """单向链表的反转"""
        cur = self.__head
        _ = None
        while cur is not None:
            pre = cur
            cur = cur.next
            if pre == self.__head:
                pre.next = None
            else:
                pre.next = _
            _ = pre
        else:
            self.__head = _
            # self.travel()
        return self


# # 创建单个节点对象
# node1 = Node(100)
# node2 = Node(200)
# # 指明节点对象之间的关系
# node1.next = node2
#
# sll = SingleLinkList(head_node=node1)
# sll.length()
# print("-" * 50)
#
# sll.travel()
# print("-" * 50)
# # 链表头部插入元素
# # 分析两种可能性: 空链表插入头结点; 非空链表插入头结点
# node3 = Node(20000)
# sll.add(node3)
# sll.travel()
# print("-" * 50)
#
# # 链表追加元素
# # 分析两种可能性: 空链表插入头结点; 非空链表插入头结点
# node4 = Node(1000)
# sll.append(node4)
# sll.travel()
# print("-" * 50)
#
# # 链表插入元素
# node5 = Node("zhangsan")
# sll.insert(2, node5)
# # sll.insert(-5, node5)
# # sll.insert(10, node5)
# sll.travel()

# 提高封装性, 不给要让用户去操作 node 对象, 增加理解操作难度
if __name__ == '__main__':
    sll = SingleLinkList()

    print(sll.is_empty())
    print(sll.length())

    sll.add(100)
    print(sll.is_empty())
    print(sll.length())
    sll.travel()

    sll.add(200)
    print(sll.is_empty())
    print(sll.length())
    sll.travel()

    sll.append("zhangsan")
    print(sll.length())
    sll.travel()

    sll.append("lisi")
    print(sll.length())
    sll.travel()

    sll.insert(-5, "he")
    sll.travel()

    sll.insert(1, "her")
    sll.travel()

    sll.insert(10, "she")
    sll.travel()

    sll.remove("zhangsan")
    sll.travel()
    sll.remove("he")
    sll.remove("she")
    sll.remove("her")
    sll.travel()

    # sll.remove(10000)

    print(sll.search("lisi"))  # True
    print(sll.search(10000))  # False

    # 单向链表反转
    temp = sll.reverse()
    temp.travel()
