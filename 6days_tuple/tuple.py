# tuple()：创建一个空元组
empty_tuple = ()
# 或使用元组构造函数
empty_tuple_constructor = tuple()
# 创建一个具有初始值的元组
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(tpl)
print(fruits)
# 元组长度
# 我们使用len()方法来获取元组的长度
tpl = ('item1', 'item2', 'item3')
print(len(tpl))  # 3
# 获取元组项
# 正索引与列表数据类型类似，我们使用正索引或负索引来访问元组项。
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print(first_item, second_item)  # item1 item2
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruits = fruits[0]
second_fruits = fruits[1]
last_index = len(fruits) - 1
last_fruits = fruits[last_index]
print(first_fruits, second_fruits, last_fruits)  # banana orange lemon
# 负索引
# 负索引是从末尾开始的，-1 表示最后一项，-2 表示倒数第二项，列表/元组长度的负数表示第一项。
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[-4]
second_item = tpl[-3]
print(first_item, second_item)  # item1 item2
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruits = fruits[-4]
second_fruits = fruits[-3]
last_fruits = fruits[-1]
print(first_fruits, second_fruits, last_fruits)  # banana orange lemon
# 元组切片
# 我们可以通过指定开始和结束的索引范围来切出子元组，返回值是一个包含指定项的新元组。
# 正索引范围
tpl = ('item1', 'item2', 'item3', 'item4')
al1_items = tpl[0:4]
al2_item = tpl[0:]
middle_two_items = tpl[1:3]
print(al1_items, al2_item,
      middle_two_items)  # ('item1', 'item2', 'item3', 'item4') ('item1', 'item2', 'item3', 'item4') ('item2', 'item3')
# 负索引范围
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]
print(all_items, middle_two_items)  # ('item1', 'item2', 'item3', 'item4') ('item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]
print(all_fruits, orange_mango,
      orange_to_the_rest)  # ('banana', 'orange', 'mango', 'lemon') ('orange', 'mango') ('orange', 'mango', 'lemon')
# 将元组更改为列表
# 我们可以将元组更改为列表，将列表更改为元组。如果我们想修改元组，我们应该将其更改为列表。
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
print(lst)  # ['item1', 'item2', 'item3', 'item4']
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)  # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)  # ('apple', 'orange', 'mango', 'lemon')
# 检索元组中的项
# 我们可以使用 in 检查元组中是否存在某个项，它返回一个布尔值。
tpl = ('item1', 'item2', 'item3', 'item4')
print('item2' in tpl)  # True
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)  # True
print('apple' in fruits)  # False
# 连接元组,我们可以使用 + 运算符连接两个或多个元组
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
print(tpl3)  # ('item1', 'item2', 'item3', 'item4', 'item5', 'item6')
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
# 删除元组
# 不能删除元组中的单个项，但可以使用 del 删除元组本身。
tpl1 = ('item1', 'item2', 'item3')
del tpl1
print(tpl1)
