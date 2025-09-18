import numpy as np

# 检索numpy包的版本
print('numpy:', np.__version__)
# 检查可用的方法
print(dir(np))

# 创建一个列表
python_list = [1, 2, 3, 4, 5]
# 检查数据类型
print('Type:', type(python_list))  # Type: <class 'list'>
# 输出python_list
print(python_list)  # [1, 2, 3, 4, 5]

# 创建一个二位数组列表
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 从python列表创建Numpy(数值python)数组
numpy_array_from_list = np.array(python_list)
print(numpy_array_from_list)  # [1 2 3 4 5]
print(type(numpy_array_from_list))  # <class 'numpy.ndarray'>

# 创建浮点型NumPy数组
# 使用浮点数据类型参数从列表创建浮点NumPy数组
# 创建列表
python_list = [1, 2, 3, 4, 5]
num_array_from_list2 = np.array(python_list, dtype=float)
print(num_array_from_list2)

# 创建布尔型Numpy数组
# 从列表创建布尔NumPy数组
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)  # [False  True  True False False]

# 使用NumPy创建多维数组   一个NumPy数组可能有一个或多个行和列
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(numpy_two_dimensional_list)
print(type(numpy_two_dimensional_list))  # <class 'numpy.ndarray'>

# 用Numpy将数组转换为列表
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))  # <class 'list'>
print('一维数组：', np_to_list)  # 一维数组： [1, 2, 3, 4, 5]
print('二维数组：', numpy_two_dimensional_list.tolist())  # 二维数组： [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 从元组创建NumPy数组
# 创建一个元组
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))  # <class 'tuple'>
print(python_tuple)  # (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(numpy_array_from_tuple)  # [1 2 3 4 5]
print(type(numpy_array_from_tuple))  # <class 'numpy.ndarray'>

# NumPy数组的形状
nums = np.array([1, 2, 3, 4, 5])
print(nums)  # [1 2 3 4 5]
print('nums的形状：', nums.shape)  # nums的形状： (5,)
print('numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)  # numpy_two_dimensional_list:  (3, 3)

three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)  # (3, 4)

# NumPy数组的数据类型
# 数据类型的类型：str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)  # [-3 -2 -1  0  1  2  3]
print(int_array.dtype)  # int64
print(float_array)  # [-3. -2. -1.  0.  1.  2.  3.]
print(float_array.dtype)  # float64

# NumPy数组的大小
"""
NumPy数组与Python列表不完全相同。要对Python列表进行数学运算，我们必须遍历项目，但NumPy可以不通过循环就进行任何数学运算。数学运算：

* 加法 (+)
* 减法 (-)
* 乘法 (*)
* 除法 (/)
* 模数 (%)
* 整除 (//)
* 指数 (**)
"""

# 加法
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # 原始数组： [1 2 3 4 5]
print('加法：', numpy_array_from_list + 2)  # 加法： [3 4 5 6 7]
print('加法：', np.add(numpy_array_from_list, 2))  # 加法： [3 4 5 6 7]

# 减法
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # 原始数组： [1 2 3 4 5]
print('减法：', numpy_array_from_list - 2)  # 减法： [-1  0  1  2  3]
print('减法：', np.subtract(numpy_array_from_list, 2))  # 减法： [-1  0  1  2  3]

# 乘法
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # 原始数组： [1 2 3 4 5]
print('乘法：', numpy_array_from_list * 2)  # 乘法： [ 2  4  6  8 10]
print('乘法：', np.multiply(numpy_array_from_list, 2))  # 乘法： [ 2  4  6  8 10]

# 除法
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # 原始数组： [1 2 3 4 5]
print('除法：', numpy_array_from_list / 2)  # 除法： [0.5 1.  1.5 2.  2.5]
print('除法：', np.divide(numpy_array_from_list, 2))  # 除法： [0.5 1.  1.5 2.  2.5]

# 模数
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # 原始数组： [1 2 3 4 5]
print('模数：', numpy_array_from_list % 2)  # 模数： [1 0 1 0 1]
print('模数：', np.mod(numpy_array_from_list, 2))  # 模数： [1 0 1 0 1]
