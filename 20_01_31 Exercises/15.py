# -*- coding:utf-8 -*-

# 题目（循环小数）
"""
循环小数可以表示成分数，现在有整数部分为 0 的循环小数 a（a>0.1），
a 的循环节从十分位开始有若干位，将 a 表示成最简分数 n/m 的形式
"""

# 算法
"""
x = 0.77777...
10x = 7.7777...（10为循环位数）
9x = 7（减去小数部分）
x = 7/9
"""

# 输入格式
"""
一个循环小数，只显示到它的第一个循环节，比如 0.7 表示循环小数 0.777777...
"""

# 输出格式
"""
循环小数对应的最简分数 n/m
"""

# 输入样例
"""
0.7
"""

# 输出格式
"""
7/9
"""


def Euclidean(a, b):
    """ 欧几里得算法（辗转相除法） """
    if a < b:
        # a 存大数
        a, b = b, a
    while b != 0:
        temp = a % b   # 余数
        a = b
        b = temp
    return a

def Decimal_to_Fraction(decimal):
    """ 无线循环小数也是有理数，有理数都可以表示成两个整数相除的形式 """
    num = pow(10, len(decimal))
    a = Euclidean(int(decimal), (num-1))
    x = "{0:d}/{1:d}".format(int(decimal)//a, (num-1)//a)
    return x

if __name__ == "__main__":
    integer, decimal = input("输入一个循环小数（整数部分为0且只显示它的第一个循环节）:")\
        .split(".")
    if int(integer) != 0:
        raise Exception("整数部分应为0！")
    else:
        print(Decimal_to_Fraction(decimal))

