# 将字符串 'Thirty', 'Days', 'Of', 'Python' 连接为一个字符串 'Thirty Days Of Python'。
days = 'Thirty'
sky = 'Days'
of = 'of'
language = 'Python'
print(days + '\t' + sky + '\t' + of + '\t' + language)
# 声明一个名为 company 的变量，并将其赋值为初始值 "Coding For All"。
company = 'Coding For All'
# 使用 print() 打印变量 company。
print(company)
# 使用 len() 方法和 print() 打印 company 字符串的长度。
company_len = len(company)
print(company_len)
# 使用 upper() 方法将所有字符更改为大写字母。
company_upper = 'company'.upper()
print(company_upper)  # COMPANY
# 使用 lower() 方法将所有字符更改为小写字母。
COMPANY_lower = 'COMPANY'.lower()
print(COMPANY_lower)  # company
# 使用 capitalize()、title() 和 swapcase() 方法格式化字符串 Coding For All。
coding_capitalize = 'coding'.capitalize()
for_capitalize = 'for'.capitalize()
all_capitalize = 'all'.capitalize()
print(coding_capitalize + '\t' + for_capitalize + '\t' + all_capitalize)  # Coding For All
cfa_title = 'coding for all'.title()
print(cfa_title.title())  # Coding For All
cfa_swapcase = 'Coding For All'.swapcase()
print(cfa_swapcase)  # cODING fOR aLL
# 切片出 Coding For All 字符串的第一个单词。
cfa = 'Coding For All'.split()
# cfa_c=cfa[0]
# cfa_f=cfa[1]
# cfa_a=cfa[2]
# print(cfa_c[:1],cfa_f[:1],cfa_a[:1]) # C F A
print(cfa[0][:1], cfa[1][:1], cfa[2][:1])  # C F A
# 使用 index、find 或其他方法检查 Coding For All 字符串是否包含单词 Coding。
challenge = 'Coding For All'
coding = 'Coding'
print(challenge.index(coding))  # 0
print(challenge.find(coding)) # 0
