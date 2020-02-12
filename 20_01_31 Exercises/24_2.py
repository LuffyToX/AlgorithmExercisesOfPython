# -*- coding:utf-8 -*-

""" 连续自然数的和（优化算法） """

num = int(input())
for i in range(1,num):
    n = i
    for j in range(i + 1, num + 1):
        n = n + j
        if n == num:
            print(i, j)
            break
        if n > num:
            break
print(num, num)