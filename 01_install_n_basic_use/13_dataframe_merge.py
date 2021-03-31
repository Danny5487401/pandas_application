## Pandas怎样实现DataFrame的Merge

# Pandas的Merge，相当于Sql的Join，将不同的表按key关联到一个表

"""
Pandas的Merge，相当于Sql的Join，将不同的表按key关联到一个表

### merge的语法：
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
* left，right：要merge的dataframe或者有name的Series
* how：join类型，'left', 'right', 'outer', 'inner'
* on：join的key，left和right都需要有这个key
* left_on：left的df或者series的key
* right_on：right的df或者seires的key
* left_index，right_index：使用index而不是普通的column做join
* suffixes：两个元素的后缀，如果列有重名，自动添加后缀，默认是('_x', '_y')

文档地址：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

本次讲解提纲：
1. 电影数据集的join实例
2. 理解merge时一对一、一对多、多对多的数量对齐关系
3. 理解left join、right join、inner join、outer join的区别
4. 如果出现非Key的字段重名怎么办

"""

### 1、电影数据集的join实例
#### 电影评分数据集
"""
是推荐系统研究的很好的数据集  
位于本代码目录：../datas/movielens-1m

包含三个文件：  
1. 用户对电影的评分数据 ratings.dat
2. 用户本身的信息数据 users.dat
3. 电影本身的数据 movies.dat

可以关联三个表，得到一个完整的大表

数据集官方地址：https://grouplens.org/datasets/movielens/
"""

import pandas as pd
df_ratings = pd.read_csv(
    "../datas/movielens-1m/ratings.dat",
    sep="::",
    engine='python',
    names="UserID::MovieID::Rating::Timestamp".split("::")
)

df_users = pd.read_csv(
    "../datas/movielens-1m/users.dat",
    sep="::",
    engine='python',
    names="UserID::Gender::Age::Occupation::Zip-code".split("::")
)

df_movies = pd.read_csv(
    "../datas/movielens-1m/movies.dat",
    sep="::",
    engine='python',
    names="MovieID::Title::Genres".split("::")
)

# 合并
df_ratings_users = pd.merge(
   df_ratings, df_users, left_on="UserID", right_on="UserID", how="inner"
)
# print(df_ratings_users.head())

df_ratings_users_movies = pd.merge(
    df_ratings_users, df_movies, left_on="MovieID", right_on="MovieID", how="inner"
)
# print(df_ratings_users_movies.head(10))


### 2、理解merge时数量的对齐关系
"""
以下关系要正确理解：
* one-to-one：一对一关系，关联的key都是唯一的
  - 比如(学号，姓名) merge (学号，年龄)
  - 结果条数为：1*1
* one-to-many：一对多关系，左边唯一key，右边不唯一key
  - 比如(学号，姓名) merge (学号，[语文成绩、数学成绩、英语成绩])
  - 结果条数为：1*N
* many-to-many：多对多关系，左边右边都不是唯一的
  - 比如（学号，[语文成绩、数学成绩、英语成绩]） merge (学号，[篮球、足球、乒乓球])
  - 结果条数为：M*N
  

"""

#### 2.1 one-to-one 一对一关系的merge
#<img src="../photos/pandas-merge-one-to-one.png" />

left = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'name': ['name_a', 'name_b', 'name_c', 'name_d']
                    })

right = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'age': ['21', '22', '23', '24']
                    })

# 一对一关系，结果中有4条
print(pd.merge(left, right, on='sno'))

#### 2.2 one-to-many 一对多关系的merge

# <img src="../photos/pandas-merge-one-to-many.png" />

left = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'name': ['name_a', 'name_b', 'name_c', 'name_d']
                    })

right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                       'grade': ['语文88', '数学90', '英语75','语文66', '数学55', '英语29']
                     })
# 数目以多的一边为准
print(pd.merge(left, right, on='sno'))


#### 2.3 many-to-many 多对多关系的merge
# <img src="../photos/pandas-merge-many-to-many.png" />
left = pd.DataFrame({'sno': [11, 11, 12, 12,12],
                      '爱好': ['篮球', '羽毛球', '乒乓球', '篮球', "足球"]
                    })

right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                       'grade': ['语文88', '数学90', '英语75','语文66', '数学55', '英语29']
                     })

print(pd.merge(left, right, on='sno'))

### 3、理解left join、right join、inner join、outer join的区别
# <img src="../photos/pandas-leftjoin-rightjoin-outerjoin.png" />

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'C': ['C0', 'C1', 'C4', 'C5'],
                      'D': ['D0', 'D1', 'D4', 'D5']})

#### 3.1 inner join，默认
# 左边和右边的key都有，才会出现在结果里

print(pd.merge(left, right, how='inner'))

#### 3.2 left join
# 左边的都会出现在结果里，右边的如果无法匹配则为Null
print(pd.merge(left, right, how='left'))

#### 3.3 right join
# 右边的都会出现在结果里，左边的如果无法匹配则为Null
print(pd.merge(left, right, how='right'))
#### 3.4 outer join
# 左边、右边的都会出现在结果里，如果无法匹配则为Null
print(pd.merge(left, right, how='outer'))


### 4、如果出现非Key的字段重名怎么办

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'A': ['A10', 'A11', 'A12', 'A13'],
                      'D': ['D0', 'D1', 'D4', 'D5']})

print(pd.merge(left, right, on='key'))  #默认后缀加x,y
print(pd.merge(left, right, on='key', suffixes=('_left', '_right')))