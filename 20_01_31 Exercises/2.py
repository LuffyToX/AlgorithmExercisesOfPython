# -*- coding:utf-8 -*-

"""
一个数如果恰好等于它的因子之和，这个数就称为“完数”。
例如 6=1＋2＋3。

编程找出1000以内的所有完数。
"""

class Complete:
    def __init__(self, num):
        self.num = num

    def juge_com_num(self, x):
        """ 判断是否是完数 """
        lst = []
        n = 1
        while n < x:
            if x % n == 0:
                lst.append(n)
            n = n + 1

        if sum(lst) == x:
            return True
        else:
            return False

    def com_num(self):
        """ 输出所有完数 """
        lst_com = []
        for n in range(1, self.num+1):
            if self.juge_com_num(n):
                lst_com.append(n)
        print(lst_com)


if __name__ == "__main__":
    n = 1000
    com = Complete(n)
    com.com_num()
