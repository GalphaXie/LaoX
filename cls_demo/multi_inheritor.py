#!/usr/bin/python3
# file: multi_inheritor.py
# Created by Guang at 19-8-5
# description:

# *-* coding:utf8 *-*


class Parent(object):
    """"""
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错, 使用不定长参数， 接收参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错, 使用不定长参数， 接收参数
        print('Son1的init开始被调用')
        self.age = age
        # Parent.__init__(self, name)
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错, 使用不定长参数， 接收参数
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错, 使用不定长参数， 接收参数
        print('Son2的init开始被调用')
        self.gender = gender
        # Parent.__init__(self, name)
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错, 使用不定长参数， 接收参数
        print('Son2的init结束被调用')


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson的init开始被调用")
        # 多继承时， 相对于使用 类名.__init__方法， 要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法, 这也是为何多继承要全部传参的原因
        # Son1.__init__(self, name, age)  # 单独调用父类的初始化方法
        # Son2.__init__(self, name, gender)
        super().__init__(name, age, gender)
        # super(GrandSon, self).__init__(name, age, gender)
        print("Grandson的init结束被调用")


if __name__ == '__main__':
    print(GrandSon.__mro__)
    gs = GrandSon('小王', 11, 'man')
    print("姓名:", gs.name)
    print("年龄:", gs.age)
    print("性别:", gs.gender)


"""
笔记：
1.执行次数：
- 如果2个子类中都继承了父类，当在子类中通过父类名调用时，parent被执行了2次
- 如果2个子类中都继承了父类，当在子类中通过super调用时，parent被执行了1次
2.super 使用
- super().方法名
- super(类名, self).方法名
3.总结：
- super().__init__相对于类名.__init__，在单继承上用法基本无差
- 但在多继承上有区别，super方法能保证每个父类的方法只会执行一次，而使用类名的方法会导致方法被执行多次，具体看前面的输出结果
- 多继承时，使用super方法，对父类的传参数，应该是由于python中super的算法导致的原因，必须把参数全部传递，否则会报错
- 单继承时，使用super方法，则不能全部传递，只能传父类方法所需的参数，否则会报错
- 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍, 而使用super方法，只需写一句话便执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因

"""