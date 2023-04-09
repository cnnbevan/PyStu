# !/usr/bin/env python
# coding=utf-8

# 判断闰年
# year = 2018
year = 2020
# year = 1900
if (year % 4 == 0) and (year % 100 != 0):
    print("%d是闰年" % year)
elif year % 400 == 0:
    print("%d是闰年" % year)
else:
    print("%d不是闰年" % year)
