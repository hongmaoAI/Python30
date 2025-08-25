"""
练习： 1级
"""

# 第二天： 30 Days of python programming

# 声明一个 first name 变量，并为它赋值
first_name = 'hong'
# 声明一个 last name 变量，并为它赋值
last_name = 'mao'
# 声明一个 full name 变量，并为它赋值
full_name = 'hong mao'
# 声明一个 country 变量，并为它赋值
country = 'China'
# 声明一个 city 变量，并为它赋值
city = 'guangzhou'
# 声明一个 age 变量，并为它赋值
age = 28
# 声明一个 year 变量，并为它赋值
year = 2025
# 声明一个 is_married 变量，并为它赋值
is_married = False
# 在一行中声明多个变量
a, b, c = 1, 2, 3
"""
练习： 2级

使用内置输入函数从用户那里获取名字、姓氏、国家和年龄，并将值存储到相应的变量名中
在 Python shell 或文件中运行 help('keywords') 检查 Python 保留字或关键字
"""
# 使用 type() 内置函数检查你声明变量的数据类型
print(type(first_name))  # str
print(type(last_name))  # str
print(type(full_name))  # str
print(type(country))  # str
print(type(city))  # str
print(type(age))  # int
# 使用 len() 内置函数，算出你 first name 变量的长度
print(len(first_name))  # 4
# 比较你 first name 和 last name 变量的长度
d = len(first_name)
e = len(last_name)
print(max(d, e))
# 声明变量 num_one 为5，num_two 为4
num_one = 5
num_two = 4
# 将 num_one 和 num_two 相加，并赋值给 total 变量
total = num_one + num_two
# 将 num_one 和 num_two 相减，并赋值给 diff 变量
diff = num_one - num_two
# 将 num_one 和 num_two 相乘，并赋值给 product 变量
product = num_one * num_two
# 将 num_one 和 num_two 相除，并赋值给 division 变量
division = num_one / num_two
# 使用模数除法求出 num_two 除以 num_one 的结果，并将结果赋给变量 remainder
remainder = num_one % num_two
# 计算 num_one 的 num_two 次方并将值赋给变量 exp
exp = num_one ** num_two
# 计算 num_one 除以 num_two 商的整数部分（整除操作），并将结果赋给变量 floor_division
floor_division = int(num_one / num_two)
# 输出
print('total', total)
print('diff', diff)
print('product', product)
print('division', division)
print('remainder', remainder)
print('exp', exp)
print('floor_division', floor_division)

"""
圆的半径为 30 米。
计算圆的面积并将值赋给名为 area_of_circle 的变量
计算圆的周长并将值赋给名为 circum_of_circle 的变量
将半径作为用户输入并计算面积。
"""
round_r = 30
area_of_circle = 3.14 * round_r ** 2
circum_of_circle = 3.14 * round_r * 2
input_round_r = int(input('输入圆的半径：'))
round_area = input_round_r ** 2 * 3.14
print('area_of_circle', area_of_circle)
print('circum_of_circle', circum_of_circle)
print('input_round_r', input_round_r)
print('round_area', round_area)
