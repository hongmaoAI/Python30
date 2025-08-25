# 声明一个值是你年龄的整型变量
age = 27
# 声明一个值是你身高的浮点型变量
me_height = 178.1
# 声明一个值是复数变量
z = 7 + 2j
# 编写一个脚本，提示用户输入三角形的底和高，并计算这个三角形的面积（面积 = 0.5 x b x h）。
"""
    输入底: 20
    输入高: 10
    三角形的面积是 100
"""
# bottom = input('请输入三角形的底：')
# height = input('请输入三角形的高：')
# triangle_area = 0.5 * int(bottom) * int(height)
# print('三角形的面积是：', triangle_area)  # 100
# 编写一个脚本，提示用户输入三角形的边 a、边 b 和边 c。计算三角形的周长（周长 = a + b + c）。
"""
    输入边 a: 5
    输入边 b: 4
    输入边 c: 3
    三角形的周长是 12
"""
# a = input('请输入三角形的第一条边：')
# b = input('请输入三角形的第二条边：')
# c = input('请输入三角形的第三条边：')
# circumference = int(a) + int(b) + int(c)
# print('三角形的周长是：', circumference)  # 12
# 提示用户输入矩形的长度和宽度。计算其面积（面积 = 长 x 宽）和周长（周长 = 2 x (长 + 宽)）
# rectangle_a = input('请输入矩形的长：')
# rectangle_b = input('请输入矩形的宽：')
# rectangle_circumference = (int(rectangle_a) + int(rectangle_b)) * 2
# rectangle_area = int(rectangle_a) * int(rectangle_b)
# print('矩形的面积为：', rectangle_area)
# print('矩形的周长为：', rectangle_circumference)
# 求出 'python' 和 'dragon' 的长度，并进行一个假的比较语句。
python_len = len('python')
dragon_len = len('dragon')
print('python与dragon长度比较', python_len > dragon_len)  # False
# 使用 and 运算符检查 'python' 和 'dragon' 中是否都有 'on'。
print('on' in 'python' and 'on' in 'dragon')  # True
# I hope this course is not full of jargon。使用 in 运算符检查句子中是否有 jargon。
print('jargon' in 'I hope this course is not full of jargon')  # True
# 'dragon' 和 'python' 中都没有 'on'。
print('on' not in 'dragon' and 'on' not in 'python')  # False
# 找到文本 python 的长度，并将该值转换为浮点数，然后将其转换为字符串。
len_python = len('python')
print(str(float(len_python)))  # 6.0
print(type(str(float(len_python))))  # str
# 偶数可以被 2 整除，余数为零。如何使用 Python 检查一个数字是偶数还是奇数？
input_data = int(input('请你输入一个数：')) % 2 == 0
print(input_data and '这个数为偶数')
# 检查 7 除以 3 的Floor除法是否等于 2.7 的整数转换值。
print(7 / 3 == int(2.7))  # False
# 检查 '10' 的类型是否等于 10 的类型。
print(type('10') == type(10))  # False
# 检查 int('9.8') 是否等于 10。
print(int(float('9.8')) == 10)  # False
