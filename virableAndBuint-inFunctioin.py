# 内置函数len() 主要用于获取对象的长度或元素的数量
print(len('hello world'))
print(len([1, 2, 3, 4, 5]))
print(len({1, '2', 3}))
# 内置函数str() 主要用于将非字符串类型的对象转化为字符串形式。 如整数、浮点数、列表、元组
print(type(str(10)))  # 数字10 已经变成字符串类型
print(type(str([1, 2, 3, 4])))
# 内置函数init() 用于将字符串或数字转换为整数类型 内资函数int()里如果没有值，则会返回0
print(int('123'))  # 123
print(int(456.123))  # 456
print(int())  # 0
# 内置函数float() 用于将整数，字符串或其他数值类型转换为浮点数
print(float(123))
print(float('678'))
print(type(float('678')))
# 内置函数input() 是一个用于接受用户输入的内置函数。当程序执行到input()函数时，会暂停运行并等待用户从键盘输入数据，输入完成后继续执行后续代码。
# 输入的结果类型最终都会是字符串类型
jian_ru = input('请输入你的名字：')
"""
# 变量 变量指的是存储数据的内存地址
命名变量时，不允许以数字开头、使用特殊字符和连字符。变量可以有一个简短的名称(如x、y、z)，但强烈建议使用更具描述性的名称(名字、姓氏、年龄、国家/地区)
Python 变量名规则
• 变量名必须以字母或下划线字符开头
• 变量名不能以数字开头
• 变量名只能包含字母数字字符和下划线(A-z、0-9、_)
• 变量名区分大小写(firstname、Firstname、FirstName、FIRSTNAME是不同的变量)
"""
first_name = 'hong'
last_name = 'mao'
age = 20
skills = ['Python', 'C++', 'Java']
person_info = {
    'first_name': first_name,
    'last_name': last_name,
    'age': age,
    'jian_ru': jian_ru,
}
print(person_info)
