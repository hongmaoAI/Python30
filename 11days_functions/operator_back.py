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


# 声明一个名为 capitalize_list_items 的函数。它接受一个列表作为参数，并返回一个大写的列表项。
def capitalize_list_items(args):
    for arg in args:
        print(arg.upper())
    return None


capitalize_list_items(['apple', 'orange', 'banana'])


# 声明一个名为 add_item 的函数。它接受一个列表和一个项作为参数。它返回在末尾添加项的列表。
def add_item(item, args):
    new_list = args.copy()
    new_list.append(item)
    return new_list


print(add_item('apple', ['banana', 'orange']))


# 声明一个名为 remove_item 的函数。它接受一个列表和一个项作为参数。它返回移除该项后的列表。
def remove_item(item, args):
    new_args = args.copy()
    new_args.remove(item)
    return new_args


print(remove_item('apple', ['banana', 'orange', 'apple']))


# 声明一个名为 sum_of_numbers 的函数。它接受一个数字参数并将范围内的所有数字相加。
def sum_of_numbers(number):
    sums = range(0, number + 1)
    sums_one = 0
    for sum_one in sums:
        sums_one = sum_one + sums_one
    return sums_one


print(sum_of_numbers(3))


# 声明一个名为 sum_of_odds 的函数。它接受一个数字参数并将范围内的所有奇数相加。
def sum_of_odds(number):
    number_list = range(0, number + 1)
    add_env = 0
    for sums in number_list:
        if sums % 2 != 0:
            add_env = sums + add_env
    return add_env


print(sum_of_odds(3))


# 声明一个名为 sum_of_even 的函数。它接受一个数字参数并将范围内的所有偶数相加。
def sum_of_even(number):
    number_list = range(0, number + 1)
    add_odd = 0
    for sums in number_list:
        if sums % 2 == 0:
            add_odd = sums + add_odd
    return add_odd


print(sum_of_even(4))
