#!/usr/bin/python3
# file: single_inheritor.py
# Created by Guang at 19-8-5
# description:

# *-* coding:utf8 *-*


class Parent(object):
    """父类"""
    def __init__(self, name):
        print("parent的init方法开始调用")
        self.name = name
        print("parent的init方法结束调用")


class Son(Parent):
    """子类"""
    def __init__(self, name, age):
        print("Son的init方法开始调用")
        self.age = age
        super().__init__(name)  # 单继承不能提供全部参数
        print("Son的init方法结束调用")


class GrandSon(Son):
    """子类"""
    def __init__(self, name, age, gender):
        print("GrandSon的init方法开始调用")
        self.gender = gender
        super().__init__(name, age)  # 单继承不能提供全部参数
        print("GrandSon的init方法结束调用")


if __name__ == '__main__':
    print(GrandSon.__mro__)
    gs = GrandSon('张三', 11, 'woman')
    print('姓名：', gs.name)
    print('年龄：', gs.age)
    print('性别：', gs.gender)


"""
笔记：
1.单继承和多继承在使用 super() 的区别：
- 1.1 单继承： 传递的参数只传需要的， 因为调用顺序是可以确定的， 需要的参数也是确定的；
- 1.1 多继承：　传递的参数必须是所有的，　应为调用的顺序没法直接判断，需python解释器自动调用c3来确定， 所以我们需要把所有的传递。
"""