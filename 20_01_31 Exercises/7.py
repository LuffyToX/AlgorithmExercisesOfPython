# -*- coding:utf-8 -*-

"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
"""


import re

class Chara_num:
    def __init__(self, _str):
        self._str = _str

    def method_1(self):
        """ 使用正则表达式 """
        chara = re.findall(r'[a-zA-Z]', self._str)       # 英文字母
        num = re.findall(r'[0-9]', self._str)            # 数字
        blank = re.findall(r' ', self._str)              # 空格
        chi = re.findall(r'[\u4E00-\u9FFF]', self._str)  # 汉字（汉字的Unicode编码范围）
        other = len(self._str) - len(chara) - len(num) - len(blank) - len(chi)
        print('字母', len(chara), '\n数字', len(num), '\n空格', len(blank), '\n中文', len(chi), '\n其他', other)

    def method_2(self):
        """ 使用方法 """
        letters = []
        spaces = []
        digits = []
        others = []
        for i in iter(self._str):  # iter 用来生成迭代器
            if i.isalpha():
                letters.append(i)
            elif i.isspace():
                spaces.append(i)
            elif i.isdigit():
                digits.append(i)
            else:
                others.append(i)
        print('''
        字母: {}, 个数: {}
        空格: {}, 个数: {}
        数字: {}, 个数: {}
        其他: {}, 个数: {}'''\
              .format(letters, len(letters), spaces, len(spaces), digits, len(digits), others, len(others)))

if __name__ == "__main__":
    string = input("请输入一行字符：")
    chara_num = Chara_num(string)
    chara_num.method_1()
    #chara_num.method_2()
