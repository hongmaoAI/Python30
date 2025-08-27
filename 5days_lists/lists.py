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
