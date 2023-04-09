# !/usr/bin/env python
# coding=utf-8


# 定义冒泡排序的函数
def SortFunc(numArray):
    loopTimes = 0
    # 记录这个循环冒泡排序的次数
    while loopTimes < len(numArray) - 1:
        # index为待比较元素的下标
        for index in range(len(numArray) - loopTimes - 1):
            if numArray[index] > numArray[index + 1]:
                tmp = numArray[index]
                numArray[index] = numArray[index + 1]
                numArray[index + 1] = tmp
        loopTimes = loopTimes + 1
    return numArray


unSortedNums = [10, 12, 48, 7, 5, 3]
print(SortFunc(unSortedNums))
