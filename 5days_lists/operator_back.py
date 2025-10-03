# 声明一个空列表
empty_list_one = list()
empty_list_two = []
# 声明一个包含 5 个以上项的列表
list_five = ['banana', 'orange', 'apple', 'lemon', 'mango']
# 查找列表的长度 len()
print(len(list_five))
# 获取列表的第一项、中间项和最后一项
print(list_five[0])
print(list_five[-1])
# 声明一个名为 mixed_data_types 的列表，包含你的姓名、年龄、身高、婚姻状况和地址
mixed_data_types = ['虹猫', '28', '178', 'False', '广州']
print(mixed_data_types)  # ['虹猫', '28', '178', 'False', '广州']
# 声明一个名为 it_companies 的列表，并分配初始值 Facebook、Google、Microsoft、Apple、IBM、Oracle 和 Amazon。
it_companies = ['Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
# 打印列表中的公司数
print(len(it_companies))  # 7
# 打印第一、中间和最后一家公司
print(it_companies[0])
print(it_companies[-1])
print(it_companies[int(len(it_companies) / 2)])
# 修改其中一家公司的名称后打印列表
it_companies[0] = 'Watermelon'
print(it_companies)  # ['Watermelon', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 向 it_companies 添加一家 IT 公司
it_companies.append('ok')
print(it_companies)  # ['Watermelon', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'ok']
# 在公司列表中间插入一家 IT 公司
it_companies.insert(3, 'Apple')
print(it_companies)  # ['Watermelon', 'Google', 'Microsoft', 'apple', 'Apple', 'IBM', 'Oracle', 'Amazon', 'ok']
# 将其中一家 it_companies 公司的名称更改为大写（不包括 IBM!）
print(it_companies[0].upper())  # WATERMELON
# 使用字符串 '#; ' 连接 it_companies
lianjie = '#; '.join(it_companies) + '#; '
print(lianjie)
# 检查 it_companies 列表中是否存在某个公司。
print('apple' in it_companies)  # True
# 使用 sort() 方法对列表进行排序
it_companies.sort()
print(it_companies)  # ['Amazon', 'Apple', 'Google', 'IBM', 'Microsoft', 'Oracle', 'Watermelon', 'ok']
# 使用 reverse() 方法按降序反转列表
it_companies.reverse()
print(it_companies)  # ['ok', 'Watermelon', 'Oracle', 'Microsoft', 'IBM', 'Google', 'Apple', 'Amazon']
# 从列表中切分出前 3 家公司
three_it_companies = it_companies[0:3]
print(three_it_companies)  # ['ok', 'Watermelon', 'Oracle']
# 从列表中删除最后一家 IT 公司
del it_companies[-1]
print(it_companies)  # ['ok', 'Watermelon', 'Oracle', 'Microsoft', 'IBM', 'Google', 'Apple']
# 销毁 it_companies 列表
del it_companies
# 连接以下列表：
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
all_end = front_end + back_end
print(all_end)  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
# 在连接的列表中插入 Python 和 SQL 到变量 all_end之后。
all_end.append('Python')
all_end.insert(0, 'SQL')
print(all_end)  # ['SQL', 'HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB', 'Python']
