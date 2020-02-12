# -*- coding:utf-8 -*-

""" 便利店优化算法 """

def convience_store():
    """ 便利店 """
    n = int(input(""))

    cus_in_0, cus_out_0 = [int(k) for k in input("").split()]

    time_1 = cus_out_0 - cus_in_0
    time_0 = 0

    for i in range(n - 1):
        cus_in, cus_out = [int(k) for k in input("").split()]
        if cus_in > cus_out_0:
            time_0 = max(time_0, cus_in - cus_out_0)
            cus_in_0 = cus_in
            cus_out_0 = cus_out
        elif cus_out > cus_out_0:
            cus_out_0 = cus_out
        time_1 = max(time_1, cus_out_0 - cus_in_0)

    print(time_1, time_0)


if __name__ == "__main__":
    convience_store()