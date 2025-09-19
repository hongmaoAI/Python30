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

# 整除
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # [1 2 3 4 5]
print('整除：', numpy_array_from_list // 2)  # 整除： [0 1 1 2 2]
print('整除：', np.floor_divide(numpy_array_from_list, 2))  # 整除： [0 1 1 2 2]

# 指数
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组：', numpy_array_from_list)  # 原始数组： [1 2 3 4 5]
print('指数：', numpy_array_from_list ** 2)  # 指数： [ 1  4  9 16 25]
print('指数：', np.power(numpy_array_from_list, 2))  # 指数： [ 1  4  9 16 25]

# 检查数据类型
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, -1, 0, 1, 2, 3], dtype='bool')
print(numpy_int_arr.dtype)  # int64
print(numpy_float_arr.dtype)  # float64
print(numpy_bool_arr.dtype)  # bool

# 转换类型
"""
我们可以使用astype将数据类型从一种类型转换为另一种类型。
让我们将int类型转换为浮点数，浮点数转换为整数，整数转换为布尔型
"""
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr.astype('int').dtype)  # int64
numpy_float_arr = np.array([1.1, 2.0, 3.2])
print(numpy_float_arr.astype('int').dtype)  # int64
numpy_int_arr = np.array([-3, -2, -1, 0, 1, 2, 3])
print(numpy_int_arr.astype('bool').dtype)  # bool

# 多维数组
# NumPy的主要优点之一是处理多维数组。我们先构建多维数组
two_dimensional_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimensional_array))  # <class 'numpy.ndarray'>
print(two_dimensional_array)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('形状：', two_dimensional_array.shape)  # 形状： (3, 3)
print('大小：', two_dimensional_array.size)  # 大小： 9
print('数据类型：', two_dimensional_array.dtype)  # 数据类型： int64

# 从NumPy中获取项目
two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimensional_array[0]
second_row = two_dimensional_array[1]
third_row = two_dimensional_array[2]
print('第一行', first_row)  # 第一行 [1 2 3]
print('第二行', second_row)  # 第二行 [4 5 6]
print('第三行', third_row)  # 第三行 [7 8 9]

# 现在让我们获取每一行的第一项：
first_column = two_dimensional_array[:, 0]
second_column = two_dimensional_array[:, 1]
third_column = two_dimensional_array[:, 2]
print('第一列：', first_column)  # 第一列： [1 4 7]
print('第二列：', second_column)  # 第二列： [2 5 8]
print('第三列：', third_column)  # 第三列： [3 6 9]

# NumPy数组切片
"""
切片NumPy数组与切片Python列表相似，只是它适用于两个维度（行和列）。
让我们先看看如何从NumPy数组中切片项目
"""
numpy_array_from_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('原始数组：', numpy_array_from_list)  # 原始数组： [ 1  2  3  4  5  6  7  8  9 10]
# [参数1：参数二：参数三] 参数一：起始位置  参数二：停止位置  参数三：步长
ten_first_items = numpy_array_from_list[0:10]
print('前10项：', ten_first_items)
first_five_items = numpy_array_from_list[:10:2]
print(first_five_items)  # [1 3 5 7 9]
last_five_items = numpy_array_from_list[5:]
print('后5项：', last_five_items)  # 后5项： [ 6  7  8  9 10]

# 反转数组
reversed_array = numpy_array_from_list[::-1]
print('反转数组', reversed_array)  # 反转数组 [10  9  8  7  6  5  4  3  2  1]

# 我们可以在Numpy二维数组上使用切片：
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimension_array)
print(two_dimension_array[1, 1])  # 5
print(two_dimension_array[1, 1:3])  # [5 6]
print(two_dimension_array[1:3, 1:3])  # [[5 6] [8 9]]

# NumPy连接数组
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])
third_array = np.array([7, 8, 9])
# 水平连接
horizontal_concat = np.hstack((first_array, second_array, third_array))
print('水平连接：', horizontal_concat)  # 水平连接： [1 2 3 4 5 6 7 8 9]
# 垂直连接
vertical_concat = np.vstack((first_array, second_array, third_array))
print('垂直连接：', vertical_concat)  # 垂直连接： [[1 2 3] [4 5 6] [7 8 9]]

# 常见NumPy函数
# 我们看看最常见的NumPy函数: 最小值、最大值、平均值
numpy_array_from_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('最小值：', numpy_array_from_list.min())  # 最小值： 1
print('最大值：', numpy_array_from_list.max())  # 最大值： 10
print('平均值：', numpy_array_from_list.mean())  # 平均值： 5.5