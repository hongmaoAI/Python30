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
# 添加列表项，要将项添加到现有列表的末尾，我们使用append()方法
lst = list()
lst.append('item')
print(lst)  # ['item']
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)  # ['banana','orange','mango','lemon','apple']
fruits.append('lime')
print(fruits)  # ['banana','orange','mango','lemon','apple','lime']
# 插入列表项,我们可以使用 *insert()* 方法在列表中的指定索引处插入单个项。请注意，其他项将向右移动。*insert()* 方法接受两个参数：索引和要插入的项。
lst = ['item1', 'item2']
lst.insert(-1, 'haha')
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # 将apple插入索引为2 其他项向右移动
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')
print(fruits)  # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
# 移除列表项 使用 *remove()* 方法从列表中删除指定的项
lst = ['item1', 'item2']
lst.remove('item2')
print(lst)
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
# 使用 Pop 删除列表项 使用 *pop()* 方法删除指定索引（如果未指定索引，则删除最后一项）：
lst = ['item1', 'item2']
lst.pop()  # 删除列表的最后一项
print(lst)  # 结果为 ['item1']
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)  # ['orange','mango']
# 使用 Del 删除列表项,使用 *del* 关键字删除指定索引，也可以用于删除索引范围内的项。它还可以完全删除列表
lsts = ['item1', 'item2']
del lst[0]  # 删除列表某一项
# print(lst)  # ['item2']
del lst  # 删除整个列表 (删除的列表不能输出)
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]
print(fruits)  # 删除索引为1到3的项 结果为['orange', 'lime']
del fruits  # 删除整个列表
# 清空列表项，使用 *clear()* 方法清空列表：
lst = ['item1', 'item2']
lst.clear()
print(lst)  # []
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)  # []
# 列表复制,可以通过将其重新分配给新变量来复制列表: list2 = list1。现在，list2 是 list1 的引用，我们对 list2 进行的任何更改也将修改原始的 list1。但是有很多时候我们不想修改原始的列表，而是想要一个不同的副本。为了避免这个问题，我们使用 *copy()*。
lst = ['item1', 'item2']
lst_copy = lst.copy()
print(lst_copy)  # ['item1','item2']
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
fruits_copy[0] = 'apple'
print(fruits)  # ['banana', 'orange', 'mango', 'lemon']
print(fruits_copy)  # ['apple', 'orange', 'mango', 'lemon']
# 连接列表,有几种方法可以连接或连接两个或多个列表。
'''
(1)加号(+)
# 语法
list3 = list1 + list2
'''
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = positive_numbers + zero + negative_numbers
print(integers)  # [1,2,3,4,5,0,-5,-4,-3,-2,-1]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# 使用 *extend()方法 extend()* 方法可以将列表附加到列表中。请参阅下面的示例。
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)  # ['item1', 'item2', 'item3', 'item4', 'item5']
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6, 7]
num1.extend(num2)
print('Numbers', num1)  # [0,1,2,3,4,5,6,7]
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)  # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:',
      fruits)  # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# 统计列表项,使用 *count()* 方法返回列表中指定项出现的次数:
lst = ['item1', 'item2']
print(lst.count('item1'))  # 1
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3
# 查找项的索引,*index()* 方法返回列表中项的索引:
lst = ['item1', 'item2']
print(lst.index('item1'))  # 0
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('banana'))  # 0
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2
# 列表反转,使用 *reverse()* 方法反转列表的顺序。
lst = ['item1', 'item2']
lst.reverse()
print(lst)  # ['item2', 'item1']
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]
# 列表排序,要对列表进行排序，我们可以使用 *sort()* 方法或内置函数 *sorted()*。*sort()* 方法将列表项按升序重新排序并修改原始列表。如果 *sort()* 方法的 reverse 参数为 true，则会按降序排列列表。
# sort():这个方法会修改原始列表
lst = ['item3', 'item2', 'item5']
lst.sort()  # ['item2', 'item3','item5']
lst.sort(reverse=True)  # ['item5', 'item3', 'item2']
print(lst)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()  # [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)  # [26, 25, 25, 24, 24, 24, 22, 19]
print(ages)
# sorted(): 不会修改原始列表，而是返回一个新列表**示例:
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
