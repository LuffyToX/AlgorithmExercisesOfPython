# -*- coding:utf-8 -*-

# 题目（p 和 q）
"""
已知两个正整数 p 和 q 的最大公约数 m 和最小公倍数 n（1<m<p<q<n），求 p 和 q
"""

# 输入格式
"""
输入共一行，两个正整数 m 和 n，分别表示 p 和 q 的最大公约数和最小公倍数，数与数之间以一个空格分开
"""

# 输出格式
"""
输出共一行，两个正整数 p 和 q，数与数之间以一个空格分开
"""


def p_q(m, n):
    m = int(m)
    n = int(n)
    for p in range(m, n+1):
        for q in range(p+1, n+1):
            if p*q == m*n:
                print(p, q)


if __name__ == "__main__":
    m, n = input("请输入最大公约数和最小公倍数：").split()
    p_q(m, n)
