import math
import numpy as np


# 声明一个函数 add_two_numbers。它接受两个参数并返回它们的和。
def add_two_numbers(a, b):
    return a + b


# 圆的面积计算公式为：area = π x r x r。编写一个函数计算 area_of_circle。
def area_of_circle(r):
    area = math.pi * r * r
    return area


# 编写一个名为 add_all_nums 的函数，它接受不定数量的参数并求和所有参数。检查所有列表项是否都是数字类型。如果不是，给予合理的反馈。
def add_all_nums(*args):
    sums = 0
    for arg in args:
        sums = sums + arg
    return sums


print(add_all_nums(1, 2, 3, 4, 5, 6))


# 摄氏温度（°C）可以使用以下公式转换为华氏温度（°F）：°F = (°C x 9/5) + 32。编写一个函数将 °C 转换为 °F，convert_celsius_to_fahrenheit。
def convert_celsius_to_fahrenheit(C):
    F = (C * 9 / 5) + 32
    return F


print(convert_celsius_to_fahrenheit(27))


# 编写一个名为 check_season 的函数，它接受一个月份作为参数并返回季节：秋季、冬季、春季或夏季。
def check_season(month):
    if 3 <= month <= 5:
        return '春季'
    elif 6 <= month <= 8:
        return '夏季'
    elif 9 <= month <= 11:
        return '秋季'
    else:
        return '冬季'


print(check_season(3))


# 声明一个名为 print_list 的函数。它接受一个列表作为参数，并打印列表的每个元素。
def print_list(args):
    for arg in args:
        print(arg)


print_list([1, 2, 3, 4, 5, 6, 7, 8])


# 声明一个名为 reverse_list 的函数。它接受一个数组作为参数，并返回数组的反转（使用循环）。
def reverse_list(args):
    lists = np.array(args)
    return lists[::-1]


print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8]))
print(reverse_list(["A", "B", 'C']))
