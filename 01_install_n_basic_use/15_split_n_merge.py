## Pandas批量拆分Excel与合并Excel
"""

实例演示：
1. 将一个大Excel等份拆成多个Excel
2. 将多个小Excel合并成一个大Excel并标记来源
"""

work_dir="../datas/c15_excel_split_merge"
splits_dir=f"{work_dir}/splits"

import os
if not os.path.exists(splits_dir):
    os.mkdir(splits_dir)

### 0、读取源Excel到Pandas
import pandas as pd
df_source = pd.read_excel(f"{work_dir}/crazyant_blog_articles_source.xlsx")
# 总行数
total_row_count = df_source.shape[0]

### 一、将一个大Excel等份拆成多个Excel
"""
1. 使用df.iloc方法，将一个大的dataframe，拆分成多个小dataframe
2. 将使用dataframe.to_excel保存每个小Excel
"""
#### 1、计算拆分后的每个excel的行数

# 这个大excel，会拆分给这几个人
user_names = ["xiao_shuai", "xiao_wang", "xiao_ming", "xiao_lei", "xiao_bo", "xiao_hong"]

split_size = total_row_count // len(user_names)  # //  是整数
if total_row_count % len(user_names) != 0:
    split_size += 1

#### 2、拆分成多个dataframe

df_subs = []
for idx, user_name in enumerate(user_names):
    # iloc的开始索引
    begin = idx*split_size
    # iloc的结束索引
    end = begin+split_size
    # 实现df按照iloc拆分
    df_sub = df_source.iloc[begin:end]
    # 将每个子df存入列表
    df_subs.append((idx, user_name, df_sub))

#### 3、将每个datafame存入excel


for idx, user_name, df_sub in df_subs:
    file_name = f"{splits_dir}/crazyant_blog_articles_{idx}_{user_name}.xlsx"
    df_sub.to_excel(file_name, index=False)

"""
### 二、合并多个小Excel到一个大Excel

1. 遍历文件夹，得到要合并的Excel文件列表
2. 分别读取到dataframe，给每个df添加一列用于标记来源
3. 使用pd.concat进行df批量合并
4. 将合并后的dataframe输出到excel
"""

#### 1. 遍历文件夹，得到要合并的Excel名称列表

import os
excel_names = []
for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)

#### 2. 分别读取到dataframe

df_list = []

for excel_name in excel_names:
    # 读取每个excel到df
    excel_path = f"{splits_dir}/{excel_name}"
    df_split = pd.read_excel(excel_path)
    # 得到username
    username = excel_name.replace("crazyant_blog_articles_", "").replace(".xlsx", "")[2:]
    print(excel_name, username)
    # 给每个df添加1列，即用户名字
    df_split["username"] = username

    df_list.append(df_split)
#### 3. 使用pd.concat进行合并
df_merged = pd.concat(df_list)

#### 4. 将合并后的dataframe输出到excel
df_merged.to_excel(f"{work_dir}/crazyant_blog_articles_merged.xlsx", index=False)