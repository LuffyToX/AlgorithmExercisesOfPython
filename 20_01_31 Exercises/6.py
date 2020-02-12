# -*- coding:utf-8 -*-

"""
输入某年某月某日，判断这一天是这一年的第几天？
"""


import datetime

def judge_day(year, month, day):
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)  # 做差
    return (date1 - date2).days + 1


if __name__ == "__main__":
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    string = '/'.join([year, month, day])
    print("%s 是 %s 的第 %d 天。"%(string, year, judge_day(year, month, day)))