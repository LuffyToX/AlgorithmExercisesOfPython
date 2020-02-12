# -*- coding:utf-8 -*-

# 题目（质因数分解）
"""
已知正整数 N 是若干（>1）个质数的乘积，输出 N 的质因数分解形式
"""

# 输入格式
"""
输入一个正整数 N
"""

# 输出格式
"""
输出一行，形式为 N=a1xa2xa3...ai，将 N 表示成 i 个质因数相乘的形式，并且这 i 个质因数从小到大排列
"""

# 输入样例
"""
15
"""

# 输出样例
"""
15=3x5
"""


def divPrime(n):
    """ 分解质因数 """
    lst = []
    print(n, '=', sep='', end='')
    while n != 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:  # i是n的一个质因数
                lst.append(i)
                n = n / i  # 将n除以i，剩下的部分继续分解
                break
    for i in range(0, len(lst) - 1):
        print(lst[i], 'x', sep='', end='')

    print(lst[-1])


if __name__ == "__main__":
    n = int(input(""))
    divPrime(n)