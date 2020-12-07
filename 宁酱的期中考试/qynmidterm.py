# -*- coding: utf-8 -*-
# @Time : 2020/12/6 10:16
# @Author : 齐雅宁
# @File : qynmidterm.py
# @Software: PyCharm
# @Illustration:期中考试

import csv
acid_seq = {}# 读取文件，提取“Amino acid”和“Sequence window”列，变成字典
acidall = ''
with open("Pho.csv", "r") as f1:
    reader1 = csv.DictReader(f1)
    for row1 in reader1:
        acid = row1['Amino acid']
        seq = row1['Sequence window']
        acid_seq.setdefault(acid, list()).append(seq)
        acidall = acidall + seq
# print(acid_seq)
#print(acidall)
acidall = set(acidall)#所有氨基酸去重
acidall = list(acidall)
acidall.sort()
head = acidall
print(head)

acidall = tuple(acidall)
head.insert(0, 'acid')
for m in ['S', 'T', 'Y']:
    sacid = acid_seq[m]
    pos_radio = {}
    i_list = {}#位置-氨基酸残基列表
    for i in range(9, 22):
        ilist = []
        for isacid in sacid:
            print(isacid)
            ilist.append(isacid[i])
        i_list[i-15] = ilist
        lists_radio = []# [('A', 0.0843514875405536), ('C', 0.0015186028853454822), ('D', 0.05142541589010837),...]每个位置的氨基酸残基出现的比例
        for item in acidall:
            lists_radio.append((item, i_list[i-15].count(item)/len(i_list[i-15])))
            # print(lists_radio)
        radio = []
        for ilists_radio in lists_radio:
            radio.append(ilists_radio[1])
        pos_radio[i-15] = radio
    with open("" + m + ".csv", "w", newline='') as f2:
        writer2 = csv.writer(f2)
        writer2.writerow(head)
        key = list(pos_radio.keys())
        for j in key:
            pos_radio[j].insert(0, j)
            writer2.writerow(pos_radio[j])

"""
总分 90
基础分 60
代码结构分 20
惊艳到老师 10(有想法，进步空间还有很大哦，不愧是我的学生，哈哈哈)
惹老师生气 -100（看之后表现，不然扣光光）
"""

