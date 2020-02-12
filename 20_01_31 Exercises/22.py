# -*- coding:utf-8 -*-

# 题目（质因数分解升级版）
"""
已知正整数 N 是若干（>1）个质数的乘积，如果某一个质因数 a 出现的次数 b 大于 1，可以节写成 a^b 的形式
"""

# 输入格式
"""
输入一个正整数N
"""

# 输出格式
"""
首先输出一行，形式为 N=a1xa2xa3...ai，将 N 表示成 i 个质因数相乘的形式，并且这 i 个质因数从小到大排列
如果某些因数出现的次数大于 1，那么另起一行输出更简洁的形式，将这些因数写成a^b的形式
不同因数之间仍然按照从小到大的顺序排列，第二行的等号和第一行的等号对齐
"""

# 输入样例
"""
36
"""

# 输出样例
"""
36=2x2x3x3
  =2^2x3^2
"""


class Div:
    def __init__(self, n):
        self.n = n
        self.lst = []


    def divPrime(self):
        """ 分解质因数 """
        num = int(self.n)
        print(num, '=', sep='', end='')
        while num != 1:
            for i in range(2, int(num + 1)):
                if num % i == 0:  # i是n的一个质因数
                    self.lst.append(i)
                    num = num / i  # 将n除以i，剩下的部分继续分解
                    break
        for i in range(0, len(self.lst) - 1):
            print(self.lst[i], 'x', sep='', end='')

        print(self.lst[-1])

    def form_cha(self):
        """ 转换成指数的形式 """
        #print(' '*len(self.n)+'=', end='')

        # 统计列表中某元素的个数
        dict = {}
        for key in self.lst:
            dict[key] = dict.get(key, 0) + 1

        # 按 key 升序排序
        items = list(dict.items())
        items.sort()
        result = []
        for key, value in items:
            if value > 1:
                string_m = str(key)+'^'+str(value)
                result.append(string_m)
            else:
                string = str(key)
                result.append(string)

        for exp in result:
            if '^' in exp:
                print(' '*len(self.n)+'=', end='')
                print('x'.join(result))
                break

if __name__ == "__main__":
    n = input("请输入一个正整数：")
    div = Div(n)
    div.divPrime()
    div.form_cha()