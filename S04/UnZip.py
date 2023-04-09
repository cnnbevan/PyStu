# !/usr/bin/env python
# coding=utf-8
# import shutil
import zipfile
# shutil.unpack_archive('D:\\EvanPro\\PyStu\\S04\\1\\1.zip','D:\\EvanPro\\PyStu\\S04\\1\\2')
f = zipfile.ZipFile("D:\\EvanPro\\PyStu\\S04\\1\\1.zip", 'r')
for file in f.namelist():
    f.extract(file, "D:\\EvanPro\\PyStu\\S04\\1\\2")
f.close()
