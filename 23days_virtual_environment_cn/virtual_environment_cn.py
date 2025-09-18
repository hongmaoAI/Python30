# 设置虚拟环境
"""
开始项目时，最好有一个虚拟环境。虚拟环境可以帮助我们创建一个隔离或独立的环境。这将有助于避免不同项目之间的依赖冲突。
如果你在终端上输入pip freeze，你将看到计算机上安装的所有包。如果我们使用virtualenv，我们将只能访问特定于该项目的包。
打开你的终端并安装virtualenv：
"""
# 安装virtualenv
# pip install virtualenv

# 安装virtualenv包后，进入项目文件夹并通过以下命令创建虚拟环境：
# python -m venv venv

# 激活windows的虚拟环境
# 对于Windows PowerShell:
# venv\Scripts\activate

# 激活后终端：
# (venv) E:\PythonProject\23days_virtual_environment_cn>

# 让我们通过输入 pip freeze 来检查这个项目中可用的包。你不会看到任何包

# 我们将做一个小型flask项目，所以让我们为这个项目安装flask包
# pip install Flask

# 完成后，你应该使用 deactivate 来关闭活动项目。