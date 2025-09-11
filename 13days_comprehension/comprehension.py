# 列表推导式
# 表推导式是一种从序列中创建列表的简洁方式。它是创建新列表的简短方法。列表推导式比使用 for 循环处理列表快得多
"""
# 语法
[i for i in iterable if 表达式]
"""
# 将字符串转换为字符列表
# 第一种方法
language = 'Python'
lst = list(language)
print(type(lst))  # <class 'list'>
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']
# 第二种方法：列表推导式
lst = [i for i in language]
print(type(lst))  # <class 'list'>
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']
# 生成一个数字列表
# 生成数字
numbers = [i for i in range(11)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 在迭代过程中进行数学运算
squares = [i * i for i in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 可以生成元组列表
numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
# 列表推导式可以与 if 表达式结合使用
# 生成偶数
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# 生成奇数
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 过滤数字：让我们从下面的列表中过滤出正偶数
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# 扁平化二维数组
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Lambda函数 Lambda 函数是没有名字的小匿名函数  可以接受任意数量的参数，但只能有一个表达式
# 创建 Lambda 函数
"""
# 语法
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
"""


# 命名两个常数相加的函数
def add_two_nums(a, b):
	return a + b


print(add_two_nums(2, 3))  # 5

# 将上述函数修改为lambda函数
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # 5

# 自调用lambda函数
print((lambda a, b: a + b)(2, 3))  # 5

squares = lambda x: x ** 2
print(squares(3))  # 9
cube = lambda x: x ** 3
print(cube(3))  # 27

# 多个变量
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22


# 在另一个函数中使用 lambda 函数
def power(x):
	return lambda n: x ** n


cube = power(2)(3)
print(cube)  # 8
