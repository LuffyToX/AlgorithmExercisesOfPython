# -*- coding:utf-8 -*-

"""
一个整数，它加上 100 后是一个完全平方数，再加上 168 又是一个完全平方数，请问该数是多少？
"""


import math

def is_square_num(num):
    """
    1. 完全平方数开根号后是一个整数，非完全平方数开根号后是一个非整数
    2. 开根号后取整，如果开根号后是整数的话就不会改变值的大小
    3. 取整后再平方，如果值和之前一样，说明是完全平方数
    """
    a = int(math.sqrt(num))
    return a*a == num

def main():
    n = 1
    while True:
        if is_square_num(n+100) and is_square_num(n+100+168) == True:
            print(n)
            break
        n = n + 1

if __name__ == "__main__":
    main()