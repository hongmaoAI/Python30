# python 中的数据类型
# 整数 1 2 3
print(1)
# 浮点数 1.2 -3.2
print('float data', 1.2)
"""
定义一个复数 z=3+2j
输出一个复数 result=3+2j 
复数的实部 result.real=3
复数的虚部 result.imag=2
"""
z = 3 + 2j
print('result=', z)
print('result.real', z.real)
print('result.imag', z.imag)
"""
字符串
'hello world'
"python NiuBi"
"""
print('result 单引号', 'hello world')
print('result 双引号', "python NiuBi")
"""
布尔值 True or False
天是亮的吗？如果天是亮的，那么值是True
天是亮的吗？如果天是不亮的，那么值是false
布尔值涉及到运算符时，值会被隐式转为数值
"""
print('天是亮的吗？如果天不是亮的，那么值是', False)
print('天是亮的吗？如果天是亮的，那么值是', True)
print(True + 2)
"""
列表 列表是一个有序的集合，可以存储不同类型的数据，类似于JavaScript中的数组
"""
print('List1',[0,1,2,3,4,5]) #s所有都是相同的数据类型 - 数字列表
print(['Banana','Orange','Mango','Avocado']) # 类型相同 - 字符串相同
print(['Banana',10,False,9.81])
"""
字典 Python字典对象是以键值对格式存储的无序集合
"""
print({
    'first_name':'hong',
    'last_name':'mao',
    'age':22,
    'is_married':False,
    'skills':['JS','TS','React','Node','Python']
})
# 元组 元组是一个有序的集合，类似于列表，但元组一旦创建就不能修改，他们呢是不可变的
a = ('Earth','Jupiter','Neptune')
print('元组',a)
# 集合 集合是类似于列表和元组的集合数据类型。与列表和元组不同，集合不是一个有序的集合。就像在数学中一样，Python中的集合只存储唯一的项目
print('集合',{2,4,3,5})