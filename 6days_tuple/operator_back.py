# 创建一个空元组
# 第一种创建方法
empty_tuple_one = ()
# 第二种创建方式
empty_tuple_two = tuple()
# 创建一个包含你姐妹和兄弟名字的元组
family_brother_tuple = ('lantu', 'shali', 'doudou', 'daben', 'dada', 'tiaotiao')
family_sister_tuple = ('sister1', 'sister2', 'sister3')
# 连接兄弟姐妹元组并将其分配给 siblings
siblings = family_brother_tuple + family_sister_tuple
print(siblings)
# 你有多少兄弟姐妹
print(len(siblings))
# 修改兄弟姐妹元组并添加你父母的名字，然后将其分配给 family_members
family_brother_list = list(family_brother_tuple)
family_sister_list = list(family_sister_tuple)
family_brother_list.append('baimao')
family_sister_list.append('BigSister')
family_members_list = family_brother_list + family_sister_list
print(family_members_list)
family_members = tuple(family_members_list)
print(family_members)

# 2级
# 从 family_members 中获取兄弟姐妹和父母
family_members_brother = family_members[0:6]
family_members_sister = family_members[7:10]
# 创建 fruits、vegetables 和 animal products 元组。连接三个元组并将其分配给名为 food_stuff_tp 的变量。
fruits = ('apple', 'orange', 'banana')
vegetables = ('potato', 'cabbage')
animal_products = ('Cat_Food', 'Dog_Food')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# 将 food_stuff_tp 元组更改为 food_stuff_lt 列表
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# 从 food_stuff_tp 元组或 food_stuff_lt 列表中切出中间项或项。
print(len(food_stuff_tp))
middle_food_stuff_lt = food_stuff_lt[int(len(food_stuff_tp) / 2)]
print(middle_food_stuff_lt)  # potato
# 从 food_staff_lt 列表中切出前三项和最后三项
top_three = food_stuff_lt[:3]
print(top_three)  # ['apple', 'orange', 'banana']
last_three = food_stuff_lt[-3:]
print(last_three)  # ['cabbage', 'Cat_Food', 'Dog_Food']
# 完全删除 food_staff_tp 元组
del food_stuff_tp
# 检查元组中是否存在项：
# 检查 'Estonia' 是否在 nordic_country 元组中
# 检查 'Iceland' 是否在 nordic_country 元组中
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # False
print('lceland' in nordic_countries)  # False
