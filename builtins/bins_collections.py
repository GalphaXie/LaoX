from collections import namedtuple
# 内置集合模块， 提供了很多有用的集合类
from collections import deque
# 提高线性表的插入和删除效率
from collections import defaultdict
# 字典没有所需要的键的时候返回默认值
from collections import OrderedDict

# 用于： 表示一个点， 限制只有两个参数
Point = namedtuple("point", ['latitude', 'longitude'])

p = Point(45.132213, 131.234123)

# 可以像属性一样提取出： 对应值

print(p.latitude)
print(p.longitude)

# ------------------------------

# 用于： 表示一个圆， 限制三个参数
Circle = namedtuple("Circle", ['x', 'y', 'r'])  # 坐标和半径

c = Circle(0, 0, 1)


"""
***********************************************
deque  函数
解决list(线性存储)对元素进行 插入和删除 的效率低下的问题， 引入 双向列表， 适合于 队列和栈
***********************************************
"""

q = deque(['a', 'b', 'c'])
q.append("x")
q.appendleft("y")

print(q)


"""
**********************************************
defaultdict
当字典不存在索要获取的键的时候， 返回默认值， 这个默认值是通过函数方法来传递， 所以这里可以进行一定的扩展来使用。
**********************************************
"""

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'key1'
print(dd['key1'])  # 存在, 返回 ‘key1’
print(dd['key2'])  # 不存在， 返回默认值


"""
**********************************************
OrderedDict
使用dict时，key是无序的。 在对 dict做迭代时， 我们无法确定key的顺序
**********************************************
"""

d = dict([('a', 1), ('b', 2), ('c', 3)])
'''
In[9]: d  # dict的Key是无序的
Out[9]: {'c': 3, 'b': 2, 'a': 1}
'''
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
'''
od  # OrderDict的key是有序的
Out[11]: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
'''

# 注意： OrderDict是按照插入的顺序排列， 不是key本身排序：


