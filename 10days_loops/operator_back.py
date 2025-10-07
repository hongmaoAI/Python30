# 分别使用while和for实现从0到10的迭代。
sum_one = 0
while sum_one <= 10:
	print(sum_one)
	sum_one += 1

list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for lists in list_one:
	print(lists)

# 分别使用while和for实现从10到0的迭代。
sum_two = 10
while 0 <= sum_two <= 10:
	print(sum_two)
	sum_two -= 1

list_two = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for lists in list_two:
	print(lists)

# 写一个循环，调用7次`print()`函数，输出如下的三角形：
'''
 #
 ##
 ###
 ####
 #####
 ######
 #######
'''
str_one = '#'
sum = 0
while 0 <= sum < 7:
	print(f'{str_one}' + '#')
	sum += 1
	str_one += '#'

# 使用嵌套循环来实现下面的输出：
'''
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
list_three = ['# # # # # # # #']
sum = 0
for strs in list_three:
	while 0 <= sum < 8:
		print(strs)
		sum += 1

# 使用循环实现下面格式的输出：
'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
m = 0
mm = 0
while 0 <= m <= 10:
	mm = m * m
	print(f'{mm}={m}x{m}')
	m += 1
# 用for循环遍历列表`['Python', 'Numpy','Pandas','Django', 'Flask']`，并打印输出每个元素。
lists = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for list_four in lists:
	print(list_four)

# 用for循环从0到100遍历并且打印输出所有偶数。
sum = 0
while 0 <= sum < 100:
	sum += 1
	while sum % 2 == 0:
		print(sum)
		break

for sums in range(0, 101):
	if sum % 2 == 0:
		print(sums)

# 用for循环从0到100遍历并且打印输出所有奇数。
for sums in range(0, 101):
	if sums % 2 != 0:
		print(sums)

# 二级
# 使用for循环从0到100遍历并且输出所有数字的和。
sums = 0
for i in range(0, 101):
	sums = i + sums
print('The sum of all numbers is %s' % sums)

# * 使用for循环从0到100遍历并且分别输出所有奇数和所有偶数的和。
odd_sums = 0
even_sums = 0
for i in range(0, 101):
	if i % 2 == 0:
		odd_sums = i + odd_sums

	else:
		even_sums = i + even_sums

print(f'The sum of all odd numbers is {odd_sums}.')
print(f'The sum of all even numbers is {even_sums}.')
