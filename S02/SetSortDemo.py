# !/usr/bin/env python
# coding=utf-8
# 定义降序规则
from functools import cmp_to_key


def desc(x, y):
    if x < y:
        return 1    # 如果x小于y，则x排在y之前
    elif x > y:
        return -1   # 如果大于y，则x排在y之后
    else:
        return 0    # 否则并列


# 定义待排序的numbers列表
numbers = [5, 58, 47, 75, 100]
numbers.sort(key=cmp_to_key(desc))  # 在排序时用到desc方法
print(numbers)      # 输出[100, 75, 58, 47, 5]
numbers.sort()
print(numbers)      # 输出[5, 47, 58, 75, 100]
