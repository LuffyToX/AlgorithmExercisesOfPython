# -*- coding:utf-8 -*-

""" 西游记词频统计 """

import os
os.chdir(r'C:\Users\hetao\Desktop\生产实习\练习\第一周\2')
fr = open('西游记.txt', 'r', encoding='UTF-8')  # 使用 utf-8 编码（参数 encoding 解决编码问题）

characters = []
stat = {}

for line in fr:  # 按行读取
	line = line.strip()
	if len(line) == 0:
		continue
	line = str(line)

	for word in range(len(line)):  # 遍历该行的每一个字
		# 去掉标点符号和空白符
		if line[word] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# 尚未记录在characters中
		if line[word] not in characters:
			characters.append(line[word])
		# 尚未记录在stat中
		if line[word] not in list(stat.keys()):
			stat[line[word]] = 0
		# 汉字出现次数加1
		stat[line[word]] += 1
print("西游记出现了 %d 个不同的字。\n每个字出现了多少次存储在\"词频统计.csv\"文件中。"%len(characters))

# lambda生成一个临时函数，d表示字典的每一对键值对，d[0]为key，d[1]为value
# 依据词频降序排序
stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)

fw = open('词频统计.csv', 'w', encoding='utf-8')
for item in stat:
	fw.write(item[0] + ': ' + str(item[1]) + '\n')
fr.close()
fw.close()
