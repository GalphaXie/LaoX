#!/usr/bin/python3
# file: rm_repeater.py
# Created by Guang at 19-9-19
# description:

# *-* coding:utf8 *-*

# 去重并从小到大排序

s = "ajldjlajfdljfddd"

# ret = "".join(sorted(set(s)))   # sorted(序列) -> list

# print(ret)


a = "not 404 found 张三 99 深圳"
import re

ret = re.findall(r"([^[0-9a-zA-Z ]+)", a)
if ret:
    result = " ".join(ret)
    print(result)


# 利用 collections 库 的 Counter 方法统计字符串每个单词出现的次数, "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

s3 = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

from collections import Counter


r = Counter(s3)
print(r.get("l"))




