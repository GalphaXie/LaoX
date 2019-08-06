#!/usr/bin/python3
# file: cls_property.py
# Created by Guang at 19-8-6
# description:

# *-* coding:utf8 *-*


class T:
    def get_bar(self):
        print("getter.....")
        return "hello world"

    def set_bar(self, value):
        """必须两个参数"""
        print("setter.....")
        return 'set value ' + value

    def del_bar(self):
        print("deleter ......")
        return "hello python"

    # BAR 作为类属性来定义， 但是因为要接收实例方法作为变量名， 所以放在下面的位置
    BAR = property(get_bar, set_bar, del_bar, "description...")  # property 是python内置的一个类


obj = T()

obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "help"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
desc = T.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
print(desc)
del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法

"""
property方法中有个四个参数

第一个参数是方法名，调用 对象.属性 时自动触发执行方法
第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息

"""


class Money(object):
    def __init__(self):
        self.__money = 0

    # 使用装饰器对money进行装饰，那么会自动添加一个叫money的属性，当调用获取money的值时，调用装饰的方法
    @property
    def money(self):
        return self.__money

    # 使用装饰器对money进行装饰，当对money设置值时，调用装饰的方法
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")


obj = Money()
print(obj.money)
obj.money = 100
print(obj.money)

"""
在装饰器 setter 的方法中可以进行  验证的操作
"""


