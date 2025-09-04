# 集合
# 集合是无序且未索引的不同元素的集合，
# 在 Python 中，集合用于存储唯一项目，可以在集合之间找到 并集、交集、差集、对称差集、子集、超集 和 不相交集。
# 创建集合 我们使用set()内置函数
# 创建空集合
st = set()
# 创建一个包含初始项目的集合
st = {'item1', 'item2', 'item3', 'item4'}
print(st)  # {'item4', 'item1', 'item3', 'item2'}
# 示例：
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)  # {'orange', 'banana', 'lemon', 'mango'}
# 获取设置的长度 我们使用len()方法来查找集合的长度。
print(len(fruits))  # 4
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))  # 4
# 要检查列表中是否存在某个项目，我们使用 in 成员运算符。
st = {'item1', 'item2', 'item3', 'item4'}
print('Does set st contain item3?', 'item3' in st)  # Does set st contain item3? True
# 示例：
fruits = {'香蕉', '橙色', '芒果', '柠檬'}
print('芒果' in fruits)  # True
# 一旦集合创建后，我们不能改变其中的任何元素，但可以添加其他的元素。
# 向集合中添加元素, 使用add()方法添加单个元素
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)  # {'item5', 'item4', 'item3', 'item2', 'item1'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)  # {'banana', 'orange', 'lemon', 'lime', 'mango'}
# 使用 update() 方法添加多个元素update() 方法允许向集合中添加多个元素。update()接收一个列表作为参数。
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
print(st)  # {'item6', 'item3', 'item7', 'item5', 'item2', 'item4', 'item1'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)  # {'banana', 'mango', 'cabbage', 'carrot', 'onion', 'potato', 'lemon', 'orange', 'tomato'}
# 从集合中移除元素
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)  # {'item3', 'item4', 'item1'}
st = {'item1', 'item2', 'item3', 'item4'}
st.discard('item4')
print(st)  # {'item2', 'item1', 'item3'}
# pop() 方法从集合中移除一个随机元素并返回该被移除的元素。
fruits = {'item1', 'item2', 'item3', 'item4'}
fruits.pop()
print(fruits)  # {'item3', 'item4', 'item2'}
# 如果我们对被移除的元素感兴趣。
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)  # mango
# 清空集合中的项目, 如果我们想要清空或清除集合中的所有项目，可以使用 _clear_ 方法。
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)  # set()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)  # set()
# 删除一个集合, 如果我们想要删除整个集合，可以使用 del 操作符。
st = {'item1', 'item2', 'item3', 'item4'}
del st
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# 将列表转换为集合, 我们可以将列表转换为集合，也可以将集合转换为列表。将列表转换为集合会去除重复项，只保留唯一项。
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)
print(st)  # {'item2', 'item3', 'item1', 'item4'}
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(fruits)  # {'lemon', 'mango', 'banana', 'orange'}
# 合并集合 使用 _union()_ 或 _update()_ 方法来合并两个集合
# union这个方法返回一个新集合
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)  # {'item3', 'item8', 'item6', 'item2', 'item1', 'item4', 'item5', 'item7'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits.union(
	vegetables))  # {'cabbage', 'mango', 'onion', 'banana', 'potato', 'carrot', 'orange', 'tomato', 'lemon'}
# update这个方法将一个集合插入到给定的集合中
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
print(st1)  # {'item5', 'item1', 'item3', 'item8', 'item6', 'item4', 'item7', 'item2'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)  # {'potato', 'cabbage', 'orange', 'tomato', 'lemon', 'mango', 'onion', 'banana', 'carrot'}
# 查找交集项, 交集返回两个集合中都存在的项的集合
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)
print(st1)  # {'item2', 'item4', 'item1', 'item3'}
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection_numbers = whole_numbers.intersection(even_numbers)
print(intersection_numbers)  # {0, 2, 4, 6, 8, 10}
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
intersection_numbers = python.intersection(dragon)
print(intersection_numbers)  # {'o', 'n'}
# 检查子集和超集 一个集合可以是另一个集合的子集或超集：
"""
子集：issubset()
超集：issuperset()
"""
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))  # True
print(st1.issuperset(st2))  # True
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)  # True even_numbers是whole_numbers的子集
whole_numbers.issuperset(even_numbers)  # True whole_numbers是even_numbers的超集
# 检查两个集合之间的差异 它返回两个集合之间的差异。
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.difference(st2))  # {'item4', 'item1'}
print(st2.difference(st1))  # set()
# 合并集合
# 如果两个集合没有共同的项或项，我们称它们为不相交集合。我们可以使用 _isdisjoint()_ 方法来检查两个集合是否相交。
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))  # False
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))  # True
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.isdisjoint(dragon))  # False
