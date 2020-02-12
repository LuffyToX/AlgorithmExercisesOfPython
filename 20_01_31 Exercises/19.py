# -*- coding:utf-8 -*-

# 题目（点的变换）
"""
给定一个点的坐标，对它进行一到两次的几何变换（平移/点对称）操作，得到新的坐标
"""

# 输入格式
"""
输入共三行:
第一行表示已知点的 x 坐标和 y 坐标;
第二行表示进行变换的次数（1或2）和每次的变换名称（move表示平移、sym表示对称）;
第三行根据第二行的操作内容给出平移向量或者对称点坐标。
"""

# 输出格式
""" 
输出共一行，包含两个整数，分别表示进行变换后的x坐标和y坐标，数与数之间以一个空格分开
"""

# 输入样例
"""
3 5
2 move sym
2 1 7 5
"""

# 输出样例
"""
9 4
"""


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def move(self, dis_x, dis_y):
        self.x += int(dis_x)
        self.y += int(dis_y)
        return self.x, self.y

    def sym(self, sym_x, sym_y):
        self.x = 2*int(sym_x) - self.x
        self.y = 2*int(sym_y) - self.y


if __name__ == "__main__":
    axis_x, axis_y = input("请输入原坐标：").split()
    num, *act = input("请输入操作次数以及操作的类型：").split()
    axis_x_act, axis_y_act, *left = input("请输入操作的坐标：").split()
    point = Point(axis_x, axis_y)

    num = int(num)
    if num == 1:
        if act[0] == 'move':
            point.move(axis_x_act, axis_y_act)
        else:
            point.sym(axis_x_act, axis_x_act)
    else:
        if act[0] == 'move' and act[1] == 'move':
            point.move(axis_x_act, axis_y_act)
            point.move(left[0], left[1])
        elif act[0] == 'move' and act[1] == 'sym':
            point.move(axis_x_act, axis_y_act)
            point.sym(left[0], left[1])
        elif act[0] == 'sym' and act[1] == 'sym':
            point.sym(axis_x_act, axis_y_act)
            point.sym(left[0], left[1])
        else:
            point.sym(axis_x_act, axis_y_act)
            point.move(left[0], left[1])
    print(point.x, point.y)

