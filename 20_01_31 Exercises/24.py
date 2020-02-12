# -*- coding:utf-8

# 题目（连续自然数的和）
"""
已知 N 是从 a 到 b 的连续自然数的和（1<=a<=b<=N），输出 a 和 b 的所有可能组合
"""

# 输入格式
"""
一个正整数 N
"""

# 输出格式
"""
输出若干行，每一行两个正整数 a 和 b，表示从 a 累加到 b 的和是 N，a 和 b 之间以一个空格分开。
每行以 a 的升序输出，最后一行显然只能是 N 和 N
"""

# 输入样例
"""
6
"""

# 输出样例
"""
1 3
6 6
"""


def con_num_and(n):
    """ a 和 b 的所有组合 """
    lst = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            if (i+j)*(j-i+1)/2 == n:
                lst.append(i)
                lst.append(j)
    # 将列表分成两个一组的嵌套列表
    result = [lst[i:i+2] for i in range(0, len(lst), 2)]
    return result


if __name__ == "__main__":
    n = int(input("请输入一个正整数N："))
    compose = con_num_and(n)
    for com in compose:
        print(com[0], ' ', com[1], sep='')
