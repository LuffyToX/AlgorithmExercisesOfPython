# -*- coding:utf-8 -*-

"""
有 1、2、3、4 四个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""


def main():
    result = []
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i!=j and i!=k and j!=k:
                    num = 100*i + 10*j + k
                    if num not in result:
                        result.append(num)
                        count += 1
    print(result)
    print(count)

if __name__ == "__main__":
    main()