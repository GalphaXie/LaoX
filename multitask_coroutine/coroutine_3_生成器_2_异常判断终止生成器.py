#!/usr/bin/python3
# file: coroutine_3_生成器_1_fibonacci.py
# Created by Guang at 19-7-21
# description:

# *-* coding:utf8 *-*


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a  # 如果一个函数中有yield语句，那么这个就不在是函数，而是一个生成器的模板
        a, b = b, a+b
        current_num += 1
    return "ok..."

# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj = create_num(10)

while True:
    try:
        ret = next(obj)
        print(ret)
    except StopIteration:
        print(StopIteration.value)  # StopIteration 对象有一个属性 value, 可以获取 yield构成的生成器的模板 的return返回值
        break

