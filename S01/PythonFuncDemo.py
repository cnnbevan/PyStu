# !/usr/bin/env python
# coding=utf-8
# 定义没返回的函数
def printMsg(x, y):
    print("x is %d" % x)
    print("y is %d" % y)


# 通过return返回
def add(x, y):
    return x + y


# 调用函数
printMsg(1, 2)
# printMsg("1", 2) 	# 报错，这就是不注意参数类型的后果
print(add(100, 50))
