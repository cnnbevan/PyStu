# !/usr/bin/env python
# coding=utf-8

priceList = [10.58, 25.47, 100.58]  # 浮点型列表
cityList = ["ShangHai", "HangZhou", "NanJing"]  # 字符串类型列表
mixList = [1, 3.14, "Company"]  # 混合类型的列表，谨慎使用

# 在控制台输出
print(priceList)  # [10.58, 25.47, 100.58]
print(cityList)  # ['ShangHai', 'HangZhou', 'NanJing']
print(mixList)  # [1, 3.14, 'Company']

del mixList[2]
print(mixList)    # 没有了最后一个元素
# mixList.remove(2) # 去掉没有的元素，也会抛出异常

mixList.remove(1)
print(mixList)    # 也看不到1了

print(priceList[0])      # 获得数组指定位置的元素，这里输出的是10.58
priceList.append(200.74)  # 添加元素
print(priceList)         # 能看到添加后的元素
print(cityList.index("ShangHai"))
# print(cityList.index("DaLian")); # 如果找不到元素，会抛出异常并终止程序
