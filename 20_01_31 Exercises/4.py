# -*- coding:utf-8 -*-

"""
古典问题：
有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死。

问每个月的兔子总数为多少？
"""


def rabbit(n):
    """ 第 n 个月的兔子数 """
    if n==1 or n==2:
        return 1
    else:
        return rabbit(n-1)+rabbit(n-2)

def main(num):
    """ 打印每个月的兔子数 """
    for i in range(1, num+1):
        print("第 %d 个月兔子数是：%d"%(i, rabbit(i)))


if __name__ == "__main__":
    num = int(input("想要打印多少个月的兔子数呢？"))
    main(num)
