# !/usr/bin/env python
# coding=utf-8

print("Hello 'World'")  # 双引号单引号夹杂使用
print('Hello "World"')  # 单引号里套双引号
print("Hello: \name is Peter.")  # \n是换行符
print(r"Hello \name is Peter.")  # 加了前缀r，则会原样输出
str = "123456789"
print(str.index("234"))  # 查找234这个字符串的位置，返回1
# print(str.index("256"))  	# 没找到则会抛出异常
print(str.find("456"))  # 查找456所在的位置，返回3
print(str.find("256"))  # 没找到，返回-1
print(len(str))  # 返回长度，结果是9
print(str.replace("234", "334"))  # 把234替换成334
# 但是str没有实际改变
print(str.replace("334", "343"))
str1 = str.replace("234", "343")
print(str1)
