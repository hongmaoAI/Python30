# 创建一个名为 dog 的空字典
dog = {}
# 向 dog 字典添加 name、color、breed、legs、age 键
dog = {'name': '', 'color': '', 'breed': '', 'legs': '', 'age': ''}
# 创建一个学生字典，添加 first_name、last_name、gender、age、marital status、skills、country、city 和 address 作为字典的键
student = {
	'first_name': '',
	'last_name': '',
	'gender': '',
	'age': 18,
	'marital_status': '',
	'skills': ['Python'],
	'country': '',
	'city': '',
	'address': ''
}
# 获取学生字典的长度
print(len(student))  # 7
# 获取 skills 的值并检查数据类型，应该是列表
skills_value = student['skills']
print(skills_value)  # Python
print(type(skills_value))  # <class 'list'>
# 修改 skills 值，添加一到两个技能
new_elements = ['Java', 'HTML']
skills_value.extend(new_elements)
print(skills_value)
# 获取字典的键列表
print(student.keys())
# 获取字典的值列表
print(student.values())
# 使用 items() 方法将字典变为由元组组成的列表
print(student.items())
# 删除字典中的一项
student.pop('address')
print(student)
# 删除其中一个字典
del student
