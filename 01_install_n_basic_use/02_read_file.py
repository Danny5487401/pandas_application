
"""
本代码演示：
1. pandas读取纯文本文件
  * 读取csv文件
  * 读取txt文件
2. pandas读取xlsx格式excel文件
3. pandas读取mysql数据表
"""
import pandas as pd

## 1、读取纯文本文件
### 1.1 读取CSV，使用默认的标题行、逗号分隔符
fpath = "../datas/ml-latest-small/ratings.csv"

# 使用pd.read_csv读取数据
ratings = pd.read_csv(fpath)

# 查看前几行数据
print(ratings.head())
# 查看数据的形状，返回(行数、列数)
print(ratings.shape)

# 查看列名列表
print(ratings.columns) # Index(['userId', 'movieId', 'rating', 'timestamp'], dtype='object')

# 查看索引列
print(ratings.index) # RangeIndex(start=0, stop=100836, step=1)

# 查看每列的数据类型
print(ratings.dtypes)

### 1.2 读取txt文件，自己指定分隔符、列名
fpath = "../datas/crazyant/access_pvuv.txt"

pvuv = pd.read_csv(
    fpath,
    sep="\t",
    header=None,
    names=['pdate', 'pv', 'uv']  # 指定列名
)
print(pvuv)

## 2、读取excel文件
# In xlrd >= 2.0, only the xls format is supported. Install openpyxl instead
fpath = "../datas/crazyant/access_pvuv.xlsx"
pvuv = pd.read_excel(fpath)
print(pvuv)

## 3、读取MySQL数据库
# import pymysql
# conn = pymysql.connect(
#         host='127.0.0.1',
#         user='root',
#         password='12345678',
#         database='test',
#         charset='utf8'
#     )
# mysql_page = pd.read_sql("select * from crazyant_pvuv", con=conn)