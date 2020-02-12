# -*- coding:utf-8 -*-

# 题目（闰年）
"""
闰年是古人为了弥补历法的年度天数与地球实际公转周期的时间差而设立的，因此闰年的 2 月有 29 天。
请编写一个程序，判断某一年是否为闰年
"""

# 输入格式
"""
输入一个非负整数，表示年份
"""

# 输出格式
"""
输出一个大写单词，如果是闰年，输出 YES，否则输出 NO
"""

# 输入样例
"""
2000
"""

# 输出样例
"""
YES
"""

class LeapYear:
    """ 判断是否是闰年 """
    def __init__(self, year):
        self.year = int(year)

    def judge(self):
        """
        闰年是能被4整除并且不能被100整除
        或可以被400整除的年份
        """
        out = ((self.year%4 == 0) and (self.year%100 != 0)) or (self.year%400 == 0)
        return out

    def print_(self):
        print_out = self.judge()
        if print_out:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    try:
        year = input("请输入一个表示年份的整数：")
        leap = LeapYear(year)
        leap.print_()
    except Exception:
        print("请输入一个表示年份的整数！")