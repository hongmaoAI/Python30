# Pandas添加了设计用于处理表格数据的数据结构和工具
"""
Pandas提供了用于数据操作的工具：
* 重塑
* 合并
* 排序
* 切片
* 聚合
* 插补
"""
import pandas as pd
import numpy as np

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)
'''
# 输出
0    1
1    2
2    3
3    4
4    5
dtype: int64
'''

# 使用自定义索引创建Pandas系列
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)
'''
1    1
2    2
3    3
4    4
5    5
dtype: int64
'''

fruits = ['Orange', 'Banana', 'Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
'''
1    Orange
2    Banana
3     Mango
dtype: object
'''

# 从字典创建Pandas系列
dct = {
	'name': 'hong mao',
	'country': 'China',
	'city': 'shenzhen'
}
s = pd.Series(dct)
print(s)
'''
name       hong mao
country       China
city       shenzhen
dtype: object
'''

# 创建常量Pandas系列
s = pd.Series(10, index=[1, 2, 3])
print(s)
'''
1    10
2    10
3    10
dtype: int64
'''

# 使用Linspace创建Pandas系列   linspace(起始点, 终点, 项目数)
s = pd.Series(np.linspace(5, 20, 10))
print(s)

# 数据框
'''
Pandas数据框可以以不同的方式创建：
* 从列表的列表创建
* 从字典创建
* 从字典的列表创建
* 从CSV文件创建
'''
# 从列表的列表创建数据框
data = [
	['hong mao', 'china', 'shenzhen'],
	['David', 'UK', 'London'],
	['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Name', 'Country', 'City'])
print(df)
'''
       Name Country       City
0  hong mao   china   shenzhen
1     David      UK     London
2      John  Sweden  Stockholm
'''

# 使用字典创建数据框
data = {'Name': ['hong mao', 'china', 'shenzhen'], 'Country': [
	'Finland', 'UK', 'Sweden'], 'City': ['Helsinki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
'''
       Name  Country       City
0  hong mao  Finland   Helsinki
1     china       UK     London
2  shenzhen   Sweden  Stockholm
'''

# 从字典列表创建数据框
data = [{'Name': 'hong mao', 'Country': 'china', 'City': 'shenzhen'},
        {'Name': 'David', 'Country': 'UK', 'City': 'London'},
        {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
'''
       Name Country       City
0  hong mao   china   shenzhen
1     David      UK     London
2      John  Sweden  Stockholm
'''

# 使用Pandas读取CSV文件
'''
让我们在数据目录中读取文件，将通过将文件路径作为参数传递给pd.read_csv()函数来读取weight-height.csv文件。
让我们使用head()方法查看前五行
'''
df = pd.read_csv('../19days_file_handling_cn/bi.csv')
# 查询前5行用 head()
print(df.head())
# 查询后5行用 tail()
print(df.tail())

# 数据探索
# 让我们使用shape属性获取行和列的数量
print('df.shape', df.shape)  # df.shape (1, 4)
# 列名
print(df.columns)  # Index(['name', 'country', 'city', 'skills'], dtype='object')
# 前10行
print(df.head(10))  # 前10行
# 最后10行
print(df.tail(10))  # 最后10行
# 计算每个值有多少个
print(df['name'].value_counts())
# 数据统计概要
print(df.describe())

# 修改数据框
# 创建数据框 首先，让我们使用前面学到的内容创建一个数据框：
data = [
	{"Name": "张三", "Country": "中国", "City": "上海"},
	{"Name": "李四", "Country": "中国", "City": "北京"},
	{"Name": "硬人", "Country": "中国", "City": "广州"}
]
# 创建一个数据框
df = pd.DataFrame(data)
print(df)

# 向DataFrame添加一个权重列：
weights = [74, 78, 69]
df['weight'] = weights
# 向DataFrame添加一个高度列：
heights = [173, 175, 169]
df['Height'] = heights
print(df)

# 修改列值
# 我们可以通过三种方式修改列：

# 1.直接在列名中写入新数据：
df['Name'] = ['赵六', '钱七', '孙八']
print(df)

# 通过索引进行修改：
df.loc[1, 'Name'] = '小七'
print(df)

# 通过iloc索引：
print('原始数据：\n', df)
df.iloc[1, 0] = '阿七'
print('修改后的数据：\n', df)
'''
原始数据：
   Name Country City  weight  Height
0   赵六      中国   上海      74     173
1   小七      中国   北京      78     175
2   孙八      中国   广州      69     169
修改后的数据：
   Name Country City  weight  Height
0   赵六      中国   上海      74     173
1   阿七      中国   北京      78     175
2   孙八      中国   广州      69     169
'''

# 格式化数据框列
# 让我们使用格式进行修改。强大公式是BMI：体重（kg）/ 身高²（m）
# 让我们添加一个BMI列
df["BMI"] = np.round(df['weight'] / ((df['Height'] * 0.01) ** 2), 2)
print(df)

# 检查列值的数据类型
# 我们可以使用dtypes属性检查DataFrame中列的数据类型：
print(df.dtypes)

# 布尔索引 布尔索引或布尔掩码允许您使用条件选择DataFrame中的特定行：
# 创建一个数据框
df = pd.DataFrame({
	'name': ['张三', '李四', '硬人', '赵六'],
	'country': ['中国', '美国', '英国', '西班牙'],
	'age': [25, 15, 22, 28],
	'在职': [True, False, True, False]
})
print(df)
'''
  name country  age     在职
0   张三      中国   25   True
1   李四      美国   15  False
2   王五      英国   22   True
3   赵六     西班牙   28  False
'''
# 让我们筛选出年龄大于20岁且在职的人员：
print(df[(df['age'] > 20) & (df['在职'] == True)])
