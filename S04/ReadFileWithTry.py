# !/usr/bin/env python
# coding=utf-8
try:
    # filename = 'D:\\EvanPro\\PyStu\\S04\\1\\python1.txt'
    filename = 'D:\\EvanPro\\PyStu\\S04\\1\\python.txt'
    f = open(filename, 'r')
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
except Exception:
    print("Error when handling the file:" + filename)
finally:
    try:
        f.close()
    except Exception:
        print("No Need to close file:" + filename)
