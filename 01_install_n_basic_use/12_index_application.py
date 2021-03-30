## Pandas的索引index的用途

"""
把数据存储于普通的column列也能用于数据查询，那使用index有什么好处？

index的用途总结：
1. 更方便的数据查询；
2. 使用index可以获得性能提升；
3. 自动的数据对齐功能；
4. 更多更强大的数据结构支持；


"""


import pandas as pd
import timeit

df = pd.read_csv("../datas/ml-latest-small/ratings.csv")
# print(df.head())
# print(df.count())


## 1、使用index查询数据
# drop==False，让索引列还保持在column
df.set_index("userId", inplace=True, drop=False)
# print(df.head())
# 使用index的查询方法
# print(df.loc[500].head(5))
# 使用column的condition查询方法
df.loc[df["userId"] == 500].head()


## 2. 使用index会提升查询性能

"""
* 如果index是唯一的，Pandas会使用哈希表优化，查询性能为O(1);
* 如果index不是唯一的，但是有序，Pandas会使用二分查找算法，查询性能为O(logN);
* 如果index是完全随机的，那么每次查询都要扫描全表，查询性能为O(N);
"""

# <img src="../photos/pandas-index-performance.png" width=600/>

### 实验1：完全随机的顺序查询

# 将数据随机打散
from sklearn.utils import shuffle

# print(df_shuffle.head())
# 索引是否是递增的
# print(df_shuffle.index.is_monotonic_increasing)
# 索引是否是唯一的
# print(df_shuffle.index.is_unique)

# 计时，查询id==500数据性能

df_shuffle = shuffle(df)
print(timeit.timeit("df_shuffle.loc[500]",setup="from __main__ import df_shuffle",number=10))


### 实验2：将index排序后的查询
df_sorted = df_shuffle.sort_index()
print(timeit.timeit("df_sorted.loc[500]",setup="from __main__ import df_sorted",number=10))

## 3. 使用index能自动对齐数据
# 包括series和dataframe
s1 = pd.Series([1,2,3], index=list("abc"))
s2 = pd.Series([2,3,4], index=list("bcd"))
print(s1+s2)


## 4. 使用index更多更强大的数据结构支持
"""
***很多强大的索引数据结构*** 
* CategoricalIndex，基于分类数据的Index，提升性能；
* MultiIndex，多维索引，用于groupby多维聚合后结果等；
* DatetimeIndex，时间类型索引，强大的日期和时间的方法支持；
"""