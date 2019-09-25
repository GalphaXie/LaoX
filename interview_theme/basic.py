#!/usr/bin/python3
# file: basic.py
# Created by Guang at 19-9-17
# description:

# *-* coding:utf8 *-*

# sorted 用法考察, 对字典按照 value 进行排序, 得到序列;
dic = {"a": 24, "g": 52, "i": 12, "k": 33}

new_dic = sorted(dic.items(), key=lambda x: x[1])

print(new_dic)

# 字典推导式:
d = {k: v for k, v in [(1, 2), (2, 4), [5, 3], ["b", "name"]]}

print(d)

# 列表切片
li = [0, 1, 2, 3, 4]
print(li[10:])  # 切片超过范围不报错,得到空[],   但是索引超过范围会报错

li_1 = [1, 2, 3]
li_2 = [3, 4, 5]

print(set(li_1) | set(li_2))  # {1, 2, 3, 4, 5}
print(set(li_1) ^ set(li_2))  # {1, 2, 4, 5}
print(set(li_1) & set(li_2))  # {3}

print(set(li_1) - set(li_2))


# 列表引用: 这种就是套路题, 纯粹应试而已, 考察的时候要仔细
def extend_list(value, li=[]):
    li.append(value)
    return li


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list("a")

print("list1= %s" % list1)
print("list2= %s" % list2)
print("list3= %s" % list3)

# 字典的fromkeys 方法

v = dict.fromkeys(["k1", "k2"], [])

v["k1"].append(666)
print(v)

v["k1"] = 777

print(v)  # {'k1': 777, 'k2': [666]}

# 一行代码实现99乘法表
x = 1
print('\n'.join(['\t'.join(["%2s *%2s = %2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))
