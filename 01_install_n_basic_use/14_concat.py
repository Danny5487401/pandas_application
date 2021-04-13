# Pandas实现数据的合并concat
"""
#### 使用场景：
批量合并相同格式的Excel、给DataFrame添加行、给DataFrame添加列
"""
#### 一句话说明concat语法：
"""
* 使用某种合并方式(inner/outer)
* 沿着某个轴向(axis=0/1)
* 把多个Pandas对象(DataFrame/Series)合并成一个。
"""
"""
#### concat语法：pandas.concat(objs, axis=0, join='outer', ignore_index=False)
* objs：一个列表，内容可以是DataFrame或者Series，可以混合
* axis：默认是0代表按行合并，如果等于1代表按列合并
* join：合并的时候索引的对齐方式，默认是outer join，也可以是inner join
* ignore_index：是否忽略掉原来的数据索引

#### append语法：DataFrame.append(other, ignore_index=False)
append只有按行合并，没有按列合并，相当于concat按行的简写形式  
* other：单个dataframe、series、dict，或者列表
* ignore_index：是否忽略掉原来的数据索引
"""
#### 参考文档：
# * pandas.concat的api文档：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
# * pandas.concat的教程：https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# * pandas.append的api文档：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

### 一、使用pandas.concat合并数据

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    'E': ['E0', 'E1', 'E2', 'E3']
                   })

df2 = pd.DataFrame({ 'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7'],
                     'F': ['F4', 'F5', 'F6', 'F7']
                   })
# ***1、默认的concat，参数为axis=0、join=outer、ignore_index=False***
df3 = pd.concat([df1,df2])
# print(df3)

# ***2、使用ignore_index=True可以忽略原来的索引***重新排布
df4 = pd.concat([df1,df2], ignore_index=True)
# print(df4)

# ***3、使用join=inner过滤掉不匹配的列***
df5 = pd.concat([df1,df2], ignore_index=True, join="inner")
# print(df5)

# ***4、使用axis=1相当于添加新列***
# ***A：添加一列Series***
s1 = pd.Series(list(range(4)), name="F")
df6 = pd.concat([df1,s1], axis=1)
# print(df6)

# ***B：添加多列Series***

s2 = df1.apply(lambda x:x["A"]+"_GG", axis=1)
s2.name="G"
df7 = pd.concat([df1,s1,s2], axis=1)
# print(df7)
# 列表可以只有Series
df8 =pd.concat([s1,s2], axis=1)
# print(df8)
# 列表是可以混合顺序的
df9 = pd.concat([s1,df1,s2], axis=1)
# print(df9)

### 二、使用DataFrame.append按行合并数据

df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))

# ***1、给1个dataframe添加另一个dataframe***
df3 = df1.append(df2,ignore_index=True)
print(df3)

#***2、可以一行一行的给DataFrame添加数据***
df = pd.DataFrame(columns=['A'])
#***A：低性能版本***
for i in range(5):
    # 注意这里每次都在复制
    df = df.append({'A': i}, ignore_index=True)

# ***B：性能好的版本***
# 第一个入参是一个列表，避免了多次复制
pd.concat(
    [pd.DataFrame([i], columns=['A']) for i in range(5)],
    ignore_index=True
)