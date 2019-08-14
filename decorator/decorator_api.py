#!/usr/bin/python3
# file: decorator_api.py
# Created by Guang at 19-8-14
# description:

# *-* coding:utf8 *-*

"""
一. python完成业务功能的实现方式：
1.面向过程；
2.函数和匿名函数
3.闭包和装饰器
4.面向对象(类和实例对象)

二. 闭包： 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包

三. 实现业务功能需要：功能 + 数据

四. 函数、匿名函数、闭包、对象 当做实参时 有什么区别？
1. 匿名函数能够完成基本的简单功能,传递是这个函数的引用 只有功能
2. 普通函数能够完成较为复杂的功能,传递是这个函数的引用 只有功能
3. 闭包能够将较为复杂的功能,传递是这个闭包中的内部函数以及数据，因此传递是功能+数据
4. 对象能够完成最为复杂的功能,传递是很多数据+很多功能，因此传递是功能+数据

五. 闭包 nonlocal
- python3 给闭包提供了一个 nonlocal 关键字， 可以供 闭包函数 修改 外部函数的局部变量
- 如果不修改则不需要 nonlocal 关键字
- python2 没有该关键字， 则可以借助 [] 这样的数据结构来自己实现 修改

六. 装饰器原理
@decorator
def index():
    pass
等价于：  index = decorator(index)
描述：
- 调用装饰器同名的函数或方法，
- 并将被装饰函数index 作为参数传递到装饰器中,
- 最后再将 装饰器同名函数或方法的执行结果 赋值给 被装饰函数同名的变量index

七. "开闭原则"
- 实现的功能代码不允许被修改，但可以被扩展
    - 封闭：已实现的功能代码块
    - 开放：对扩展开发

八. 装饰器的功能：
- 引入日志
- 函数执行时间统计
- 执行函数前预备处理
- 执行函数后清理功能
- 权限校验等场景
- 缓存

九. 装饰器的几种情况 | 万能装饰器
- 无参数无返回值
- 有(1个|多个)参数无返回值 : 给内部函数增加形参
- 无参数有(1个|多个)返回值 : 在内部函数中执行 被装饰函数的时候， return 执行结果； 其实可以默认都return, 通用无返回值请情
- 有(1个|多个)参数有(1个|多个)返回值 : 给内部函数增加形参, return 装饰函数()
- 1个装饰器装饰多个函数
- 多个装饰器装饰1个函数 : 装饰顺序 从内向外(更靠近被装饰函数的装饰器更先装饰)

十. 装饰器装饰的函数在没有被调用前就已经完成装饰， 见下面的案例.

十一. 类做装饰器, __call__方法


"""

import time


# 1.闭包案例
def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))

# -----------------------------
print("-" * 50)


# 2.nonlocal 关键字的演示
x = 300


def test1():
    x = 200

    def test2():
        nonlocal x
        print("----1----x=%d" % x)
        x = 100
        print("----2----x=%d" % x)

    return test2


t1 = test1()
t1()


# -----------------------------
print("-" * 50)


# 3.装饰器(运行时间统计) 案例演示
def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("alltimeis %f" % (stop_time - start_time))

    return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1():
    print("-----test1----")
    for i in range(1000000):
        pass


# test1 = set_func(test1)
test1()


# -----------------------------
print("-" * 50)


# 4.案例：装饰器在调用函数之前，已经被python解释器执行了，所以要牢记 当调用函数之前 其实已经装饰好了，尽管调用就可以了
def set_func(func):
    print("---开始进行装饰")

    def call_func(a):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func(a)

    return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num):
    print("-----test1----%d" % num)


@set_func  # 相当于 test2 = set_func(test2)
def test2(num):
    print("-----test2----%d" % num)

# test1(100)
# test2(200)


# -----------------------------
print("-" * 50)


# 5.案例： 既有参数又有返回值的 装饰器
def set_func(func):
    print("---开始进行装饰")

    def call_func(*args, **kwargs):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        # func(args, kwargs)  # 不行，相当于传递了2个参数 ：1个元组，1个字典
        return func(*args, **kwargs)  # 拆包

    return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----test1----%d" % num)
    print("-----test1----", args)
    print("-----test1----", kwargs)
    return "ok"


@set_func
def test2():
    pass


ret = test1(100)
print(ret)

ret = test2()
print(ret)


# -----------------------------
print("-" * 50)


# 6.案例： 类装饰器
class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("这里是装饰器添加的功能.....")
        return self.func()


@Test  # 相当于get_str = Test(get_str)
def get_str():
    return "haha"


print(get_str())


# -----------------------------
print("-" * 50)


# 7.案例: 带参数的装饰器
def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("----权限级别1，验证----")
            elif level_num == 2:
                print("----权限级别2，验证----")
            return func()

        return call_func

    return set_func


# 带有参数的装饰器装饰过程分为2步:
# 1. 调用set_level函数，把1当做实参
# 2. set_level返回一个装饰器的引用，即set_func
# 3. 用返回的set_func对test1函数进行装饰（装饰过程与之前一样）
@set_level(1)
def test1():
    print("-----test1---")
    return "ok"


@set_level(2)
def test2():
    print("-----test2---")
    return "ok"


test1()
test2()


# -----------------------------
print("-" * 50)


# 8.案例: 万能装饰器

def wrapper(func):
    def call_func(*args, **kwargs):

        return func(*args, **kwargs)

    return call_func


def decorator(*args, **kwargs):
    def wrapper(func):
        def call_func(*args, **kwargs):

            return func(*args, **kwargs)

        return call_func

    return wrapper
