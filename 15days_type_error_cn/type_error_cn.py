# Python类型错误

# SyntaxError(语法错误)
# print 'hello world'
print('hello world')

# NameError(名称错误)
# print(name) # name未定义
name = 'hong mao'
print(name)  # hong mao

# IndexError(索引错误)
nums = [1, 2, 3, 4, 5]
# print(nums[5]) # 索引只到4，没有索引5

# ModuleNotFoundError(模块未找到错误)
# import maths # 错误的引用
# import math # 正确的引用

# AttributeError(属性错误)
import math

# print(math.PI) # math中不存在PI
print(math.pi)

# KeyError (键错误)
users = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
print(users['name'])  # Asab
# print(users['county']) # KeyError: 'county'
print(users['country'])

# TypeError (类型错误)
# print(4 + '3')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(4 + int('3'))  # 7

# ImportError (导入错误)
# from math import power  # ImportError: cannot import name 'power' from 'math' (unknown location)
from math import pow

# ValueError (值错误)
# print(int('12a')) # ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError (零除错误)
print(1 / 0)  # ZeroDivisionError: division by zero
