# -*- coding: utf-8 -*-

# 题目（相似三角形）
"""
已知两个三角形的三条边均为正整数，判断这两个三角形是否相似
"""

# 输入格式
"""
输入共一行，包含 6 个正整数a、b、c、d、e、f，
其中 a、b、c 是一个三角形的三条边，d、e、f 是另一个三角形的三条边，数与数之间以一个空格分开
"""

# 输出格式
"""
输出一个大写单词，如果两个三角形相似输出 “YES”，否则输出 “NO”
"""

# 输入样例
"""
3 4 5 6 8 10
"""

# 输出样例
"""
YES
"""

class Resem_tri:
    def __init__(self, lst):
        lst_1 = []
        lst_2 = []
        for i in range(6):
            if i < 3:
                lst_1.append(int(lst[i]))
            else:
                lst_2.append(int(lst[i]))
        lst_1.sort()
        lst_2.sort()

        self.a = lst_1[0]
        self.b = lst_1[1]
        self.c = lst_1[2]
        self.d = lst_2[0]
        self.e = lst_2[1]
        self.f = lst_2[2]

    def judge_tri(self):
        """ 判断是否能构成三角形 """
        fir = (self.a + self.b) > self.c
        sec = (self.a + self.c) > self.b
        thi = (self.b + self.c) > self.a
        fot = (self.d + self.e) > self.f
        fif = (self.d + self.f) > self.e
        six = (self.e + self.f) > self.d
        return (fir and sec and thi and fot and fif and six)

    def resem(self):
        """ 判断是否相似 """
        if self.judge_tri:
            if self.a > self.d:
                label = (self.a / self.d) == (self.b / self.e) == (self.c / self.f)
            else:
                label = (self.d / self.a) == (self.e / self.b) == (self.f / self.c)

            if label == True:
                print("YES")
            else:
                print("NO")
        else:
            print("不能构成三角形")

if __name__ == "__main__":
    str = input("请输入两个三角形的三边长：").split()
    str_new = []
    for i in str:
        if i != ' ':
            str_new.append(i)
    res = Resem_tri(str_new)
    res.resem()