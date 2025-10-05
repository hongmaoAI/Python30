# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 找到集合 it_companies 的长度
print(len(it_companies))  # 7
# 向 it_companies 添加'Twitter'
it_companies_list = list(it_companies)
it_companies_list.append('Twitter')
it_companies = set(it_companies_list)
print(it_companies)  # {'Oracle', 'Facebook', 'Twitter', 'Apple', 'Microsoft', 'IBM', 'Amazon', 'Google'}
# 一次性向集合 it_companies 插入多个 IT 公司
fruits = ('apple', 'orange', 'strawberry')
it_companies.update(fruits)
print(it_companies)
# 从集合 it_companies 中移除一家公司
# 随机移除
it_companies.pop()
print(
	it_companies)  # {'strawberry', 'Twitter', 'Apple', 'orange', 'Google', 'IBM', 'Oracle', 'Amazon', 'apple', 'Facebook'}
# 指定移除
it_companies.remove('orange')
print(it_companies)  # {'strawberry', 'Twitter', 'Apple', 'Google', 'IBM', 'Oracle', 'Amazon', 'apple', 'Facebook'}
# 移除和丢弃之间有什么区别
# 当元素在集合中不存在时，使用remove会报错，使用discard不会报错
# it_companies.remove('HTML') # KeyError: 'HTML'
it_companies.discard('HTML')
print(it_companies)
# 2级
# 合并 A 和 B  union  update  isdisjoint
C = A.union(B)
print(C)  # {19, 20, 22, 24, 25, 26, 27, 28}
# 找到 A 和 B 的交集
C_intersection = A.intersection(B)
print(C_intersection)  # {19, 20, 22, 24, 25, 26}
# A 是 B 的子集吗 issubset
print(A.issubset(B))  # True
# A 和 B 是不相交集合吗
print(A.isdisjoint(B))  # False
# A 和 B 之间的对称差异是什么
print(A.symmetric_difference(B))  # {27, 28}
# 完全删除集合
del it_companies
