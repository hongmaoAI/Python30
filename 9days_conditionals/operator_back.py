# 使用 input 获取用户输入（例如：“输入你的年龄：”）。如果用户 18 岁或以上，给出反馈：你已经足够大，可以学习驾驶。如果未满 18 岁，则给出需要等待的年数。输出：
# 输入你的年龄：30
# 你已经足够大，可以学习驾驶。
# 输出：
# 输入你的年龄：15
# 你还需要等待3年才能学习驾驶
from numpy.ma.core import true_divide

user_import = input('输入你的年龄：')
user_import = int(user_import)
if user_import >= 18:
	print('你已经足够大，可以学习驾驶')
else:
	print('你还需要等待3年才能学习驾驶。')

# 使用 if…else 比较 my_age 和 your_age 的值。谁更年长（我还是你）？使用 input（“输入你的年龄：”）获取年龄作为输入。您可以使用嵌套条件来打印'年'表示 1 年的年龄差异，'年'表示更大的差异，如果 my_age = your_age，则打印自定义文本。输出：
# 输入你的年龄：30
# 你比我大5岁。
your_age = input('输入你的年龄：')
your_age = int(your_age)
my_age = 25
if your_age > my_age:
	print('你比我大%s岁' % (your_age - my_age))
elif my_age == your_age:
	print('咱们两人的年龄居然一样')
else:
	print('你比我的年龄小%s岁' % (my_age - your_age))
# 使用输入提示从用户处获得两个数字。如果 a 大于 b，返回 a 大于 b，如果 a 小于 b，返回 a 小于 b，否则返回 a 等于 b。输出:
# 输入第一个数字：4
# 输入第二个数字：3
# 4大于3
a = input('输入第一个数字：')
b = input('输入第二个数字：')
a = int(a)
b = int(b)
if a > b:
	print('%a大于%s' % (a, b))
else:
	print('%a小于%s' % (a, b))
# 2级
# 编写代码，根据学生的分数给出等级：
'''
80-100, A
70-79, B
60-69, C
50-59, D
0-49, F
'''
grade = input('输入你的分数：')
grade = int(grade)
if 80 <= grade <= 100:
	print('80-100,A')
elif 70 <= grade <= 79:
	print('70-79,B')
elif 60 <= grade <= 69:
	print('60-69,C')
elif 50 <= grade <= 59:
	print('50-59,D')
else:
	print('0-49,F')
# 检查是否是秋天、冬天、春天或夏天。如果用户输入：9 月、10 月或 11 月，是秋天。12 月、1 月或 2 月，是冬天。3 月、4 月或 5 月，是春天。6 月、7 月或 8 月，是夏天。
month = input('输入月份：')
month = int(month)
if 9 <= month <= 10:
	print('9 月、10 月或 11 月，是秋天。')
elif 3 <= month <= 5:
	print('3 月、4 月或 5 月，是春天。')
elif 6 <= month <= 8:
	print('6 月、7 月或 8 月，是夏天。')
else:
	print('12 月、1 月或 2 月，是冬天。')
'''
以下列表包含了一些水果：
fruits = ['banana', 'orange', 'mango', 'lemon']
如果列表中不存在某个水果，则将其添加到列表中并打印修改后的列表。如果水果存在，则打印('该水果已在列表中')。
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_food = input('输入水果数量：')
if fruits_food not in fruits:
	fruits.append(fruits_food)
	print(fruits)
else:
	print('该水果已在列表中')
