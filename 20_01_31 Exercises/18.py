# -*- coding:utf-8 -*-

""" 求两个正整数的最小公倍数 """


def Euclidean(a, b):
    """ 欧几里得算法（辗转相除法） """
    if a < b:
        # a 存大数
        a, b = b, a

    t = a % b

    while t != 0:
        a = b
        b = t
        t = a % b
    return b

if __name__ == "__main__":
    try:
        a, b = input("请输入两个整数：").split()
        a = int(a)
        b = int(b)
        print(int((a*b)/Euclidean(a,b)))
    except Exception:
        print("请按指定格式输入！")
