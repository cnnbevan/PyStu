# !/usr/bin/env python
# coding=utf-8
try:
    filename = 'D:\\EvanPro\\PyStu\\S04\\1\\myFile.txt'
    f = open(filename, 'a')
    f.write('Hello,')
    f.write('Python!')
except Exception:
    print("Error when writing the file:" + filename)
finally:
    try:
        f.close()
    except Exception:
        print("No Need to close file:" + filename)
