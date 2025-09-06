# 条件语句
# 默认情况下，Python 脚本中的语句是从上到下顺序执行的。如果处理逻辑需要，可以通过两种方式来改变顺序：
"""
* 条件执行：如果某个表达式为真，则执行一个或多个语句块
* 重复执行：只要某个表达式为真，则重复执行一个或多个语句块。在本节中，我们将讨论if，else，elif语句。
"""
# if 条件 关键字 if 用于检查条件是否为真并执行代码块
a = 3
if a > 0:
	print("a是一个大于0的整数")
# if else 如果条件为真，则执行第一个代码块，否则执行 else 条件
a = 3
if a < 0:
	print("a是一个负数")
else:
	print("a是一个正数")
# if elif else
a = 0
if a > 0:
	print("a是一个正数")
elif a < 0:
	print("a是一个负数")
else:
	print("a是0")
# 简写 代码 if 条件 else 代码
a = -1
print("a是正数") if a > 0 else print("a是负数")
# 嵌套条件 条件可以嵌套
"""
if 条件:
    代码
    if 条件:
        代码
"""
a = 0
if a > 0:
	if a % 2 == 0:
		print("a是一个整数且为偶数")
	else:
		print("a是一个正数")
elif a == 0:
	print("a是零")
else:
	print("a是一个负数")
# if 条件和逻辑运算符 可以使用逻辑运算符*and*来避免编写嵌套条件
"""
if 条件 and 条件:
    代码
"""
a = 7
if a > 0 and a % 2 == 0:
	print('a是一个正数且为偶数')
elif a > 0 and a % 2 != 0:
	print('a是一个正数')
elif a == 0:
	print('a是零')
else:
	print('a是一个负数')
# if 和 or 逻辑运算符
"""
if 条件 or 条件:
    代码
"""
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
	print('访问授权！')
else:
	print('访问拒绝！')
