# -*- coding:utf-8 -*-

# 题目
"""
核桃编程的 n 个部门（n<10）一起去郊区团建，每个部门各有 A1, A2, A3 … An 个人。
预定的大巴车每辆可坐 40 人，每辆大巴车上有两名领队，求预定的大巴车数量
"""

# 输入格式
"""
输入 n+1 行，第一行一个正整数 n，接下来有 n 行，表示每个部门的人数
"""

# 输出格式
"""
输出一个正整数，表示需要乘坐大巴车的数量
"""

# 输入样例
"""
2
45
67
"""

# 输出样例
"""
3
"""


def num_car(lst):
    """ 求需要的大巴车数量 """
    sum_hetao = sum(lst)
    number = sum_hetao//(40-2)+1
    return number


if __name__ == "__main__":
    n = int(input(""))
    lst = []
    for i in range(1, n+1):
        lst.append(int(input("")))
    #print(lst)
    num = num_car(lst)
    print(num)

