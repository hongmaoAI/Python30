# 创建字符串
letter = 'P'  # 字符串可以是一个文字，也可以是一堆文字
print(letter)  # P
print(len(letter))  # 1
greeting = "hello,world"
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
# 多行字符串使用三个单引号 (''') 或者三个双引号 (""") 创建。
multiline_string_one = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string_one)
multiline_string_two = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string_two)
# 字符串中的转义序列
print('I hope everyone is enjoying the Python Challenge.\nAre you ?')  # \n换行
print('Days\tTopics\tExercises')  # 增加一个制表符 \t:制表符（4个空格）
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')
print('In every programming language it starts with \"hello,World!\"')
# 字符串格式化
# 仅字符串
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string_one = 'I am %s %s.I teach %s' % (first_name, last_name, language)
print(formated_string_one)
# 字符串和数字
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string_two = ('The area of circle with a radius %d is %.2f.'
                       % (radius, area))  # %.数值f 表示固定精度的浮点数 2 表示小数点后的 2 位有效数字
print(formated_string_two)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string_three = 'The following are python libraries：%s' % python_libraries
print(formated_string_three)
# 新式字符串格式化 (str.format) 这种格式化方法在python3中引入的
first_name_two = 'Asabeneh'
last_name_two = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}.I teach {}'.format(first_name_two, last_name_two, language)
print(formated_string)
a = 4
b = 3
print('{}+{}={}'.format(a, b, a + b))
print('{}-{}={}'.format(a, b, a - b))
print('{}*{}={}'.format(a, b, a * b))
print('{}/{}={:.2f}'.format(a, b, a / b))
print('{}%{}={}'.format(a, b, a % b))
print('{}//{}={}'.format(a, b, a // b))
print('{}**{}={}'.format(a, b, a ** b))
# 字符串和数字
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area if a circle with a radius {} is {:.2f}'.format(radius, area)  # 保留两位小数
print(formated_string)
# 字符串插值/f-String 这是一种新的字符串格式化方法，字符串插值，f-string  字符串以f开头，我们可以在相应的位置注入数据
c = 4
d = 3
print(f'{a}+{b}={a + b}')
print(f'{a}-{b}={a - b}')
print(f'{a}*{b}={a * b}')
print(f'{a}/{b}={a / b:.2f}')
print(f'{a}%{b}={a % b}')
print(f'{a}//{b}={a // b}')
print(f'{a}**{b}={a ** b}')
# 拆解字符串
# Python字符串是字符序列，与其他python有序对象-列表和元组-共享基本访问方法。从字符串中提取单个字符的最简单方法是将他们解压缩到相应的变量中。
language = 'Python'
e, f, g, h, i, j = language
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
# 通过索引获取字符串中的字符
# 在编程中，计数从零开始。因此，字符串的第一个字母位于零索引处，字符串的最后一个字母位于字符串长度减一处。
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
# 如果我们想从右边开始，我们可以使用负索引。-1是最后一个索引
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)
# 字符串切片就是将字符串切片成子字符串
language = 'Python'
first_three = language[0:3]  # 从索引开始，直到3，但是不包括3
print(first_three)
last_three = language[3:6]
print(last_three)
# 另一种方式
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)
# 字符串反转
greeting = 'Hello,World!'
print(greeting[::-1])
# 切片时跳过字符 通过将步长参数传递给切片方法，可以在切片时跳过字符
language = 'Python'
pto = language[0:6:2]
print(pto)
# 字符串方法
# capitalize():将字符串中的第一个字符转换为大写字母
challenge = 'thirty days of python'
print(challenge.capitalize())
# count(): 返回字符串中子字符串的出现次数，count(子字符串，start=..，end=..)。start 是计数的起始索引，end 是计数的最后一个索引。
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))
# endswith():判断字符串是否以特定的子字符串结尾，返回True或False
challenge = 'thirty days of python'
print(challenge.endswith('on')) #True
print(challenge.endswith('tion')) #False
