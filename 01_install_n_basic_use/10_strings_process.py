
## Pandas字符串处理
"""
前面我们已经使用了字符串的处理函数：
df["bWendu"].str.replace("℃", "").astype('int32')

***Pandas的字符串处理：***
1. 使用方法：先获取Series的str属性，然后在属性上调用函数；
2. 只能在字符串列上使用，不能数字列上使用；
3. Dataframe上没有str属性和处理方法
4. Series.str并不是Python原生字符串，而是自己的一套方法，不过大部分和原生str很相似；

***Series.str字符串方法列表参考文档:***
https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling

"""

"""
***本节演示内容：***  
1. 获取Series的str属性，然后使用各种字符串处理函数
2. 使用str的startswith、contains等bool类Series可以做条件查询
3. 需要多次str处理的链式操作
4. 使用正则表达式的处理
"""
import pandas as pd

### 0、读取北京2018年天气数据

fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# print(df.dtypes)
"""
ymd          object
bWendu       object
yWendu       object
tianqi       object
fengxiang    object
fengli       object
aqi           int64
aqiInfo      object
aqiLevel      int64
dtype: object
"""


### 1、获取Series的str属性，使用各种字符串处理函数
# print(df["bWendu"].str) # <pandas.core.strings.accessor.StringMethods object at 0x000001FF9159F588>
# # 字符串替换函数
# print(df["bWendu"].str.replace("℃", ""))
# # 判断是不是数字
# print(df["bWendu"].str.isnumeric())


### 2、使用str的startswith、contains等得到bool的Series可以做条件查询

# condition = df["ymd"].str.startswith("2018-03")
# print(df[condition].head())

### 3、需要多次str处理的链式操作
"""
怎样提取201803这样的数字月份？  
1、先将日期2018-03-31替换成20180331的形式  
2、提取月份字符串201803
"""

# df["ymd"].str.replace("-", "")

print(df["ymd"].str.replace("-", "").str.slice(0,6))
# slice就是切片语法，可以直接用
# print(df["ymd"].str.replace("-", "").str[0:6])

### 4. 使用正则表达式的处理

# 添加新列
def get_nianyueri(x):
    year,month,day = x["ymd"].split("-")
    return f"{year}年{month}月{day}日"
df["中文日期"] = df.apply(get_nianyueri, axis=1)
print(df["中文日期"])
"""问题：怎样将“2018年12月31日”中的年、月、日三个中文字符去除？"""

# 方法1：链式replace
df["中文日期"].str.replace("年", "").str.replace("月","").str.replace("日", "")

# ***Series.str默认就开启了正则表达式模式***
# 方法2：正则表达式替换
# df["中文日期"] =df["中文日期"].str.replace("[年月日]", "")
# print(df["中文日期"])