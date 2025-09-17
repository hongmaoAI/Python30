import requests
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# 使用requests的get方法从url获取数据
response = requests.get(url)
# 检查状态
status = response.status_code
print(status)  # 200

# 使用beautifulSoup解析页面内容
content = response.content
# 将获取到的数据解析出来
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)  # <title>BU Facts &amp; Stats | Office of the President</title>
print(soup.title.get_text())  # BU Facts & Stats | Office of the President
# print(soup.body) # 给出网站上的整个页面
print(response.status_code) # 200

tables=soup.find_all('table')
print(tables)