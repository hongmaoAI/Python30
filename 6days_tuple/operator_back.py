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
