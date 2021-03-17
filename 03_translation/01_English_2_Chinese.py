"""
Python批量翻译英语单词
***用途：***
对批量的英语文本，生成英语-汉语翻译的单词本，提供Excel下载

***本代码实现：***
1. 提供一个英文文章URL，自动下载网页；
2. 实现网页中所有英语单词的翻译；
3. 下载翻译结果的Excel

***涉及技术：***
1. pandas的读取csv、多数据merge、输出Excel
2. requests库下载HTML网页
3. BeautifulSoup解析HTML网页
4. Python正则表达式实现英文分词
"""

### 1. 读取英语-汉语翻译词典文件
"""
词典文件来自：https://github.com/skywind3000/ECDICT
使用步骤：https://github.com/skywind3000/ECDICT
1. 下载代码打包：https://github.com/skywind3000/ECDICT/archive/master.zip
2. 解压master.zip，然后解压其中的‪stardict.csv文件
"""

import pandas as pd

# 注意：stardict.csv的地址需要替换成你自己的文件地址
df_dict = pd.read_csv("D:/tmp/ECDICT-master/stardict.csv")