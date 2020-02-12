# -*- coding:utf-8 -*-

# 题目（循环小数升级版）
"""
循环小数可以表示成分数，现在有整数部分为 0 的循环小数 a（a>0.1），
a 的循环节从某一位开始有若干位，将 a 表示成最简分数 n/m 的形式
"""

# 算法
"""
x = 0.177777...             x = 0.1727272...
100x = 17.7777...          1000x = 172.7272...
10x = 1.7777...            10x = 1.727272...
90x = 16（减去小数部分）    990x = 171
x = 16/90                   x = 171/990
"""

# 输入格式
"""
输入共一行，包含两个数，一个循环小数和一个整数，循环小数只显示到它的第一个循环节，
整数表示从小数点后第几位开始循环节，数与数之间以一个空格分开。
比如输入样例里表示的循环小数是 0.17777777...
"""

# 输出格式
"""
循环小数对应的最简分数 n/m
"""

# 输入样例
"""
0.17 2
"""

# 输出样例
"""
8/45
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

def Decimal_to_Fraction(decimal, number):
    """ 无线循环小数也是有理数，有理数都可以表示成两个整数相除的形式 """
    # 循环位数
    circle_num = len(decimal) - number + 1
    num_1 = pow(10, circle_num+number-1)
    num_2 = pow(10, number-1)
    frac_son = int(decimal)-int(decimal[:number-1])
    frac_fat = (num_1-num_2)
    a = Euclidean(frac_son, frac_fat)
    x = "{0:d}/{1:d}".format(frac_son//a, frac_fat//a)
    return x

if __name__ == "__main__":
    rational, number= input("请输入一个循环小数以及循环节位置：").split()
    integer, decimal = rational.split(".")
    number = int(number)

    print(Decimal_to_Fraction(decimal, number))

