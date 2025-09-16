# Python的包管理器 pip
## 什么是PIP？
在运用python中我们需要使用pip来安装不同的python包
每一个包，是一个python模块
一个python模块，可以包含一个或多个模块
## 安装PIP
如果你还没有安装pip，让我们现在安装它。转到你的终端或命令提示符，复制并粘贴：

`asabeneh@Asabeneh:~$ pip install pip`

通过以下命令检查pip是否已安装：
`pip --version`

**pip 25.2 from E:\Project\Python30\Lib\site-packages\pip (python 3.13)**
# 使用pip安装包
让我们尝试安装_numpy_，即数值Python。它是机器学习和数据科学社区中最流行的包之一。

* NumPy是Python科学计算的基础包。它包含以下内容：
  * 强大的N维数组对象
  * 复杂的（广播）函数
  * 用于集成C/C++和Fortran代码的工具
  * 有用的线性代数、傅里叶变换和随机数功能
  
`~$ pip install numpy`

# Pandas是一个开源的、BSD许可的库
读取xls文件

`data_excel = pd.read_excel('../19days_file_handling_cn/sample.xls')
print(data_excel)`

# 从URL读取数据

`pip install requests`

我们将在_requests_模块中看到_get_、_status_code_、_headers_、_text_和_json_方法：
* _get()_：打开网络并从url获取数据——它返回一个响应对象
* _status_code_：在我们获取数据后，我们可以检查操作的状态（成功、错误等）
* _headers_：检查头部类型
* _text_：从获取的响应对象中提取文本
* _json_：提取json数据

