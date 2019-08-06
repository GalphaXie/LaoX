#!/usr/bin/python3
# file: property_demo.py
# Created by Guang at 19-8-5
# description:

# *-* coding:utf8 *-*

# property属性 : 一种用起来像是使用的实例属性一样的特殊属性，可以对应于某个方法


class Pager(object):
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


if __name__ == '__main__':
    pager = Pager(1)
    # pager.start  # 调用property属性
    print(pager.start)
    print(pager.end)

"""
笔记：
property属性的定义和调用要注意一下几点：
- 定义时，在实例方法的基础上添加 @property 装饰器；并且仅有一个self参数
- 调用时，无需括号
Python的property属性的功能是：property属性内部进行一系列的逻辑计算，最终将计算结果返回
"""