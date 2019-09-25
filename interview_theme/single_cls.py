#!/usr/bin/python3
# file: single_cls.py
# Created by Guang at 19-9-18
# description:

# *-* coding:utf8 *-*


"""
# python下, 单例的几种实现方式:

- 1. 类属性来记录 实例对象, 然后在 __new__ 方法返回;
- 2. python 的模块天生就是 单例模式, 考虑在一个模块中实现一个类, 然后在该模块中进行该类的实例化, 当导入实例的时候自然就是 单例.
    模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了
- 3. 装饰器
- 4. 自定义类方法, 但是该方法中实现 创建类; 该方法当 __init__ 中出现 IO 操作 在多线程的时候, 容易出现 非单例的情况, 解决思路是 加锁;  但是该方法不推荐
- 5. classmeta 方式



"""


class SingleInstance1(object):
    """
    方式一: 通过 instance 类属性来标记
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        print("这是一个单例")

        if not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        print(self.instance)


# player1 = SingleInstance1()
# player2 = SingleInstance1()
# player3 = SingleInstance1()
# player4 = SingleInstance1()

# 方式二: 装饰器实现

def Singleton(cls):
    _instance = {}

    def instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return instance


@Singleton
class A(object):

    def __init__(self, x):
        self.x = x


# a1 = A(2)
# a2 = A(3)

# print(id(a1))
# print(id(a2))


# 元类

# class Singleton(type):
#
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class Config(metaclass=Singleton):
#     def __init__(self, SQLALCHEMY_DB_URI):
#         self.SQLALCHEMY_DB_URI = SQLALCHEMY_DB_URI

"""
补充知识:
如果元类中定义了__call__，此方法必须返回一个对象，否则类的实例化就不会起作用。（实例化得到的结果为__call__的返回值）

我的理解:
1.元类中会先调用 __new__ 方法, 该方法会生成 类似的实例对象就是: type.__new__ 的结果, 就是当前元类名字的类对象, 就是当前的元类;
2.然后 __new__ 的返回值会 作为 元类中 __call__方法的第一参数cls,  然后可以在这里拦截; 先使用 object基类.__new__ 来生成一个实例对象, 然后在调用__init__ 方法
3.只要保证 __call__ 返回的是同一个 实例对象， 则 A（） 实例化的时候不再调用 A.__new__ 

还是没怎么理解？


大神的笔记：
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法

我的补充：
1. 当某个类是由元类创建的时候， 那么得先有元类， 元类也会调用 __new__ & __init__ 方法； 这一点和 普通的类并无二致
2. 当遇到语法 `类名（）`的时候， 会去调用 他父类的 __call__ 方法， 这里就是调用元类的 __call__ 方法； 
3. 我们要做拦截就是在 元类的 __call__（cls,...）中拦截， 因为 该方法的第一个参数cls指代的就是 被元类创建的类， 那么我们可以在
元类__call__中调用 被元类的子类的 __new__ 方法， 当该方法得到的结果 是唯一的时候， 那么也就可以得到单例了。
4.call 本来在普通类的时候是一个实例方法， 但是在元类中该方法有些特殊， 其第一个参数也是实例，不过这个实例是个类。所以一般习惯用cls代替self
5. 难点：super(SingletonType, cls).__call__(*args, **kwargs) 不等价于  type.__call__(*args, **kwargs), 而等价于 type.__call__(cls, *args, **kwargs)

"""

# 演示 元类
# class SingletonType(type):
#     def __init__(self, *args, **kwargs):
#         super(SingletonType, self).__init__(*args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):  # 这里的cls，即Foo类
#         print('cls', cls)
#         # 手动调用 Foo 的 new 方法
#         obj = cls.__new__(cls, *args, **kwargs)
#         # 得到一个实例，传入 init 中
#         # cls.__init__(obj, *args, **kwargs)  # Foo.__init__(obj)
#         return obj
#
#
# class Foo(metaclass=SingletonType):  # 指定创建Foo的type为SingletonType
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#
#
# obj = Foo('xx')


# 元类实现

import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    print(SingletonType.__mro__)  # (<class '__main__.SingletonType'>, <class 'type'>, <class 'object'>)
                    # 这里理解起来很有难度, super(SingletonType, cls) 表示的是 SingletonType 的父类， 即type; 调用的是 父类的 __call__ 的方法
                    # cls._instance = type.__call__(cls, *args, **kwargs)
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)  # 调用的是 type() 的,得到的是 其实例,也就是 当前的类对象
                    print(cls._instance)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1, obj2)




