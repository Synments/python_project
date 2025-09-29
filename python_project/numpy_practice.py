# 1. 匯入 (import) NumPy 套件  
# 通常會給它一個別名 (alias) `np`，這是業界慣例 
import numpy as np

# 2. 建立一個一維陣列 (Create a 1D Array) 
# 將一個 Python 列表傳入 np.array() 函式中 
my_list = [1, 2, 3, 4, 5] 
my_array = np.array(my_list) 
print("一維陣列 (1D Array)：", my_array) 

# 3. 建立一個二維陣列 (Create a 2D Array) 
# 將一個巢狀列表傳入 
my_nested_list = [[1, 2, 3], [4, 5, 6]] 
my_2d_array = np.array(my_nested_list) 
print("二維陣列 (2D Array)：\n", my_2d_array) 

# 程式碼說明 (Code Explanation): 
# import numpy as np: 匯入 NumPy 套件，並將其簡稱為 `np`。 
# np.array(my_list): 呼叫 NumPy 的 array 函式，將 `my_list` 轉換成 NumPy 陣列。 
# print(): 印出陣列的內容，會發現 NumPy 陣列的顯示方式與列表不同。 

# 4. 檢視陣列屬性 (View Array Attributes) 
print("\n--- 陣列屬性 (Array Attributes) ---")
print("my_array 的維度 (Dimensions of my_array)：", my_array.ndim) 
print("my_array 的形狀 (Shap of my_array)：", my_array.shape) 
print("my_array 的元素總數 (Total elements of my_array)：", my_array.size) 
print("my_array 的資料型態 (Data type of my_array)：", my_array.dtype) 

print("\n--- 陣列屬性 (Array Attributes) ---") 
print("my_2d_array 的維度 (Dimensions of my_2d_array)：", my_2d_array.ndim) 
print("my_2d_array 的形狀 (Shape of my_2d_array)：", my_2d_array.shape) 
print("my_2d_array 的元素總數 (Total elements of my_2d_array)：", my_2d_array.size) 
print("my_2d_array 的資料型態 (Data type of my_2d_array)：", my_2d_array.dtype) 

# 程式碼說明 (Code Explanation): 
# my_array.ndim：使用 `.` 來存取陣列的屬性，例如 `my_array.ndim` 會回傳陣列的維度數。 
# my_2d_array.shape：這會回傳一個元組 (tuple)，例如 (2, 3)，表示這個二維陣列有 2 列 (row) 和 3 行 (column)。 

# 5. 陣列基本運算 (Basic Array Operations) 
print("\n--- 陣列運算 (Array Operations) ---") 
# 陣列與單一數值相加 (Add a scalar to an array) 
# NumPy 會將 `10` 這個數值，與陣列中的每一個元素相加 
add_result = my_array + 10 
print("陣列與數值相加：", add_result) 

# 陣列與陣列相乘 (Multiply an array by another array) 
# 兩個相同形狀的陣列相乘，會執行逐元素 (element-wise) 相乘 
multiply_result = my_array * my_array 
print("陣列與自身相乘：", multiply_result) 

# 6. 陣列廣播 (Array Broadcasting) 
print("\n--- 陣列廣播 (Array Broadcasting) ---") 
# 建立一個與 my_2d_array 形狀相容的陣列
broadcast_array = np.array([10, 20, 30]) 
print("廣播陣列：", broadcast_array) 

# 執行廣播運算 
# NumPy 會將 `broadcast_array` 擴展到與 `my_2d_array` 相同的形狀 (2, 3)，再進行逐元素相加 
broadcast_result = my_2d_array + broadcast_array 
print("廣播運算結果：\n", broadcast_result)

# 10. 陣列的索引與切片 (Array Indexing and Slicing) 
print("\n--- 陣列索引與切片 (Array Indexing and Slicing) ---") 
# 選取 my_array 的單一元素 (Select a single element from my_array) 
print("my_array 的第一個元素：", my_array[0])

# 選取 my_2d_array 的單一元素 (Select a single element from my_2d_array) 
# 語法為 [列, 行] 
print("my_2d_array 的第二列第三行元素：", my_2d_array[1, 2])

# 使用切片選取子集 (Use slicing to select a subarray) 
# 從 my_array 中選取第二個到第四個元素 
slice_result = my_array[1:4] 
print("切片結果：", slice_result) 

# 在二維陣列中切片 (Slicing in a 2D array) 
# 選取 my_2d_array 的所有列，和第一、二行 
slice_2d_result = my_2d_array[:, :2] 
print("二維切片結果:\n", slice_2d_result) 
