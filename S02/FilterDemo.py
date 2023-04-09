# !/usr/bin/env python
# coding=utf-8
# 判断输入参数是否是小写字母的函数
def isLowCase(str):
    return str.lower() == str


strlist = list(filter(isLowCase, ["Hello", "world"]))
print(strlist)  # ['world']
# 判断输入参数是否为空的函数

print(list(filter(isLowCase, ['evan'])))


def filterNull(empNo):
    return empNo.strip() != ''


dataFromFile = ['101', '102', '103', '']
empList = list(filter(filterNull, dataFromFile))
print(empList)  # ['101', '102', '103']
