# 文件处理 文件格式（.txt、.json、.xml、.csv、.tsv、.excel）
# 处理数据我们使用内置函数 open()
"""
# 语法
open('filename',mode)  # mode(r,a,w,x,t,b)可以是读取，写入，更新
* "r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则返回错误
* "a" - 追加 - 打开文件进行追加，如果文件不存在则创建文件
* "w" - 写入 - 打开文件进行写入，如果文件不存在则创建文件
* "x" - 创建 - 创建指定的文件，如果文件已存在则返回错误
* "t" - 文本 - 默认值。文本模式
* "b" - 二进制 - 二进制模式
"""

# 引入OS模块
import os
# 引入json
import json
# 引入csv模块
import csv
# 引入模块
import xlrd

f = open('./reading_file_example.txt')
print(f)
# 文件有不同的读取方法：read()、readline、readlines， 打开的文件必须用 close() 方法关闭
# 打开文件
txt = f.read()
# 关闭文件
f.close()
print(type(txt))  # <class 'str'>

# 打印文本文件的前10个字符
f = open('./reading_file_example.txt')
txt = f.read(10)
print(txt)
f.close()

# readline()：只读取第一行
f = open('./reading_file_example.txt')
txt_line = f.readline()
print(txt_line)  # 30days study python
f.close()

# readlines()：逐行读取所有文本，并返回一个行列表
f = open('./reading_file_example.txt')
lines = f.readlines()
print(lines)
print(type(lines))  # <class 'list'>
f.close()

# 获取所有行作为列表的另一种方法是使用 splitlines()：
f = open('./reading_file_example.txt')
lines = f.read().splitlines()
print(lines)
print(type(lines))  # <class 'list'>
f.close()

"""
* 在打开文件后，我们应该关闭它。我们很容易忘记关闭它们。
* 使用 with 打开文件的新方法 它会自动关闭文件
"""
# 用with方法发重写前面的例子
with open('./reading_file_example.txt') as f:
	lines = f.read().splitlines()
	print('lines_type', type(lines))  # lines_type <class 'list'>
	print('lines', lines)

# 打开文件,进行写入和更新
"""
要写入现有文件，我们必须向 _open()_ 函数添加模式作为参数：
* "a" - 追加 - 将在文件末尾追加，如果文件不存在则创建一个新文件。
* "w" - 写入 - 将覆盖任何现有内容，如果文件不存在则创建。
"""

# 追加文件
with open('./reading_file_example.txt', 'a') as f:
	f.write('on line')
# 写入文件 如果文件不存在，则重新创建一个文件
with open('./writing_file_example.txt', 'w') as f:
	f.write('Create a file')

# 删除文件 -> OS模块
# 如果文件不存在，remove方法将引发错误，因此最好使用条件语句：
if os.path.exists('./example.txt'):
	os.remove('./example.txt')
else:
	print('文件不存在')

# 文件类型
# 我们来处理带有json扩展名的文件  JSON代表JavaScript对象表示法  实际上它就是字典

# 字典
person_dct = {
	"name": "Asabeneh",
	"country": "Finland",
	"city": "Helsinki",
	"skills": ["JavaScrip", "React", "Python"]
}
# JSON: 字典的字符串形式
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
# 我们使用三个引号并使其多行以使其更具可读性
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# 将JSON转换为字典
# 要将JSON更改为字典，首先我们导入json模块，然后使用 loads_方法
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_dct = json.loads(person_json)
print(type(person_dct))  # <class 'dict'>
print(person_dct)

# 将字典转换为JSON
# 要将字典更改为JSON，我们使用 dumps 方法。
person = {
	"name": "Asabeneh",
	"country": "Finland",
	"city": "Helsinki",
	"skills": ["JavaScrip", "React", "Python"]
}
# 将字典转换为JSON字符串
person_json = json.dumps(person, indent=4)  # indent可以是2，4，8，它漂亮的打印了
print(type(person_json))  # <class 'str'>
print(person_json)

# 保存为JSON文件
person = {
	"name": "Asabeneh",
	"country": "Finland",
	"city": "Helsinki",
	"skills": ["JavaScrip", "React", "Python", "好"]
}
# ensure_ascii=False 表示的是 非ASCII字符（如汉字等）将以其原始形式输出 默认为True
with open('./json_example.json', 'w', encoding='utf-8') as f:
	json.dump(person, f, ensure_ascii=False, indent=4)

# 读取刚才创建的json文件
with open('./json_example.json', 'r', encoding='utf-8') as f:
	person = json.load(f)
	print(
		person)  # {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python', '好']}

# 带有csv扩展名的文件
"""
CSV代表逗号分隔值。CSV是一种简单的文件格式，用于存储表格数据，如电子表格或数据库。
CSV是数据科学中非常常见的数据格式
"""
with open('./cleaned_bi.csv') as f:
	csv_reader = csv.reader(f, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'列名为：{",".join(row)}')
			line_count += 1
		else:
			print(f'{row[0]} {row[1]}的年龄{row[2]}.他的性别是{row[3]}')
			line_count += 1
	print(f'已处理{line_count}行。')

# 使用相同的方法将数据写入csv文件
with open('./bi.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	# 写入列
	writer.writerow((['name', 'country', 'city', 'skills']))
	# 写入数据
	writer.writerow(['Asabeneh', 'Finland', 'Helsinki', 'JavaScript'])

# 带有xlsx扩展名的文件
# 要读取Excel文件，我们需要安装xlrd包。我们将使用它来读取Excel文件。
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)