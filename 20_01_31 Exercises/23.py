# -*- coding:utf-8 -*-

# 题目（辗转相除法）
"""
辗转相除法， 又名欧几里德算法，是求最大公约数的一种方法。
输入两个正整数 M 和 N（N<=M），用辗转相除法求出 M 和 N 的最大公约数
"""

# 输入格式
"""
输入共一行，包含两个整数，数与数之间以一个空格分开
"""

# 输出格式
"""
输出若干行，依次输出使用辗转相除法生成的带余数除法算式（商和余数之间用符号"..."隔开），
最后一行输出 M 和 N 的最大公约数
"""

# 输入样例
"""
4 2
"""

# 输出样例
"""
4/2=2...0
2
"""


def Euclidean(a, b):
    """ 欧几里得算法（辗转相除法） """
    if a < b:
        # a 存大数
        a, b = b, a

    t = a % b
    print("%d/%d=%d...%d" % (a, b, a // b, a % b))

    while t != 0:
        a = b
        b = t
        t = a % b
        print("%d/%d=%d...%d"%(a, b, a//b, a%b))
    return b

if __name__ == "__main__":
    try:
        a, b = input("请输入两个整数：").split()
        a = int(a)
        b = int(b)
        value = Euclidean(a, b)
        print(value)
    except Exception:
        print("请按指定格式输入！")
