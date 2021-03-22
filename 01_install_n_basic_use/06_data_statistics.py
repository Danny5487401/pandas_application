
## Pandas数据统计函数
"""
1. 汇总类统计
2. 唯一去重和按值计数
3. 相关系数和协方差

"""

import pandas as pd

### 0、读取csv数据

fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

### 1、汇总类统计
# 一下子提取所有数字列统计结果
print(df.describe())

## 查看单个Series的数据
print(df["bWendu"].mean())

### 2、唯一去重和按值计数
#### 2.1 唯一性去重
"""
一般不用于数值列，而是枚举、分类列
"""
print(df["fengxiang"].unique())

#### 2.2 按值计数
print(df["fengxiang"].value_counts())

### 3、相关系数和协方差
"""

用途（超级厉害）：
1. 两只股票，是不是同涨同跌？程度多大？正相关还是负相关？
2. 产品销量的波动，跟哪些因素正相关、负相关，程度有多大？

来自知乎，对于两个变量X、Y：
1. 协方差：***衡量同向反向程度***，如果协方差为正，说明X，Y同向变化，协方差越大说明同向程度越高；如果协方差为负，说明X，Y反向运动，协方差越小说明反向程度越高。
2. 相关系数：***衡量相似度程度***，当他们的相关系数为1时，说明两个变量变化时的正向相似度最大，当相关系数为－1时，说明两个变量变化的反向相似度最大
"""
# 协方差矩阵：
print(df.cov())
# 相关系数矩阵
print(df.corr())
# 单独查看空气质量和最高温度的相关系数
print(df["aqi"].corr(df["bWendu"]))
# 空气质量和温差的相关系数
print(df["aqi"].corr(df["bWendu"]-df["yWendu"]))