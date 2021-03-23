## Pandas的SettingWithCopyWarning报警

### 0、读取数据

import pandas as pd

fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')


### 1、复现


# 只选出3月份的数据用于分析
condition = df["ymd"].str.startswith("2018-03")


# # 设置温差
# df[condition]["wen_cha"] = df["bWendu"]-df["yWendu"]
# # 查看是否修改成功
# print(df[condition].head())

"""
F:/pandas_application/01_install_n_basic_use/08_error_SettingWithCopyWarning.py:21: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead
"""
### 2、原因
"""
发出警告的代码
df[condition]["wen_cha"] = df["bWendu"]-df["yWendu"]

相当于：df.get(condition).set(wen_cha)，第一步骤的get发出了报警

***链式操作其实是两个步骤，先get后set，get得到的dataframe可能是view也可能是copy，pandas发出警告***

官网文档：
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

核心要诀：pandas的dataframe的修改写操作，只允许在源dataframe上进行，一步到位
"""

### 3、解决方法1

# 将get+set的两步操作，改成set的一步操作
df.loc[condition, "wen_cha"] = df["bWendu"]-df["yWendu"]
print(df[condition].head())



### 4、解决方法2
# 如果需要预筛选数据做后续的处理分析，使用copy复制dataframe
df_month3 = df[condition].copy()
df_month3["wen_cha"] = df["bWendu"]-df["yWendu"]
print(df_month3.head())

"""
***总之，pandas不允许先筛选子dataframe，再进行修改写入***  
要么使用.loc实现一个步骤直接修改源dataframe  
要么先复制一个子dataframe再一个步骤执行修改
"""