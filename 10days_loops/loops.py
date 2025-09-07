# 循环
# while循环 使用关键字`while`来创建while循环。它在条件被满足时重复执行代码块 当条件变为false时，会结束循环代码块，执行循环之后的代码
"""
#语法
while condition:
	code goes here
"""
count = 0
while count < 5:
	print(count)
	count = count + 1
# 在上面的循环中，当count等于5时, 循环停止
# 如果我们想要在循环条件变为false时运行特定的代码块，我们可以使用 else 关键字
"""
# 语法
while condition:
    code goes here
else:
    code goes here
"""
count = 0
while count < 5:
	print(count)
	count = count + 1
else:
	print(count)
# 当count等于5时，循环条件变为false，循环终止，然后开始执行else块中的代码。因此，5将会被打印输出
# break和continue
# break：当我们想要退出循环时，我们使用 break 关键字
"""
while condition:
    code goes here
    if another_condition:
        break
"""
count = 0
while count < 5:
	print(count)
	count = count + 1
	if count == 3:
		break
# 上面的while循环只会打印输出0,1,2,但当count等于3时，循环会终止
# continue: 当我们想要跳过当前循环并继续执行下一个循环时，我们使用continue关键字
"""
# 语法
while condition:
    code goes here
    if another_condition:
        continue
"""
count = 0
while count < 5:
	if count == 3:
		count = count + 1
		continue
	print(count)
	count = count + 1
# while循环只会打印输出0，1，2，4
# for 循环
"""
`for`关键字用于创建for循环。和别的编程语言相似，
但语法上有一些不同。它可以用于对序列的遍历（也就
是列表、元组、字典、集合、字符串等）
"""
# 列表的for循环
"""
# 语法
for iterator in lst:
    code goes here
"""
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
	print('number为：', number)
# 字符串的for循环
"""
# 语法
for iterator in string:
    code goes here
"""
language = 'Python'
for letter in language:
	print(letter)

for i in range(len(language)):
	print('language为：', language[i])

# 元组的for循环
"""
# 语法
for iterator in tpl:
    code goes here
"""
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
	print(number)

# 字典的for循环循环遍历将会遍历字典的键。
"""
# 语法
for iterator in dct:
    code goes here
"""
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
for key in person:
	print('key为：', key)

for key, value in person.items():
	print(key, value)
# 集合的for循环
"""
# 语法
for iterator in st:
    code goes here
"""
it_companies = {
	'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
}
for company in it_companies:
	print(company)
# break :当我们想要在循环完成前退出循环时，我们使用 break 关键字
"""
for iterator in sequence:
    code goes here
    if condition:
        break
"""
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
	print(number)
	if number == 3:
		break
# 上面的例子中，当number等于3时，循环会终止
# continue :当我们想要跳过当前循环并继续执行下一个循环时，我们使用 continue 关键字
"""
for iterator in sequence:
    code goes here
    if condition:
        continue
"""
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
	print(number)
	if number == 3:
		continue
	print('Next number should be', number + 1) if number != 5 else print("loop's end")
	print('outside the loop')
# range() 函数
"""
range()`函数用于生成一个序列的数字。range(start, end, step)函数接受三个参数：起始值、
结束值和步长.默认情况下，起始值是0，步长是1。这个函数需要至少一个参数。
"""
# 使用 range() 函数生成序列
lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  # {0, 2, 4, 6, 8, 10}
# 遍历由range生成的序列
for number in range(11):
	print(number)  # 打印输出0到10， 不包括11
# 嵌套for循环 在循环中嵌套另一个循环。这种循环称为嵌套循环
"""
# 语法
for x in y:
    for t in x:
        print(t)
"""
person = {
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}
for key in person:
	if key == 'skills':
		for skill in person['skills']:
			print(skill)
# for和else 如果我们想要在循环结束时执行特定的代码块，我们可以使用`else`关键字
"""
# 语法
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
"""
for number in range(11):
	print(number)
else:
	print('The loop stops at', number)
# pass语句
"""
在python中，当需要一些语句（比如在`:`后），但我们不想执行任何代码时，
我们可以使用`pass`关键字来避免报错。此外，我们也可以用它来作为一个
占位符，以便在以后填充代码。
# 语法
for number in range(6):
    pass
"""
for number in range(6):
	pass
