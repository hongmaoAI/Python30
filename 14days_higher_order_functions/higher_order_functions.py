# 高阶函数
"""
一个函数可以接收一个或多个函数作为参数
一个函数可以作为另一个函数的返回值
一个函数可以被修改
一个函数可以被赋值给变量
"""
from functools import reduce


# 函数作为参数
def sum_numbers(nums):
	return sum(nums)


def higher_order_function(f, lst):
	summation = f(lst)
	return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)


# 函数作为返回值
def square(x):  # 求平方函数
	return x ** 2


def cube(x):  # 求立方函数
	return x ** 3


# 定义一个绝对值函数
def absolute(x):
	if x >= 0:
		return x
	else:
		return -x


def higher_order_function(type_name):
	if type_name == 'square':
		return square
	elif type_name == 'cube':
		return cube
	elif type_name == 'absolute':
		return absolute
	return None


result = higher_order_function('square')
print(result(3))  # 9
result = higher_order_function('cube')
print(result(3))  # 27
result = higher_order_function('absolute')
print(result(-3))  # 3


# 高阶函数根据传入的参数来返回不同的函数
# Python闭包
# Python 允许嵌套函数访问外部封闭函数的作用域
# 闭包是通过在另一个封装函数内部嵌套函数，然后返回内部函数
def add_ten():
	ten = 10

	def add(num):
		return num + ten

	return add


closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))


# python装饰器
# 装饰器是一种设计模式 允许用户在不修改对象结构的情况下为其添加新功能
# 装饰器通常在你想要装饰的函数定义之前调用
# 创建装饰器

# 普通函数
def greeting():
	return 'Welcome to Python!'


def uppercase_decorator(function):
	def wrapper():
		func = function()
		make_uppercase = func.upper()
		return make_uppercase

	return wrapper


g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON!


# 将上述普通函数用装饰器实现下
def uppercase_decorator(function):
	def wrapper():
		func = function()
		make_uppercase = func.upper()
		return make_uppercase

	return wrapper


@uppercase_decorator
def greeting():
	return 'Hong Mao'


print(greeting())  # HONG MAO


# 将多个装饰器应用于单个函数 这些装饰器都是高阶函数，接受函数作为参数

# 第一个装饰器
def uppercase_decorator(function):
	def wrapper():
		func = function()
		make_uppercase = func.upper()
		return make_uppercase

	return wrapper


# 第二个装饰器
def split_string_decorator(function):
	def wrapper():
		func = function()
		splitted_string = func.split()
		return splitted_string

	return wrapper


@split_string_decorator
@uppercase_decorator
def greeting():
	return 'Welcome to Python!'


print(greeting())


# 在装饰器函数中接受参数
# 大多数时候我们需要我们的函数接受参数 所以需要定义一个接受参数的装饰器
def decorator_with_parameters(function):
	def wrapper_accepting_parameters(para1, para2, para3):
		function(para1, para2, para3)
		print('I live in {}'.format(para3))

	return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
	print('I am {} {}. I love to teach.'.format(first_name, last_name, country))


print_full_name('Hong', 'Mao', 'US')

# 内置高阶函数 map、filter、reduce
# Lambda 函数可以作为参数传递，其最佳使用案例是在地图、过滤和减少等功能中
# Map函数
# map()函数是一个内置函数，接收一个函数和可迭代对象作为参数
"""
# 语法
map(function,iterable)
"""
numbers = [1, 2, 3, 4, 5]


def square(x):
	return x ** 2


# eg1
numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
# 运用lambda函数
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# eg2
numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # [1, 2, 3, 4, 5]

# eg3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']


def change_to_upper(name):
	return name.upper()


names_upper = map(change_to_upper, names)
print(list(names_upper))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# 将上述函数用lambda修改
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Filter 函数
# 调用指定函数，该函数对指定的可迭代对象（列表）中的每个项目返回布尔值。它过滤出满足过滤条件的项目
"""
# 语法
filter(function,iterable)
"""

# eg1
# 定义一个只过滤偶数的函数
numbers = [1, 2, 3, 4, 5]


def is_even(num):
	if num % 2 == 0:
		return True
	return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]

# eg2
numbers = [1, 2, 3, 4, 5]


def is_odd(num):
	if num % 2 != 0:
		return True
	return False


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5]

# 定义一个函数，功能过滤特定字符串的长度
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']


def is_name_long(name):
	if len(name) > 7:
		return True
	return False


long_names = filter(is_name_long, names)
print(list(long_names))  # ['Asabeneh']

# Reduce 函数  它接收两个参数，一个函数和一个可迭代对象 返回一个单一的值
numbers_str = ['1', '2', '3', '4', '5']


def add_two_nums(x, y):
	return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)  # 15
