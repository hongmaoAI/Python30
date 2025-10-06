# 使用 input 获取用户输入（例如：“输入你的年龄：”）。如果用户 18 岁或以上，给出反馈：你已经足够大，可以学习驾驶。如果未满 18 岁，则给出需要等待的年数。输出：
# 输入你的年龄：30
# 你已经足够大，可以学习驾驶。
# 输出：
# 输入你的年龄：15
# 你还需要等待3年才能学习驾驶
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
