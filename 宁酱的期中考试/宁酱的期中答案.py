# -*- coding: utf-8 -*-
# @Time : 2020/11/24 22:40
# @Author : 张宇鹏
# @FileName: 宁酱的期中答案.py
import csv


def A1(P1):
    sequence_S = []
    S_dic = {}
    # 读取csv，获取序列列表
    with open('Pho.csv') as f1:
        reader1 = csv.DictReader(f1)
        for row in reader1:
            if row["Amino acid"] == P1:
                sequence_S.append(row['Sequence window'])

    # 创造字典
    for x in sequence_S:
        index = 1
        for y in x[9:22]:
            S_dic.setdefault(y, {}).setdefault(str(index), []).append(y)

            # {"A": {"1": ["A", "A", "A"], "2": ["A", "A", "A"]}, "C": {"1": ["C"], "2": ["C"]}}

            index = index + 1
    print(S_dic)
    # 写入csv
    with open(P1 + '.csv', mode='w', encoding='utf-8', newline='') as f2:
        writer1 = csv.writer(f2)
        head = ['acid', '-6', '-5', '-4', '-3', '-2', '-1', P1, '1', '2', '3', '4', '5', '6']
        writer1.writerow(head)
        save = []
        aa = ['_', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', "R", 'S', 'T', 'V', 'W', 'Y']
        for x in aa:
            save.append(x)
            for y in range(1, 14):
                if S_dic[x].__contains__(str(y)):
                    save.append(len(S_dic[x][str(y)]) / len(sequence_S))
                else:
                    save.append("0")
            writer1.writerow(save)
            save = []


if __name__ == '__main__':
    P = ["S", "T", "Y"]
    for x in P:
        A1(x)
        print(x, "已完成")
