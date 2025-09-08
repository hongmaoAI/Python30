# 定义函数
# 声明和调用函数
# 创建一个函数时，我们称其为声明一个函数 函数可以带参数也可以不带参数
"""
# 语法
# 声明一个函数
def function_name():
	codes
	codes
	# 调用一个函数
	function_name()
"""


# 无参数的函数 函数可以在没有参数的情况下声明
def generate_full_name():
	first_name = 'Asabeneh'
	last_name = 'Yetayeh'
	space = ' '
	full_name = first_name + space + last_name
	print(full_name)


generate_full_name()  # 调用一个函数 输出 Asabeneh Yetayeh


def add_two_numbers():
	num_one = 2
	num_two = 3
	total = num_one + num_two
	print(total)


add_two_numbers()  # 调用一个函数 输出 5


# 返回值的函数 函数也可以有返回值 如果一个函数没有 return 语句，那么函数的返回值为 None
def generate_full_name():
	first_name = 'Asabeneh'
	last_name = 'Yetayeh'
	space = ' '
	full_name = first_name + space + last_name
	return full_name


print(generate_full_name())  # Asabeneh Yetayeh


def add_two_numbers():
	num_one = 2
	num_two = 3
	total = num_one + num_two
	return total


print(add_two_numbers())  # 5
# 有参数的函数
# 在一个函数中，我们可以传递不同的数据类型（数字、字符串、布尔值、列表、元组、字典或集合）作为参数
# 单个参数：如果我们的函数需要一个参数，我们应该用一个实参调用它
"""
# 语法
  def function_name(parameter):
    codes
    codes
  # 调用函数
  print(function_name(argument))
"""


# 参数为字符串 输出与另一字符串的语句做拼接
def greetings(name):
	message = name + ', welcome to python for Everyone!'
	return message


print(greetings('Asabeneh'))  # Asabeneh, welcome to python for Everyone!


# 参数与10相加
def add_ten(num):
	ten = 10
	return num + ten


print(add_ten(90))  # 100


# 两个数相乘
def square_number(x):
	return x * x


print(square_number(8))  # 64


# 圆的面积
def area_of_circle(r):
	PI = 3.14
	area = PI * r ** 2
	return area


print(area_of_circle(10))  # 314.0


def sum_of_numbers(n):
	total = 0
	for i in range(n + 1):
		total += i
	print(total)


print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050
# 一个函数可以没有参数，也可以有一个或多个参数
# 两个参数
"""
# 语法
  def function_name(para1, para2):
    codes
    codes
  # 调用函数
  print(function_name(arg1, arg2))
"""


# 定义一个输出名字的函数
def generate_full_name(first_name, last_name):
	space = ' '
	full_name = first_name + space + last_name
	return full_name


print('Full_name:', generate_full_name('Asabeneh', 'Yetayeh'))  # Full_name: Asabeneh Yetayeh


# 定义一个两个数字相加
def sum_two_numbers(num_one, num_two):
	sum = num_one + num_two
	return sum


print('Sum of two numbers:', sum_two_numbers(1, 9))  # Sum of two numbers: 10


# 定义一个可以计算年龄的函数
def calculate_age(current_year, birth_year):
	age = current_year - birth_year
	return age


print('Age', calculate_age(2025, 1997))  # 28


# 定义一个可以输出物体有多重的函数
def weight_of_object(mass, gravity):
	weight = str(mass * gravity) + 'N'
	return weight


print('Weight of an object in Newtons:', weight_of_object(100, 9.81))  # Weight of an object in Newtons: 981.0N
# 使用键值对传递参数 我们使用键值对传递参数，参数的顺序就无关紧要了
"""
# 语法
def function_name(para1, para2):
    codes
    codes
# 调用函数
print(function_name(para1 = 'John', para2 = 'Doe'))
"""


def print_fullname(first_name, last_name):
	space = ' '
	full_name = first_name + space + last_name
	print(full_name)


print(print_fullname(first_name='Asabeneh', last_name='Yetayeh'))  # Asabeneh Yetayeh


def add_two_numbers(num1, num2):
	total = num1 + num2
	print(total)


print(add_two_numbers(num2=3, num1=2))  # 5


# 返回值的函数 -> 返回字符串
def print_name(firstname):
	return firstname


print_name('Asabeneh')


def print_full_name(firstname, lastname):
	space = ' '
	full_name = firstname + space + lastname
	return full_name


print(print_full_name('Asabeneh', 'Yetayeh'))  # Asabeneh Yetayeh


# 返回值的函数 -> 返回数字
def add_two_numbers(num1, num2):
	total = num1 + num2
	return total


print(add_two_numbers(2, 3))  # 5


def calculate_age(current_year, birth_year):
	age = current_year - birth_year
	return age


print('Age', calculate_age(2025, 1997))  # Age 28


# 返回值的函数 -> 返回布尔值
def is_even(n):
	if n % 2 == 0:
		print('even')
		return True
	return False


print(is_even(10))  # even True
print(is_even(7))  # False


# 返回值的函数 -> 返回列表
def find_even_numbers(n):
	evens = []
	for i in range(n + 1):
		if i % 2 == 0:
			evens.append(i)
	return evens


print(find_even_numbers(10))  # [0, 2, 4, 6, 8, 10]
# 带默认参数的函数
# 我们在调用函数时会传递默认值给参数 调用函数时没有传递实参，参数的默认值将会被使用
"""
def function_name(param = value):
    codes
    codes
# 调用函数
function_name()
function_name(arg)
"""


def greetings(name='Peter'):
	message = name + ', welcome to python for Everyone!'
	return message


print(greetings())  # Peter, welcome to python for Everyone!
print(greetings('Asabeneh'))  # Asabeneh, welcome to python for Everyone!


def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
	space = ' '
	full_name = first_name + space + last_name
	return full_name


print(generate_full_name())  # Asabeneh Yetayeh
print(generate_full_name('David', 'Smith'))  # David Smith


def calculate_age(birth_year, current_year=2025):
	age = current_year - birth_year
	return age


print('Age', calculate_age(1997))  # Age 28


def weight_of_object(mass, gravity=9.81):
	weight = str(mass * gravity) + 'N'
	return weight


print('Weight of an object in Newtons:', weight_of_object(100))  # Weight of an object in Newtons: 981.0N
print('Weight of an object in Newtons:', weight_of_object(100, 1.62))  # Weight of an object in Newtons: 162.0N
# 不定数量的参数 当不知道传递给函数的参数数量时，在参数名前加上 * 来创建
"""
# 语法
def function_name(*args):
    codes
    codes
# 调用函数
function_name(param1, param2, param3,..)
"""


def sum_all_nums(*nums):
	total = 0
	for num in nums:
		total += num
	return total


print(sum_all_nums(2, 3, 5))  # 10


# 函数中的默认和不定数量的参数
def generate_groups(team, *args):
	print(team)
	for i in args:
		print(i)


print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))


# 作为另一个函数参数的函数
def square_number(n):
	return n * n


def do_something(f, x):
	return f(x)


print(do_something(square_number, 3))  # 9
