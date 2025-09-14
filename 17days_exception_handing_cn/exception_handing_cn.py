# 异常处理
# 使用 try 和 except 优雅地处理错误`
"""
# 语法
try:
#    没有错误时，执行
except:
#    如果出错，执行这个块中的代码
"""
# eg1:
try:
	print(10 + '5')
except Exception:
	print('出现一些错误')

# eg2:
try:
	name = input('输入你的名字：')
	year_born = input('你出生的年份：')
	age = 2025 - int(year_born)
	print(f'你是{name},你的年龄是{age}')
except:
	print('出现了一些错误')

# eg3:
try:
	name = input('输入你的名字：')
	year_born = input('你出生的年份：')
	age = 2025 - year_born
	print(f'你是{name},你的年龄是{age}')
except TypeError:
	print('发生了类型错误')
except ValueError:
	print('发生了值错误')
except ZeroDivisionError:
	print('发生了除零错误')

# eg4:
try:
	name = input('输入你的名字：')
	year_born = input('你出生的年份：')
	age = 2025 - int(year_born)
	print(f'你是{name},你的年龄是{age}')
except TypeError:
	print('发生了类型错误')
except ValueError:
	print('发生了值错误')
except ZeroDivisionError:
	print('发生了除零错误')
else:
	print('我通常与try块一起运行')
finally:
	print('我总是运行。')
# 简化上述代码
try:
	name = input('输入你的名字：')
	year_born = input('你出生的年份：')
	age = 2025 - int(year_born)
	print(f'你是{name},你的年龄是{age}')
except Exception as e:
	print(e)


# 打包和解包
# * 用于元组
# ** 用于字典

# 解包列表
def sum_of_five_nums(a, b, c, d, e):
	return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# 在内置的range函数中使用解包, 该函数需要一个起始和结束
numbers = range(2, 7)
print(list(numbers))
# 在内置的range函数中使用解包，该函数需要一个起始和结束参数
args = [2, 7]  # [2, 3, 4, 5, 6]
numbers = range(*args)
print(numbers)  # range(2, 7)

# 列表/元组解包
counteries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = counteries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7


# 解包字典
def unpacking_person_info(w_name, country, city, age):
	return f'{w_name}住在{country}的{city},他{age}岁'


dct = {'w_name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
print(unpacking_person_info(**dct))  # Asabeneh住在Finland的Helsinki,他250岁


# 打包
# 当不知道函数传递多少个参数 用打包方法让我们的函数接受无限数量或任意数量的参数
# 打包列表
def sum_all(*args):
	s = 0
	for i in args:
		s += i
	return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# 打包字典
def packing_person_info(**kwargs):
	for key in kwargs:
		print(f"{key}={kwargs[key]}")
	return kwargs


print(packing_person_info(name='Asabeneh', country='Finland', city='Helsinki', age=250))
"""
name=Asabeneh
country=Finland
city=Helsinki
age=250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}s
"""

# 展开
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

# 枚举 我们对列表的索引感兴趣 enumerate内置函数
for index, item in enumerate([20, 30, 40]):
	print(index, item)
"""
0 20
1 30
2 40
"""

for index, i in enumerate(counteries):
	if i == 'Finland':
		print(f'国家 {i} 位于索引{index}')  # 国家 Finland 位于索引0

# Zip 列表组合
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
	fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
