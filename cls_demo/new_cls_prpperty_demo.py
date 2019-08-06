#!/usr/bin/python3
# file: new_cls_prpperty_demo.py
# Created by Guang at 19-8-6
# description:

# *-* coding:utf8 *-*


class Good(object):
    """新式类有三种property"""

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):  # 这里必须要传递两个参数， 第二个参数是value
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


good = Good()
print(good.price)
good.price = 200
print(good.price)
del good.price
# print(good.price)

"""
注意
- 经典类中的属性只有一种访问方式，其对应被 @property 修饰的方法
- 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法
- 由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除

"""


