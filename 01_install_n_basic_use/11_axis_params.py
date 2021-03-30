## Pandas的axis参数怎么理解？

"""

* axis=0或者"index"：
  - 如果是单行操作，就指的是某一行
  - 如果是聚合操作，指的是跨行cross rows
* axis=1或者"columns"：
  - 如果是单列操作，就指的是某一列
  - 如果是聚合操作，指的是跨列cross columns

***按哪个axis，就是这个axis要动起来(类似被for遍历)，其它的axis保持不动***

"""

import pandas as pd
import numpy as np


df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A', 'B', 'C', 'D']
)
print(df)

### 1、单列drop，就是删除某一列

# "A"代表的就是删除某列
print(df.drop("A", axis=1))

### 2、单行drop，就是删除某一行

# "1"代表的就是删除某行
print(df.drop(1, axis=0))

### 3、按axis=0/index执行mean聚合操作
# 反直觉：输出的不是每行的结果，而是每列的结果
# axis=0 or axis=index
print(df.mean(axis=0))
"""
***指定了按哪个axis，就是这个axis要动起来(类似被for遍历)，其它的axis保持不动***
"""
# <img src="../photos/pandas-axis-index.png" width="300" />


### 4、按axis=1/columns执行mean聚合操作
print(df.mean(axis=1))
# <img src="../photos/pandas-axis-columns.png" width="300" />


### 5、再次举例，加深理解

def get_sum_value(x):
    return x["A"] + x["B"] + x["C"] + x["D"]

df["sum_value"] = df.apply(get_sum_value, axis=1)
print(df)