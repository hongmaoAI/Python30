# 使用pip安装包 numpy

# 引入numpy
import numpy
# 引入pandas
import pandas as pd
# requests 远程链接的包
import requests
from pprint import pp  # 导入pretty print，以美观地显示

# 查看版本号
print(numpy.version.version)  # 2.3.3

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)
print(np_arr)  # [1 2 3 4 5]

# 查看列表的长度
print(len(np_arr))  # 5

# 列表 * 2
print(np_arr * 2)  # [ 2  4  6  8 10]

# 列表 + 2
print(np_arr + 2)  # [3 4 5 6 7]

# 读取xls文件
data_excel = pd.read_excel('../19days_file_handling_cn/sample.xls')
print(data_excel)

#
url = 'https://postman-echo.com/get?foo1=bar1&foo2=bar2'
response = requests.get(url)
print(response.json())

# 从UPL远程读取埃塞俄比亚经济数据API
url = 'http://api.worldbank.org/countries/et?format=json'  # 埃塞俄比亚经济数据API
response = requests.get(url)  # 打开网络并获取数据
print(response)  # 响应对象
print(response.status_code)  # 状态码，成功时为200
# 让我们改变响应的JSON格式
ethiopia_data = response.json()
pp(ethiopia_data)  # 用pretty print打印数据
