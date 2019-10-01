#!/usr/bin/python3
# file: 01-单链表反转.py
# Created by Guang at 19-9-26
# description:

# *-* coding:utf8 *-*


class SingleLinkedListNode:

    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_


def reverse(head):

    pre, data, next_ = None, head.data, head.next_
    if next_ is None:
        return head





if __name__ == '__main__':
    li = SingleLinkedListNode(0)
    li.next_ = SingleLinkedListNode(1)
    li.next_.next_ = SingleLinkedListNode(2)

