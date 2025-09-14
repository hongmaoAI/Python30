# 正则表达式
"""
正则表达式（RegEx）是一种特殊的文本字符串，有助于在数据中查找模式。
RegEx可用于检查不同数据类型中是否存在某种模式。
要在Python中使用RegEx，首先我们应该导入RegEx模块，该模块被称为*re*
"""
# re 模块 导入模块后，我们可以使用它来检测或查找模式
"""
# 导入语法
import re
"""
import re

# re模块中的方法
# re.match() ：只在字符串的第一行开头搜索，如果找到则返回匹配的对象，否则返回None
# re.search() ：如果字符串中的任何地方（包括多行字符串）有匹配项，则返回匹配对象
# re.findall() ：返回包含所有匹配项的列表
# re.split() ：接受一个字符串，在匹配点处分割，返回一个列表
# re.sub() ：替换字符串中的一个或多个匹配项
"""
# 匹配语法
substring是一个字符串或模式，string是我们查找模式的文本，re.I是忽略大小写
re.match(substring,string,re.I)
"""

txt = 'I love to teach python and javaScript'
match = re.match('i love to teach', txt, re.I)
# 获取匹配的起始和结束位置，作为元组
span = match.span()
print(span)  # (0, 15)
# 从span中找到起始和结束位置
start, end = span
print(start, end)  # 0 15
# 获取[0,15]的字符串
substring = txt[start:end]
print(substring)  # I love to teach
# 搜索
"""
# 语法
re.search(substring, string, re.I)
# substring是一个模式，string是我们查找模式的文本，re.I是忽略大小写标志
"""
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# search 返回一个带有span和match的对象
match_two = re.search('first', txt, re.I)
print(match_two)  # <re.Match object; span=(100, 105), match='first'>
span_two = match_two.span()
print(span_two)  # (100, 105)
start_two, end_two = span_two
print(start_two, end_two)  # 100 105
substring_two = txt[start_two:end_two]
print(substring_two)  # first

# 使用 findall 搜索所有匹配项 findall() 将所有匹配项作为列表返回
findall_one = re.findall('language', txt, re.I)
print(findall_one)  # ['language', 'language']

"""
由于我们使用*re.I*，所以包含了大小写字母。
如果我们没有re.I标志，那么我们将不得不以不同的方式编写我们的模式
"""
findall_two = re.findall('Python|python', txt)
print(findall_two)  # ['Python', 'python']

findall_three = re.findall('[Pp]ython', txt)
print(findall_three)  # ['Python', 'python']

# 替换子字符串
match_replaced = re.sub('Python|python', 'JavaScript', txt, flags=re.I)
print(
	match_replaced)  # JavaScript is the most beautiful language that a human being has ever created. I recommend
# JavaScript for a first programming language
# 或者
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, flags=re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created. I recommend
# JavaScript for a first programming language

# 使用RegEx拆分文本 split
print(re.split('\n',
               txt))  # ['Python is the most beautiful language that a human being has ever created.', 'I recommend python for a first programming language']

# 编写RegEx模式
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']
# 不区分大小写，第一种写法
matches = re.findall(regex_pattern, txt, flags=re.I)
print(matches)  # ['Apple', 'apple']
# 不区分大小写，第二种写法
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
"""
* [a-c] 表示，a或b或c
* [a-z] 表示，从a到z的任何字母
* [A-Z] 表示，从A到Z的任何字符
* [0-3] 表示，0或1或2或3
* [0-9] 表示从0到9的任何数字
* [A-Za-z0-9] 任何单个字符，即a到z，A到Z或0到9
"""
regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

regex_pattern = r'[a-zA-Z0-9]'
matches = re.findall(regex_pattern, txt)
print(matches)

# d 是一个特殊字符，表示数字
regex_pattern = r'\d'  # d 是一个特殊字符
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

regex_pattern = r'\d+'  # + 表示一个或多个
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

# 句点(.)
regex_pattern = r'[a].'  # 这个方括号表示 a 和 . 表示任何字符
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# 零次或多次(*)
regex_pattern = r'[a].*'  # . 任何字符，* 任何字符零次或多次
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# 零次或一次(?)  它可以存在，也可以不存在。
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# RegEx中的量词 使用大括号 指定模式的长度
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

# 脱字符(^)
# 以什么开始
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
# 否定
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z]+'  # ^ 在方括号内表示否定，不是A-Z，不是a-z，不是空格
matches = re.findall(regex_pattern, txt)
print(matches)  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' 6,  2019 ', ' ', ' ', ' ', ' 8, 2021']
