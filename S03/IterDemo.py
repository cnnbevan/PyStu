# !/usr/bin/env python
# coding=utf-8
class createEven:           # 有“可遍历需求”的类
    def __init__(self, min, max):
        self.value = min
        self.min = min
        self.max = max

    def __iter__(self):     # 输出全部
        print("in iter")
        return self

    def __next__(self):     # 生成下一个偶数
        print("in next")
        self.value += 2
        if (self.value >= self.min and self.value <= self.max):
            return self.value
        else:
            return 0


myEvenList = createEven(0, 10)
for i in myEvenList:        # 输出myEventList列表中不大于10的偶数
    if i > 0:
        print(i)
    else:
        break
