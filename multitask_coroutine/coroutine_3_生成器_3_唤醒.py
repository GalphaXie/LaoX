#!/usr/bin/python3
# file: coroutine_3_生成器_1_fibonacci.py
# Created by Guang at 19-7-21
# description:

# *-* coding:utf8 *-*


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>ret>>>>", ret)
        a, b = b, a+b
        current_num += 1


obj = create_num(10)

# obj.send(None)  # send一般不会放到第一次启动生成器，如果非要这样做 那么传递None

ret = next(obj)  # 唤醒 yield a (等号右边的部分), 然后生成器对象 “暂停”， 并将 a 返回给 24行的ret
print(ret)  # ret = 1

# send里面的数据会 传递给第13行，当做yield a的结果，然后第13行的 ret保存这个结果,,,
# send的结果是下一次调用yield时 yield后面的值
ret = obj.send("hahahha")  # 开始执行 等号左边(即yield a)左边的代码, 将send()内部的参数作为值传递给等号左边的变量ret; 同时 生成器继续向下执行
print(ret)  # ret = 第二次取出来的a，即1

"""
上述代码执行结果：

0
>>>ret>>>> hahahha
1

"""

"""
笔记：
1. next() 等价于 send(None)
- 第一次不能调用 含非None参数的 send() 函数， 否则会报错; 一般第一次都调用 next() 函数
2. 从执行结果推断出结论：
- 1. ret = next(obj)  # 唤醒 yield a (等号右边的部分), 然后生成器对象 “暂停”， 并将 a 返回给 接收next()函数返回值的变量ret
- 2. send里面的数据会传递给yield a 所在行的等号左边的结果，然后 yield a 左边的变量 保存这个结果
- 3. send的结果是下一次调用yield时 yield后面的值
3. 唤醒操作除了 send next 还可以用原生的 __next__() 
"""