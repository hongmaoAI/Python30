# 字典 字典是一种由无序、可修改（可变）的键值对组成的数据类型。
# 创建字典 为了创建字典，我们使用大括号 {} 或内置函数 dict()。
empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct)
# 字典的值可以是任何数据类型：字符串、布尔值、列表、元组、集合或字典。
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
print(person)
# 字典长度 len()方法检查字典中的键值对的数量
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(len(dct))  # 4
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
print(len(person))  # 7
# 访问字典项 通过参考其键名来访问字典项
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct['key1'])  # value1
print(dct['key2'])  # value2
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
print(person['first_name'])  # Asabeneh
print(person['country'])  # Finland
print(person['skills'])  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
# print(person['city'])  # KeyError: 'city'
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
print(person.get('first_name'))  # Asabeneh
print(person.get('country'))  # Finland
print(person.get('skills'))  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))  # None
# 向字典添加项 可以向字典中添加新的键值对
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct['key4'])  # value4
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
# 修改字典中的项目 可以修改字典中的项目
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key1'] = 'value-one'
print(dct)
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_married': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
person['first_name'] = 'Eyob'
person['age'] = 252
print(person)
# 检查字典中的键 使用 in 运算符来检查字典中是否存在某个键
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key2' in dct)  # True
print('key5' in dct)  # False
# 从字典中删除键值对
"""
* pop(key): 删除具有指定键名的项目
* popitem(): 删除最后一个项目
* del: 删除具有指定键名的项目
"""
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop('key2')  # 删除‘key2’:'value2'
print(dct)  # {'key1': 'value1', 'key3': 'value3', 'key4': 'value4'}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()  # 删除最后一项
print(dct)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
del dct['key2']  # 删除key2的键值对
print(dct)  # {'key1': 'value1', 'key3': 'value3'}
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_married': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
person.pop('first_name')
print(person)  # 删除firstname键值对
person.popitem()  # 删除最后一项
print(person)
del person['is_married']
print(person)  # 删除is_married键值对
# 将字典改变为项目列表 items() 方法将字典变成由元组组成的列表。
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
# 清空字典 如果我们不需要字典中的项目，我们可以使用 _clear()_ 方法来清空它们
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.clear())  # None
# 删除字典 如果我们不再使用字典，我们可以完全删除它
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct
# 复制字典
# 使用 copy() 方法复制一个字典。使用 copy 方法可以避免原始字典被修改。
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()
print(dct_copy)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
# 获取字典的键列表 keys() 方法给我们一个包含所有字典键的列表。
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct.keys()
print(keys)  # dict_keys(['key1', 'key2', 'key3', 'key4'])
# 获取字典的值列表 values 方法给我们一个包含所有字典值的列表。
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
values = dct.values()
print(values) #dict_values(['value1', 'value2', 'value3', 'value4'])
