## Pandas对缺失值的处理
"""
Pandas使用这些函数处理缺失值：
* isnull和notnull：检测是否是空值，可用于df和series
* dropna：丢弃、删除缺失值
  - axis : 删除行还是列，{0 or ‘index’, 1 or ‘columns’}, default 0
  - how : 如果等于any则任何值为空都删除，如果等于all则所有值都为空才删除
  - inplace : 如果为True则修改当前df，否则返回新的df
* fillna：填充空值
  - value：用于填充的值，可以是单个值，或者字典（key是列名，value是值）
  - method : 等于ffill使用前一个不为空的值填充forword fill；等于bfill使用后一个不为空的值填充backword fill
  - axis : 按行还是列填充，{0 or ‘index’, 1 or ‘columns’}
  - inplace : 如果为True则修改当前df，否则返回新的df

"""
import pandas as pd
### 实例：特殊Excel的读取、清洗、处理

#### 步骤1：读取excel的时候，忽略前几个空行



studf = pd.read_excel("../datas/student_excel/student_excel.xlsx", skiprows=2)
# print(studf.head())

#### 步骤2：检测空值
# print(studf.isnull())
#
# print(studf["分数"].isnull())

# 筛选没有空分数的所有行
print(studf.loc[studf["分数"].notnull(), :])

#### 步骤3：删除掉全是空值的列

studf.dropna(axis="columns", how='all', inplace=True)
print(studf)
#### 步骤4：删除掉全是空值的行
studf.dropna(axis="index", how='all', inplace=True)
print(studf)

### 步骤5：将分数列为空的填充为0分
studf = studf.fillna({"分数":0})

# 等同于
# studf.loc[:, '分数'] = studf['分数'].fillna(0)
print(studf)

### 步骤6：将姓名的缺失值填充
# 使用前面的有效值填充，用ffill：forward fill
studf.loc[:, '姓名'] = studf['姓名'].fillna(method="ffill")
print(studf)

### 步骤7：将清洗好的excel保存
studf.to_excel("../datas/student_excel/student_excel_clean.xlsx", index=False)