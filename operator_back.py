# 赋值运算符 他表示将一个值存储在某个变量中，我们称之为赋值或将值分配给变量
"""
Operator | Example | Same As
---|---|---
= | x = 5 | x = 5
+= | x += 3 | x = x + 3
-= | x -= 3 | x = x - 3
*= | x *= 3 | x = x * 3
/= | x /= 3 | x = x/3
%= | x %= 3 | x = x % 3
//= | x //= 3 | x = x // 3
**= | x **= 3 | x = x ** 3
&= | x &= 3 | x = x & 3
|= | x |= 3 | x = x | 3
^= | x^= 3 | x = x^3
>>= | x >>= 3 | x = x >> 3
<<= | x <<= 3 | x = x << 3
"""
# python中的算数运算符
# 整型
print('addition', 1 + 2)  # 加法运算符 3
print('subtraction', 2 - 1)  # 减法运算符 1
print('multiplication', 2 * 3)  # 乘法运算符 6
print('division', 4 / 2)  # 除法运算符 2
print('division', 6 / 2)  # 除法运算符 3
print('division', 7 / 2)  # 除法运算符 3.5
print('division without the remainder', 7 // 2)  # 整除运算符 3
print('modulus', 3 % 2)  # 模运算符，取余 1
print('exponentiation: ', 2 ** 3)  # 指数运算符 8
# 浮点数
print('floating point number,PI', 3.14)
print('floating point number,gravity', 9.81)
# 复数
print('complex number', 1 + 1j)
print('multiplying complex numbers：', (1 + 1j) * (1 - 1j))
# 比较运算符
print('3>2', 3 > 2)  # True
print('3==2', 3 == 2)  # False
print('3!=2', 3 != 2)  # True
print('3<2', 3 < 2)  # False
print('3>=2', 3 >= 2)  # True
print('3<=2', 3 <= 2)  # False
# 比较得到True或者False
print('True==True', True == True)  # True
print('True==False', True == False)  # False
print('False==False', False == False)  # True
# 除了上述比较运算符之外，Python还使用：
# is：如果变量相等，返回True(x is y)
# is not：如果变量不相等，返回True(x is not y)
# in：如果列表包含某变量，返回True(x in y)
# not in：如果列表不包含某变量(x in y)
print('1 is 1', 1 is 1)  # True
print('1 is not 2', 1 is not 2)  # True
print('A in Apple', 'A' in 'Apple')  # True
print('B in Banana', 'B' in 'Banana')  # True
print('coding' in 'coding for all')  # True
print('a in an', 'a' in 'an')  # True
print('4 is 2 ** 2:', 4 is 2 ** 2)  # True
print('-------------------------------')
# 逻辑运算符   在python中逻辑运算用and or not
print(3 > 2 and 2 < 3)  # True
print(3 > 2 and 4 < 3)  # False
print(3 < 2 and 1 > 4)  # False
print('True and True：', True and True)  # True
print(3 > 2 or 5 > 1)  # True
print(3 > 2 or 5 < 1)  # True
print(3 < 2 or 5 < 1)  # False
print('True or False：', True or False)  # True
print(not 3 > 2)  # False
print(not True)  # False
print(not False)  # True
print(not not True)  # True
print(not not False)  # False
