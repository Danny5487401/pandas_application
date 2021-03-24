## Pandas数据排序
"""
Series的排序：
***Series.sort_values(ascending=True, inplace=False)***
参数说明：
* ascending：默认为True升序排序，为False降序排序
* inplace：是否修改原始Series

DataFrame的排序：
***DataFrame.sort_values(by, ascending=True, inplace=False)***
参数说明：
* by：字符串或者List<字符串>，单列排序或者多列排序
* ascending：bool或者List<bool>，升序还是降序，如果是list对应by的多列
* inplace：是否修改原始DataFrame

"""

import pandas as pd

### 0、读取数据
fpath = "../datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
### 1、Series的排序
# print(df["aqi"].sort_values())
# print(df["tianqi"].sort_values(ascending=False))


### 2、DataFrame的排序

#### 2.1 单列排序
# print(df.sort_values(by="aqi"))

#### 2.2 多列排序
# 两个字段都是降序
# print(df.sort_values(by=["aqiLevel", "bWendu"], ascending=False))
# 分别指定升序和降序
print(df.sort_values(by=["aqiLevel", "bWendu"], ascending=[True, False]))