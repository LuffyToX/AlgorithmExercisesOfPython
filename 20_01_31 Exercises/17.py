# -*- coding:utf-8 -*-

# 题目（整除）
"""
给定四个正整数 m 和 a、b、c，分别判断 m 被 a、b、c 整除的情况
"""

# 输入格式
"""
输入共两行，第一行是正整数 m，第二行是三个正整数 a、b、c，数与数之间以一个空格分开
"""

# 输出格式
"""
输出共一行，把 a、b、c 当中能够整除 m 的数字输出，小的数字在前，大的数字在后，数与数之间以一个空格分开。
如果 a、b、c 都不能整除 m，请输出小写字母 n
"""

# 输入样例
"""
24
6 8 12
"""

# 输出样例
"""
6 8 12
"""


class Divide:
    def __init__(self, m):
        self.m = int(m)

    def reminder(self, num):
        if self.m%num == 0:
            return num
        else:
            return False

if __name__ == "__main__":
    m = input("请输入整数 m ：")
    a, b, c = input("请输入三个整数：").split()
    divide = Divide(m)

    lst = []
    x = divide.reminder(int(a))
    if x != False:
        lst.append(x)
    y = divide.reminder(int(b))
    if y != False:
        lst.append(y)
    z = divide.reminder(int(c))
    if z != False:
        lst.append(z)
    lst.sort()
    if lst == []:
        print('n')
    else:
        for i in lst:
            print(i, end=' ')


