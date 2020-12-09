def Day1():  # 定义方法，顺便学学如何自定义函数
    # 循环输出1到100
    # function1
    for x in range(100):
        print(x + 1)
    # function2
    for x in range(1, 101):
        print(x)


def Day2():
    # 输出1到100之间的奇数
    # function1
    for x in range(1, 101, 2):
        print(x)
    # function2
    for x in range(1, 101):
        if x % 2 == 1:
            print(x)


def Day3():
    # 用逗号连接1-10
    str_link = ","
    list_1_10 = []
    for x in range(1, 11):
        list_1_10.append(str(x))  # append 在列表的末尾添加元素
    # print(list_1_10)
    print("Day3  ", str_link.join(list_1_10))  # join 连接字符串，连接的对象必须是字符串
    return str_link.join(list_1_10)


def Day4(str1_10):
    # 把刚刚生成的1-10的字符串按照逗号切割为10个元素存放到一个列表里
    import re  # 引入正则表达式这个包
    save_split = re.split(",", str1_10)  # re.split("切割符", "带切割字符串")  返回一个列表（这个列表里的元素是str类型）
    """
    re这个包需要重点学习一下，常用的还有下面三个：
    替换 re.sub()
    匹配所有 re.findall()
    有无匹配 re.match()
    """
    print("Day4  ", save_split)
    return save_split


def Day5(list1_10):
    """
    将昨天生成的数组（1-10）写入到名称任意的txt文件中，样式如下
    (文件开始)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    (文件结束)
    """
    with open("lalala.txt", mode='w', encoding='utf-8') as f1:
        for x in list1_10:
            f1.write(x)
            if x != list1_10[-1]:  # 目的是让文件的最后一行没有"\n"，其实无所谓了
                f1.write("\n")


def Day6():
    # 读取昨天生成的文件，把那10个数字写入到数组中，即[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    import re
    save = []
    with open("lalala.txt", mode='r') as f1:
        for x in f1:
            save.append(int(re.sub('\n', '', x)))
    print("Day6  ", save)


def Day7():
    # 学习一下集合,有a和b两个列表，请输出a和b的交集、交集个数、并集、并集个数。
    # 填空：集合具有___和___的特点。
    a = ['a', 'a', 'b', 'c', 'd']
    b = ['b', 'c', 'd', 'e']
    intersection = set(a) & set(b)
    intersection_length = len(intersection)
    union = set(a) | set(b)
    union_length = len(union)
    print("交集：", intersection)
    print("并集：", union)


def Day8():
    # 周末大作业(周六日完成)
    # 读hhh.txt文件
    # 生成以下字典
    # {'A': ['c', 'a', 'b', 'd'], 'B': ['a', 'd'], 'C': ['a', 'e']}
    import re  # 调用re模块，这是个正则表达式的包
    A_dic = {}  # 定义一个空的字典
    with open("hhh.txt", mode='r', encoding='utf-8') as f1:
        # 以with open 这种方式打开文件，这种方式相比你的那种方式最大的优点就是不用关
        # mode是选择读写方式，encoding是选择编码方式
        for x in f1:  # 按行读取，注意这很重要，因为我们处理的经常是很大的文件，我们不可能把所有的文件全都放到内存里，所以一行一行读取，是一种很好的方式。
            x = re.sub("\n", '', x)  # 去除行尾符。用到的是re包中的sub替换功能，把\n替换为了空
            save_split = re.split("\t", x)  # 把这行文件按照\t切割，并把切割后的结果赋值给了列表save_split
            A_dic.setdefault(save_split[0], set()).add(save_split[1])   # 学会setdefault函数
            """
            字典名称.setdefault()方法
            
            字典名称.setdefault(key名称, set()).add(value名称)
            （1）这个方法的功能是，如果这个字典中没有这个key名称，那么就在这个字典中添加上这个key，并把这个key对应的value设置成set() {ps:set()是集合的赋空方式}，
            然后再把value名称添加到空集合中 {ps .add()是往集合里添加元素，类似于.append()往列表里添加元素}
            (2)如果这个字典中有这个key名称,则直接在这个key对应的value上添加上后面的value名称这个值。
            
            那么为什么要把，字典的value的类型设置成集合呢？
            答：为了去重
            
            课后思考？
            字典名称.setdefault(key名称, []).append(value名称)的作用?
            课后拓展
            字典名称.setdefault(key名称, {}).setdefault(名称, set()).add(value名称)
            """

    # 上面的代码生成了{'A': {'c', 'a', 'b', 'd'}, 'B': {'a', 'd'}, 'C': {'a', 'e'}}的结果，字典的value是集合，下面的代码是把字典的value改为列表。
    for dict_item in A_dic:  # 集合转列表
        A_dic[dict_item] = list(A_dic[dict_item])
    print(A_dic)
# 下周计划
# 学习csv文件的读写（用csv模块）
# 学习json文件的读写(用json模块)


def Day9():
    # 自定义一个函数，它的功能是两数相加，并在主函数中调用此函数。
    # 主函数中已经有了两个变量a=1  b=2  通过调用自定义函数，返回一个值赋予给变量c。
    # 参考答案 略
    pass


def Day10():
    # 周2作业
    # 通过csv模块读取Day10.csv文件的每一行，并输出到控制台
    import csv
    with open("Day10.csv") as f1:
        reader1 = csv.DictReader(f1)  # 读取csv文件 csv.DictReader(句柄)
        for row in reader1:
            print(row)  # 查看每行结果，你会发现每一行都是一个字典结构， 且不会输出第一行，第一行作为了列名


def Day11():
    # 周3作业
    # 通过csv模块读取Day10.csv文件,并生成两个字典
    # key2value1 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    # key2value2 = {'A': '1', 'B': '1', 'C': '2', 'D': '2'}
    import csv
    key2value1 = {}
    key2value2 = {}
    with open("Day10.csv") as f1:
        reader1 = csv.DictReader(f1)
        for row in reader1:
            key2value1[row["key"]] = row["value1"]
            key2value2[row["key"]] = row["value2"]
    print(key2value1)
    print(key2value2)


def Day12():
    # Day12:
    # 将两个字典按照Day10.csv的样式，写入到Day12.csv中
    import csv
    key2value1 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    key2value2 = {'A': '1', 'B': '1', 'C': '2', 'D': '2'}
    with open('作业所需文件/Day12.csv', mode='w', encoding='utf-8', newline='') as f1:
        writer = csv.writer(f1)
        head = ['key', 'value1', 'value2']
        writer.writerow(head)
        save = []
        for x in key2value1:
            save.append(x)
            if key2value1.__contains__(x):
                save.append(key2value1[x])
            else:
                save.append("")
            if key2value2.__contains__(x):
                save.append(key2value2[x])
            else:
                save.append("")
            writer.writerow(save)
            save = []


def Day13():
    pass


def Day14():
    # 通过requests这个包获取https://scihub.wikicn.top/10.1007/s00432-019-03087-8这个网站上的html内容，并把html内容输出到控制台
    # 参考https://blog.csdn.net/xc_zhou/article/details/81021496    前面一部分就足矣了
    import requests
    response = requests.get("https://scihub.wikicn.top/10.1007/s00432-019-03087-8")
    print(response.text)


def Day15():
    # 目标：学习BeautifulSoup这个包
    # 参考：https://cuiqingcai.com/1319.html   看参考文章的第4部分（创建对象）和第7部分（搜索文档树）即可
    # 题目：从Day14获取的html中提取这个div的内容（提示，属性id具有唯一性）：
    # <div id="buttons">
    # <ul>
    # <li id="reload"><a href="//scholar.google.com/" target="_blank">⇣ Google Scholar</a></li>
    # <li><a href="#" onclick="location.href='https:\/\/sci.bban.top\/pdf\/10.1007\/s00432-019-03087-8.pdf?download=true'">⇣ save</a></li>
    # </ul>
    # </div>
    import requests
    from bs4 import BeautifulSoup
    response = requests.get("https://scihub.wikicn.top/10.1007/s00432-019-03087-8")
    soup = BeautifulSoup(response.text)
    for x in soup.find_all(id='buttons'):
        print(x)


def Day16():
    # 目的：继续学习BeautifulSoup这个包
    # 参考：自己探索吧
    # 题目：从Day15提取的div中的下载链接https:\/\/sci.bban.top\/pdf\/10.1007\/s00432-019-03087-8.pdf?download=true
    import requests
    from bs4 import BeautifulSoup
    import re
    response = requests.get("https://scihub.wikicn.top/10.1007/s00432-019-03087-8")
    soup = BeautifulSoup(response.text)
    # for x in soup.find_all(id='buttons'):
    #     print(x)
    soup.find(id='buttons')
    for y in soup.find(id='buttons').find_all("a"):
        try:
            down_url = re.split("'", y["onclick"])[1]
            print(down_url)
        except:
            pass


if __name__ == '__main__':
    # Day1()
    # Day2()
    # str_1_10 = Day3()  # 调用方法
    # list_1_10 = Day4(str_1_10)
    # Day5(list_1_10)
    # Day6()
    # Day7()
    # Day8()
    # Day10()
    # Day11()
    # Day12()
    # Day14()
    Day15()
