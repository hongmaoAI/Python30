# 类和对象
"""
在Python中，一切都是对象，都有其属性和方法
在程序中使用的数字、字符串、列表、字典、元组、集合等都是相应内置类的对象
创建类来创建对象
类就像一个对象构造器，或者说是创建对象的"蓝图"
类定义了对象的属性和行为，而对象则代表了类
"""

# 创建类
"""
# 语法
class 类名:
	python code
"""


class Person:
	pass


print(Person)
# 创建对象  通过调用类来创建对象
p = Person()
print(p)


# 类构造函数
class Person:
	def __init__(self, name):
		print('self.name', name)
		self.name = name


p = Person('Asabeneh')
print(p.name)
print(p)


# 向构造函数添加更多参数
class Person_eg2:
	def __init__(self, firstname, lastname, age, country, city):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.country = country
		self.city = city


p = Person_eg2('hong', 'mao', 27, 'US', 'NewYork')
print(p.firstname)  # hong
print(p.lastname)  # mao
print(p.age)  # 27
print(p.country)  # US
print(p.city)  # NewYork


# 对象方法
# 对象可以有方法。方法是属于对象的函数
class Person:
	def __init__(self, firstname, lastname, age, country, city):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.country = country
		self.city = city

	def person_info(self):
		return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'


p = Person('hong', 'mao', 27, 'US', 'NewYork')
print(p.person_info())  # hong mao今年27岁。他住在US的NewYork。


# 对象默认方法 如果我们为构造函数中的参数提供默认值，可以避免在不带参数调用或实例化类时出现错误
class Person:
	def __init__(self, firstname='hong', lastname='mao', age=27, country='US', city='NewYork'):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.country = country
		self.city = city

	def person_info(self):
		return f'{self.firstname} {self.lastname}，今年{self.age}岁。他住在{self.country}的{self.city}'


p1 = Person()
print(p1.person_info())  # hong mao，今年27岁。他住在US的NewYork
p2 = Person('John', 'Doe', 28, 'Nomanland', 'Noman city')
print(p2.person_info())  # John Doe，今年28岁。他住在Nomanland的Noman city


# 修改类默认值的方法
# person类的所有构造函数参数都有默认值 此外，我们还有一个skills参数，可以通过方法访问
class Person:
	def __init__(self, firstname='hong', lastname='mao', age=27, country='US', city='NewYork'):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.country = country
		self.city = city
		self.skills = []

	def person_info(self):
		return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'

	def add_skill(self, skill):
		self.skills.append(skill)


p3 = Person()
print(p3.person_info())  # hong mao今年27岁。他住在US的NewYork。
p3.add_skill('HTML')
p3.add_skill('CSS')
p3.add_skill('JavaScript')
print(p3.skills)  # ['HTML', 'CSS', 'JavaScript']
p4 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p4.person_info())  # John Doe今年30岁。他住在Nomanland的Noman city。

# 继承 继承允许我们定义一个继承父类所有功能的类。它使代码可重用
"""
# 语法
class 子类名(父类名):
	python code
"""


# eg:
class Student(Person):
	pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())  # Eyob Yetayeh今年30岁。他住在Finland的Helsinki。
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # ['JavaScript', 'React', 'Python']
print(s2.person_info())  # Lidiya Teklemariam今年28岁。他住在Finland的Espoo。
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)  # ['Organizing', 'Marketing', 'Digital Marketing']
