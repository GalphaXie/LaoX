# !/usr/bin/python3
#  file: coroutine_4_yield_多任务.py
#  Created by Guang at 19-7-21
#  description:
#
#  *-* coding:utf8 *-*
import gevent
import time


def func1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        gevent.sleep(1)


def func2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        gevent.sleep(1)


def func3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        gevent.sleep(1)


g1 = gevent.spawn(func1, 5)
g2 = gevent.spawn(func2, 5)
g3 = gevent.spawn(func3, 5)

g1.join()
g2.join()
g3.join()


"""运行结果如下：
<Greenlet at 0x7fd539f8d548: func1(5)> 0
<Greenlet at 0x7fd539f8d548: func1(5)> 1
<Greenlet at 0x7fd539f8d548: func1(5)> 2
<Greenlet at 0x7fd539f8d548: func1(5)> 3
<Greenlet at 0x7fd539f8d548: func1(5)> 4
<Greenlet at 0x7fd539f8d748: func2(5)> 0
<Greenlet at 0x7fd539f8d748: func2(5)> 1
<Greenlet at 0x7fd539f8d748: func2(5)> 2
<Greenlet at 0x7fd539f8d748: func2(5)> 3
<Greenlet at 0x7fd539f8d748: func2(5)> 4
<Greenlet at 0x7fd539f8d848: func3(5)> 0
<Greenlet at 0x7fd539f8d848: func3(5)> 1
<Greenlet at 0x7fd539f8d848: func3(5)> 2
<Greenlet at 0x7fd539f8d848: func3(5)> 3
<Greenlet at 0x7fd539f8d848: func3(5)> 4

从结果中产生的合理推断：
1. gevent.getcurrent() 结果是对象， 且是 greenlet 的封装
2. 并没有真正的按照多任务执行： 3个greenlet是依次运行而不是交替运行
3. 如果把 三行 join 注释掉， 则控制台没有任何打印。
    - 主进程如果结束， 主线程结束； 主线程结束， 进程必挂。
    - join() 阻塞作用， 等待各个函数执行结束。
4. 尝试：用time模块中的sleep来模拟一个耗时操作, 发现并没有改观。
5. 尝试：用gevent模块中的sleep来模拟一个耗时操作, 终于看到交替执行。
    - 结论： 必须将程序中的耗时操作都切换成 gevent中 对应的方法， 才能实现多任务
6. 继续推断: 针对不同的耗时操作(文件读取和网络)，如果都需要手动去 修改成 gevent 对应的方法显然不现实， 所有有了 ‘打补丁’
    - monkey.patch_all()
    - 同时采用更加简单的方式 完成 “注册”： gevent.joinall([ ])

"""