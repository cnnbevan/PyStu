# !/usr/bin/env python
# coding=utf-8


def printPrime(maxNum):
    num = []
    currentNum = 2
    for currentNum in range(2, maxNum + 1):
        devidedNum = 2
        for devidedNum in range(2, currentNum + 1):
            if (currentNum % devidedNum == 0):
                break
        if currentNum == devidedNum:
            num.append(currentNum)
        print(num)


printPrime(101)

for current in range(2, 4):  # range 是没有最后一个数值的
    print(current)
