# !/usr/bin/env python
# coding=utf-8

priceList = [10.58, 25.47, 100.58, 500.47]
cityList = ["ShangHai", "HangZhou", "NanJing", "NB", "NB"]

# 进行排序
priceList.sort()
print(priceList)
# print(priceList.sort()); # 错误的用法
cityList[0] = 'NingBo'
print(cityList)

print(sum(priceList))   # 求和
print(max(priceList))   # 求最大值，输出500.47
print(min(cityList))    # 求最小值，输出HangZhou
print(cityList.count("NB"))
print(len(cityList))
subList = priceList[1:len(priceList)+1]  # 截取数组中元素
print(subList)  # 输出[25.47, 100.58]
