# -*- coding:utf-8 -*-

""" 判断三角形的类型 """

class TypeTriangle:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def judge(self):
        """ 判断是否可以构成三角形 """
        result = (self.a+self.b+self.c) == 180
        return result

    def acute_angle(self):
        """ 锐角三角形 """
        if self.judge():
            result = (self.a < 90) and (self.b < 90) and (self.c < 90)
            return result

    def abtuse_angle(self):
        """ 钝角三角形 """
        if self.judge():
            result = (self.a > 90) or (self.b > 90) or (self.c > 90)
            return result

    def right_angle(self):
        """ 直角三角形 """
        if self.judge():
            result = (self.a == 90) or (self.b == 90) or (self.c == 90)
            return result

    def isosceles_angle(self):
        """ 等腰三角形 """
        if self.judge():
            result = (self.a == self.b) or (self.a == self.c) or (self.b == self.c)
            return result

    def equilateral_angle(self):
        """ 等边三角形 """
        if self.judge():
            result = (self.a == self.b == self.c)
            return result

    def type_(self):
        if self.acute_angle():
            # 锐角三角形
            if self.equilateral_angle():
                # 等边三角形
                print("6")
                return
            elif self.isosceles_angle():
                # 等腰三角形
                print("4")
                return
            print("1")
        elif self.right_angle():
            # 直角三角形
            if self.isosceles_angle():
                # 等腰直角三角形
                print("5")
                return
            print("2")
        else:
            # 钝角三角形
            if self.isosceles_angle():
                # 等腰三角形
                print("4")
                return
            print("3")

if __name__ == "__main__":
    try:
        a, b, c = input("请输入三个值：").split()
        type_triangle = TypeTriangle(a, b, c)
        type_triangle.type_()
    except Exception:
        print("请按格式输入！")

