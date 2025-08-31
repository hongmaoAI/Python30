"""
Python 中有四种集合数据类型：

List：有序且可变的集合。允许重复的成员。
Tuple：有序且不可变的集合。允许重复的成员。
Set：无序、不可索引且不可变的集合，但我们可以向集合中添加新项。不允许重复的成员。
Dictionary：无序、可变且可索引的集合。不允许重复的成员。
"""
# 列表是什么？列表是不同数据类型的集合，有序且可修改（可变）。列表可以为空，也可以包含不同数据类型的项。
# 创建一个列表，在python中，有两种方式可以创建列表
# 第一种创建列表的方式，使用内置函数list()
lst_one = list()
empty_list = list()
print(len(empty_list))
# 第二种创建列表的方式，使用方括号，[]
lst_two = []
empty_list = []
print(len(empty_list))
# 具有初始值的列表。我们使用len()来检查列表的长度
fruits = ['banana', 'orange', 'mango', 'lemon']  # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  # list of vegetables
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('number of vegetables:', len(vegetables))
# 列表可以包含不同数据类型的项
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]  # 包含不同类型的列表
# 使用正索引访问列表项
# 我们使用索引访问列表中的每个项。列表索引从 0 开始。下图清楚地显示了索引从哪里开始。
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
# 使用index作为索引来获取列表中的数据
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)
# 使用负索引访问列表项
# 负索引意味着从末尾开始，-1 指的是最后一项，-2 指的是倒数第二项。
first_fruit = fruits[-1]
last_fruit = fruits[-4]
second_fruit = fruits[-2]
print(first_fruit, last_fruit, second_fruit)
# 拆解列表项
lsts = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lsts
print(first_item)
print(second_item)
print(third_item)
print(rest)
# 示例一
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
# 示例二
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(tenth)
print(rest)
# 示例三
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
# 列表切分
# 正索引：我们可以通过指定开始、结束和步长来指定一系列正索引，返回值将是一个新列表。 （开始默认值为 0，结束默认值为 len(lst) - 1（最后一项），步长默认值为 1）
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits)  # ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:]
print(all_fruits)  # ['banana', 'orange', 'mango', 'lemon']
orange_and_mango = fruits[1:3]
print(orange_and_mango)  # ['orange', 'mango']
orange_and_lemon = fruits[1:]
print(orange_and_lemon)  # ['orange', 'mango', 'lemon']
orange_and_lemon = fruits[::2]
print(orange_and_lemon)  # ['banana','mango']
# 负索引：我们可以通过指定开始、结束和步长来指定一系列负索引，返回值将是一个新列表。
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
print(all_fruits)  # ['banana', 'orange', 'mango', 'lemon']
orange_and_mongo = fruits[-3:-1]
print(orange_and_mongo)  # ['orange','mango']
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)  # ['orange','mango','lemon']
reverse_fruits = fruits[::-1]  # 负步长将按相反顺序排列列表
print(reverse_fruits)  # ['lemon','mango','orange','banana']
# 修改列表，列表是一个可变或可修改的有序集合。
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)  # ['avocado','orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['avocado','apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  # ['avocado','apple', 'mango', 'lime']
# 检索列表项，使用in运算符检查列表项是否为列表的成员
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
