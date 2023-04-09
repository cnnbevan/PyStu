# !/usr/bin/env python
# coding=utf-8
f = open("D:\\EvanPro\\PyStu\\S04\\1\\python.txt", 'r')
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()
