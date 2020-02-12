# -*- coding:utf-8 -*-

"""
判断 101-200 之间有多少个素数，并输出所有素数
"""


def judge_prime(num_lst):
    prime_lst = []
    for num in num_lst:
        for i in range(2, num):
            if num % i == 0:
                # 不是素数
                break
        else:
            prime_lst.append(num)
    print(prime_lst)

if __name__ == "__main__":
    lst = []
    for i in range(101, 201):
        lst.append(i)
    judge_prime(lst)