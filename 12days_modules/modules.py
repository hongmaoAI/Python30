# 将模块一次性导入
import mymodule
# 模块按需导入
from mymodule import generate_full_name, sum_two_numbers, person
# 导入模块，并对模块重命名
from mymodule import generate_full_name as fullname
# 导入内置模块
import os
# 导入sys模块
import sys
# 导入所有模块
from statistics import *
# 导入math
import math
# 重命名内置函数名称
from math import pi as PI
# 字符串模块
import string
# 随机模块
from random import random, randint

# 模块
"""
什么是模块
模块是包含一组代码或一组函数的文件，可以包含在一个应用程序中。
一个模块可以是包含单个变量、函数或大规模代码库的文件.
"""
# 创建模块
# 要创建模块，我们在一个 Python 脚本中编写代码并保存为 .py 文件。
# 在项目12days_modules文件夹中创建一个名为 mymodule.py 的文件。让我们在此文件中编写一些代码。
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))  # Asabeneh Yetayeh
# 从模块中导入函数 我们可以在一个文件中有很多函数，并且我们可以分别导入所有函数
print(generate_full_name('hong', 'mao'))  # hong mao
print(sum_two_numbers(2, 3))  # 5
print(person('hongmao', 27, '男'))  # ('姓名：hongmao', '年龄：age', '性别：男')
# 从模块中导入函数并重命名 在模块的导入中，我们可以重命名
print(fullname('hong', 'mao'))  # hong mao
# 导入内置模块
# 一些常见的内置模块：math、datetime、os、sys、random、statistics、collections、json、re
# OS 模块
# Python 中的 OS 模块提供了创建、更改当前工作目录和删除目录（文件夹）、获取其内容、更改和识别当前目录的函数。
"""
# 导入模块
import os
# 创建目录
os.mkdir('directory_name')
# 更改当前目录
os.chdir('path')
# 获取当前工作目录
os.getcwd()
# 删除目录
os.rmdir()
"""
print(os.getcwd())  # E:\PythonProject\12days_modules
# Sys 模块
"""
sys 模块提供用于操作 Python 运行时环境不同部分的函数和变量。函数 sys.argv 返回
传递给 Python 脚本的命令行参数列表。此列表中索引 0 处的项始终是脚本的名称，
索引 1 处是从命令行传递的参数。
"""
print(sys.argv[0])  # E:\PythonProject\12days_modules\modules.py
# 统计模块 提供用于数值数据的数学统计的函数  统计函数：mean、median、mode、stdev 等。
args = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(args))  # mean计算平均值 21.09090909090909
print(median(args))  # median计算中位数 22
print(mode(args))  # mode计算众数 20
print(stdev(args))  # stdev计算数据集的标准差6.106628291529549
# 数学模块 包含许多数学运算和常数的模块
print(math.pi)  # pi常数 3.141592653589793
print(math.sqrt(2))  # 平方根 1.4142135623730951
print(math.pow(2, 3))  # 指数函数8.0
print(math.floor(9.81))  # 向下取整  9
print(math.ceil(9.81))  # 向上取整 10
print(math.log10(100))  # 以10为底的对数 2.0
# 当我们导入时，我们也可以重命名函数名称
print(PI)  # 3.141592653589793
# 字符串模块
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 随机模块
print(random())  # 随机生成一个0到0.9999数 0.38624724128345
print(randint(5, 20))  # 随机生成一个5到20的整数 11
