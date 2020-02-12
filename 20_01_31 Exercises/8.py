# -*- coding:utf-8 -*-

# 题目
"""
已知正整数 N 是两个连续自然数的乘积，输出其中较小的那个乘数
"""

# 输入格式
"""
一个正整数
"""

# 输出格式
"""
一个正整数，即较小的那个乘数
"""

# 输入样例
"""
12
"""

# 输出样例
"""
3
"""


import math

def MultipleMin(a):
    i = 1
    while True:
        if i*(i+1) == a:
            result = i
            break
        else:
            i += 1
        if i >= math.sqrt(a):
            str = "该数没有连续自然数乘积的形式"
            return str
    return result

if __name__ == "__main__":
    try:
        a = int(input("请输入一个正整数："))
        result = MultipleMin(a)
        print(result)

    except Exception:
        print("请检查输入是否为正整数形式")
