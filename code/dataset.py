import pandas as pd
import numpy as np

# 载入数据
accepted_data = pd.read_csv("../data/acceptedmin_data.csv",encoding='latin-1')
rejected_data = pd.read_csv("../data/rejectedmin_data.csv",encoding='latin-1')


state_to_level = {
    'CA': 'A', 'TX': 'A', 'NY': 'A',
    'FL': 'B', 'IL': 'B', 'PA': 'B', 'OH': 'B', 'NJ': 'B',
    'NC': 'C', 'VA': 'C', 'MI': 'C', 'MA': 'C', 'WA': 'C', 'GA': 'C', 'MN': 'C', 'TN': 'C', 'CO': 'C', 'WI': 'C', 'MO': 'C', 'CT': 'C', 'LA': 'C',
    'AZ': 'D', 'IN': 'D', 'MN': 'D', 'MD': 'D', 'MN': 'D', 'MA': 'D', 'WA': 'D', 'TN': 'D', 'KS': 'D', 'UT': 'D', 'AR': 'D', 'DC': 'D', 'IA': 'D',
    'NV': 'E', 'OK': 'E', 'IA': 'E', 'NM': 'E', 'HI': 'E', 'WV': 'E', 'NH': 'E', 'ID': 'E', 'ME': 'E', 'RI': 'E', 'AK': 'E', 'SD': 'E', 'MT': 'E', 'WY': 'E', 'ND': 'E', 'VT': 'E'
}


# 将州名称替换为对应的级别
accepted_data['State'] = accepted_data['State'].map(state_to_level)
rejected_data['State'] = rejected_data['State'].map(state_to_level)

# 查看数据集的前几行，确保数据被正确加载。
# print(accepted_data.head())
# print(rejected_data.head())

#防止encoding格式报错，先检查
# import chardet
# with open("../data/accepted_data.csv",'rb') as f:
#     result = chardet.detect(f.read())
#     print(result)

print(accepted_data.isnull().sum())
print(rejected_data.isnull().sum())


# 将emp_length为空白的数据修改为unknown
# accepted_data['emp_length'].fillna('unknown',inplace=True)
# print("acc:\n",accepted_data.isnull().sum())
# rejected_data['emp_length'].fillna('unknown',inplace=True)
# print("rej:\n",rejected_data.isnull().sum())

# 删除缺失值
# rejected_data.dropna(inplace=True)
# print("rej:\n",rejected_data.isnull().sum())

# 增加标签
# accepted_data['label'] = 1
# rejected_data['label'] = 0

print(accepted_data.head())
print(rejected_data.head())

# 保存文件
accepted_data.to_csv("../data/accepted_data.csv",index=False)
rejected_data.to_csv("../data/rejected_data.csv",index=False)
