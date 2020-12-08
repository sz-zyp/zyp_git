宁酱的每日python题目
不好意思，一下子出完了，明年再见，加油 gogogo


Day19（周日，今年最后一个，耶）
    目的：（1）学习pubmed_API的另外一个：PMID到题录信息
         （2）学习xml  需要用到这个包xml.etree.ElementTree
    题目：由Day18的PMID得到对应的doi
    参考：
    （1）API参考（还是老师的教诲，如下）
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=33014839,32887021,32618099&rettype=
    你可以直接搜索该网址，查看一下结果
        参数说明：
        https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?     pubmed_API的另外一个，功能是通过PMID获取题录信息（好像还有4,5个API，我们就不学了，因为我也没用过，嘤嘤嘤）
        db=pubmed                                                      用的数据库是pubmed
        &retmode=xml                                                   访问后得到的是xml类型的数据
        &id=33014839,32887021,32618099                                 PMID，ID之间用英文的逗号连接
    （2）xml学习参考，我们用xml.etree.ElementTree这个包
        参考：https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#parsing-xml
        1.包的调用，这个包的调用用如下方式，正好也可以学习一下try异常处理，try的用法可以参考：https://www.runoob.com/python/python-exceptions.html
        try:  # try的意思是运行如下命令，如果报错则执行except里的命令
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET
        2.xml格式说明：xml的格式也是层层嵌套的关系
        例如我们要获取的doi就在标签 PubmedArticle -> PubmedData -> ArticleIdList -> ArticleId属性IdType为doi的下面
        3.包的使用  主要还是findall()函数


Day18(周六)
    目的：学习pubmed_API的其中一个：keyword到PMID
    参考：老师的教诲，如下
        https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term="breast+cancer"+AND+("Tandem+mass+tag"+OR+"TMT")&retmode=json&retmax=100000
        你可以直接搜索该网址，查看一下结果
        参数说明：
            https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?     pubmed_API的其中一个，功能是通过搜索关键词得到文献ID
            db=pubmed                                                       用的数据库是pubmed
            &term="breast+cancer"+AND+("Tandem+mass+tag"+OR+"TMT")          term后跟检索式，注意检索式中的空格被加号替代
            &retmode=json                                                   访问后得到的是json类型的数据
            &retmax=100000                                                  能够搜到的最大文献数目上限
            &reldate=360&datetype=pdat&usehistory=y                         此外，还有这些参数
    题目：有一个检索式   "breast cancer" AND ("Tandem mass tag" OR "TMT")
         通过访问pubmed的API，得到检索式对应的PMID号码
    特别注意：访问API不要过于频繁，不能在1秒内访问超过3次，否则封ip

Day17(周五)
    目的：json文件的读和写
    参考：https://www.cnblogs.com/bigberg/p/6430095.html
    题目：
    （1）有一字符串如下所示，转化为字典类型，并写入到D17.json文件中
    Day17_str = {"A": "a", "B": "b", "C": ["1", "2", "3"]}
    (2)读取D17.json文件，并把字典类型的值赋予给变量Day17_dic

Day16（周四）
    目的：继续学习BeautifulSoup这个包
    参考：自己探索吧
    题目：从Day15提取的div中的下载链接https:\/\/sci.bban.top\/pdf\/10.1007\/s00432-019-03087-8.pdf?download=true

Day15（周三）:
    目标：学习BeautifulSoup这个包
    参考：https://cuiqingcai.com/1319.html   看参考文章的第4部分（创建对象）和第7部分（搜索文档树）即可
    题目：从Day14获取的html中提取这个div的内容（提示，属性id具有唯一性）
    <div id="buttons">
    <ul>
        <li id="reload"><a href="//scholar.google.com/" target="_blank">⇣ Google Scholar</a></li>
        <li><a href="#" onclick="location.href='https:\/\/sci.bban.top\/pdf\/10.1007\/s00432-019-03087-8.pdf?download=true'">⇣ save</a></li>
    </ul>
    </div>

Day14:
    通过requests这个包获取https://scihub.wikicn.top/10.1007/s00432-019-03087-8  这个网站上的html内容，并把html内容输出到控制台
    参考https://blog.csdn.net/xc_zhou/article/details/81021496    前面一部分就足矣了

Day13:
    开始学习爬虫
    学习html基础
    了解以下概念，晚上提问
    一、什么叫
    （1）标签 tag
    （2）属性 attribute
    （3）文本 text
    二、常用元素的作用
    （1）p标签
    （2）a标签
    （3）h1标签
    （4）div

Day12:
    将两个字典按照Day10.csv的样式，写入到Day12.csv中
    key2value1 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    key2value2 = {'A': '1', 'B': '1', 'C': '2', 'D': '2'}

Day11:
    周3作业
    通过csv模块读取Day10.csv文件,并生成两个字典
    key2value1 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    key2value2 = {'A': '1', 'B': '1', 'C': '2', 'D': '2'}

Day10:
    周2作业
    参考：https://www.cnblogs.com/yanglang/p/7126660.html
    通过csv模块读取Day10.csv文件的每一行，并输出到控制台

Day9:
    自定义一个函数，它的功能是两数相加，并在主函数中调用此函数。
    主函数中已经有了两个变量a=1  b=2  通过调用自定义函数，返回一个值赋予给变量c。



