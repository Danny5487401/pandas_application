## 03. Pandas数据结构

"""
1. Series
2. DataFrame
3. 从DataFrame中查询出Series

"""

import pandas as pd
import numpy as np
"""
### 1. Series

Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。
"""

#### 1.1 仅有数据列表即可产生最简单的Series

s1 = pd.Series([1,'a',5.2,7])
print(s1.index,s1.values)

#### 1.2 创建一个具有标签索引的Series
s2 = pd.Series([1, 'a', 5.2, 7], index=['d','b','a','c'])
print(s2.index)

#### 1.3 使用Python字典创建Series
sdata={'Ohio':35000,'Texas':72000,'Oregon':16000,'Utah':5000}
s3=pd.Series(sdata)
print(s3)

#### 1.4 根据标签索引查询数据:类似Python的字典dict
print(s2['a'])
print(s2[['b','a']])
print(type(s2[['b','a']])) # <class 'pandas.core.series.Series'>

### 2. DataFrame
"""
DataFrame是一个表格型的数据结构
* 每列可以是不同的值类型（数值、字符串、布尔值等）
* 既有行索引index,也有列索引columns
* 可以被看做由Series组成的字典

创建dataframe最常用的方法，见02节读取纯文本文件、excel、mysql数据库
"""

#### 2.1 根据多个字典序列创建dataframe
data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
    }
df = pd.DataFrame(data)

"""
### 3. 从DataFrame中查询出Series
* 如果只查询一行、一列，返回的是pd.Series
* 如果查询多行、多列，返回的是pd.DataFrame
"""
#### 3.1 查询一列，结果是一个pd.Series
print(type(df['year']))  #<class 'pandas.core.series.Series'>
#### 3.2 查询多列，结果是一个pd.DataFrame
print(type(df[['year', 'pop']]))  # <class 'pandas.core.frame.DataFrame'>
#### 3.3 查询一行，结果是一个pd.Series
print(type(df.loc[1]))  #<class 'pandas.core.series.Series'>
#### 3.4 查询多行，结果是一个pd.DataFrame
print(type(df.loc[1:3]))