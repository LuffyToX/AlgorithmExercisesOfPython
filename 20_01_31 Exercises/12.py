# -*- coding:utf-8 -*-

# 题目（便利店）
"""
楼下的便利店 7 点开始营业，小核桃假设从 7 点开始是第 0 秒，
然后记录每一个顾客的进店秒数和离店秒数。
比如顾客 a 的进店秒数是 300，离店秒数是 600，表示此顾客是 7 点 05 分进店，7 点 10 分离店。
小核桃记录一段时间后开始统计，从第一个顾客进店开始，最长的店里无顾客时间和最长的店里有顾客时间。
"""

# 输入格式
"""
输入若干行，第一行一个正整数 N，表示记录了N个顾客。
接下来 N 行，每行两个非负整数，分别表示顾客的进店秒数和离店秒数，数与数之间以一个空格分开
"""

# 输出格式
"""
输入一行，两个非负整数，分别表示求出来的两个时间，数与数之间以一个空格分开
"""

# 输入样例
"""
3
300 600
500 800
1000 1300
"""

# 输出样例
"""
500 200
"""

def convenience_store(lst_in, lst_out):
    """ 便利店 """
    time_in = []
    time_out = []

    if len(lst_in) != 1:
        for i in range(len(lst_in) - 1):
            if lst_out[i] < lst_in[i + 1]:  # 无人时间
                time_out.append(lst_in[i + 1] - lst_out[i])
            else:  # 有人时间
                min_time = lst_in[i]
                j = i
                while lst_out[j] >= lst_in[j + 1]:
                    max_time = lst_out[j + 1]
                    j = j + 1
                    if j == len(lst_in) - 1:
                        break
                # print(max_time, min_time)
                time_in.append(max_time - min_time)
    else:  # 只记录了一个人
        print(lst_out[0]-lst_in[0], 0)


    if time_out != [] and time_in != []:
        print(max(time_in), max(time_out))
    elif time_out == [] and time_in != []:
        print(max(time_in), 0)
    elif time_out != [] and time_in == []:
        print(0, max(time_out))


if __name__ == "__main__":
    n = int(input("小核桃记录了多少个顾客？\n"))

    lst_in = []
    lst_out = []

    for i in range(1, n + 1):
        print("第 %d 个" % i, end='')
        cus_in, cus_out = input("顾客的进店离店时间？\n").split()
        lst_in.append(int(cus_in))
        lst_out.append(int(cus_out))

    convenience_store(lst_in, lst_out)
