## Pandas怎样新增数据列？
"""
1. 直接赋值
2. df.apply方法
3. df.assign方法
4. 按条件选择分组分别赋值

"""
import pandas as pd

### 0、读取csv数据到dataframe

fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
print(df.head())

### 1、直接赋值的方法
"""实例：清理温度列，变成数字类型"""

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

# 实例：计算温差
# 注意，df["bWendu"]其实是一个Series，后面的减法返回的是Series
df.loc[:, "wencha"] = df["bWendu"] - df["yWendu"]
print(df.head())


### 2、df.apply方法
"""
Apply a function along an axis of the DataFrame.

Objects passed to the function are Series objects whose index is either the DataFrame’s index (axis=0) or the DataFrame’s columns (axis=1). 

实例：添加一列温度类型：  
1. 如果最高温度大于33度就是高温
2. 低于-10度是低温
3. 否则是常温
"""

def get_wendu_type(df):
    if df["bWendu"] > 33:
        return '高温'
    if df["yWendu"] < -10:
        return '低温'
    return '常温'

# 注意需要设置axis==1，这是series的index是columns
df.loc[:, "wendu_type"] = df.apply(get_wendu_type, axis=1)
print(df.head())
# 查看温度类型的计数
print(df["wendu_type"].value_counts())

### 3、df.assign方法
"""Assign new columns to a DataFrame.

Returns a new object with all original columns in addition to new ones. """

# 实例：将温度从摄氏度变成华氏度

# 可以同时添加多个新的列
df = df.assign(
    yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,
    # 摄氏度转华氏度
    bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
)
print(df.head())

### 4、按条件选择分组分别赋值
"""按条件先选择数据，然后对这部分数据赋值新列  
实例：高低温差大于10度，则认为温差大"""

# 先创建空列（这是第一种创建新列的方法）
df['wencha_type'] = ''

df.loc[df["bWendu"]-df["yWendu"]>10, "wencha_type"] = "温差大"

df.loc[df["bWendu"]-df["yWendu"]<=10, "wencha_type"] = "温差正常"
print(df.head())