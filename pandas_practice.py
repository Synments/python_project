import pandas as pd 
import numpy as np

# 1. 使用 pd.read_csv() 讀取 CSV 檔案 
df = pd.read_csv("sample_data.csv") 

# 顯示 DataFrame 的內容 
print(df) 

# 2. 檢視 DataFrame 結構與資訊 (Inspect DataFrame Structure and Info)
print("\n--- 檢視 DataFrame 資訊 (Inspecting DataFrame Info) ---")
# 顯示 DataFrame 的前 2 行 (Display the first 2 rows)
print("DataFrame 前 2 行 (df.head(2)):\n", df.head(2))

# 顯示 DataFrame 的摘要資訊 (Display a summary of the DataFrame)
print("\nDataFrame 摘要資訊 (df.info()):")
df.info()

# 3. 模擬並處理缺失值 (Simulate and Handle Missing Values)
print("\n--- 缺失值處理 (Handling Missing Values) ---")
# 建立一個包含 NaN (Not a Number) 的 DataFrame
data_with_nan = {
    'Product': ['A', 'B', 'C', 'D'], 
    'Price': [100, 200, np.nan, 400],    # np.nan 代表缺失值 
    'Sale': [10, np.nan, 30, 40]
}

df_nan = pd.DataFrame(data_with_nan) 
print("原始帶有缺失值的 DataFrame:\n", df_nan) 

# 方法一：刪除缺失值 (Method 1: Drop Missing Values) 
# 刪除任何包含至少一個 NaN 的列 (row) 
df_dropped = df_nan.dropna() 
print("\n使用 dropna() 刪除缺失值後的結果 (只剩完整資料)：\n", df_dropped) 

# 方法二：填補缺失值 (Method 2: Fill Missing Values) 
# 填補 (fill) 缺失值，使用 Price 欄位的平均數 (mean) 來填補 Price 欄位中的 NaN 
mean_price = df_nan['Price'].mean() 
df_filled = df_nan['Price'].fillna(mean_price) 

print("\n計算出的 Price 平均數 (不包含 NaN):", mean_price) 
print("使用 fillna() 填補後的 Price 欄位 (Series):\n", df_filled) 

# 4. 處理重複值 (Handling Duplicate Values) 
print("\n--- 重複值處理 (Handling Duplicate Values) ---") 
# 建立一個包含重複記錄的 DataFrame 
data_with_duplicates ={ 
    "ID": [101, 102, 103, 102, 104, 101],
    "Score": [85, 90, 78, 90, 95, 85],
    "Course": ["Math", "English", "Science", "English", "Art", "Math"] 
} 
df_dup = pd.DataFrame(data_with_duplicates) 
print("原始帶有重複值的 DataFrame：\n",df_dup) 

# 步驟一：檢查重複 (Step 1: Check for Duplicates) 
# 檢查每一列是否與之前的列重複 
duplicates_check = df_dup.duplicated() 
print("\n重複值檢查結果 (布林序列)：\n", duplicates_check) 

# 步驟二：刪除重複 (Step 2: Drop Duplicates) 
# 刪除 (drop) 所有重複的列 (只保留第一次出現的記錄) 
df_no_duplicates = df_dup.drop_duplicates() 
print("\n使用 drop_duplicates() 刪除重複後的結果：\n", df_no_duplicates) 

