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

# 5. 資料彙整 (Data Merging) 
print("\n--- 資料彙整 (Data Merging) ---") 

# 建立第一個 DataFrame (學生資料) 
df_students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"] 
})
print("DataFrame 1 (df_students)：\n", df_students) 

# 建立第二個 DataFrame (課程分數)
df_scores = pd.DataFrame({
    "StudentID": [1, 2, 3, 5],    # 注意學生 ID 5 是新的，4 是缺失的 
    "Score": [95, 80, 70, 99], 
    "Class": ["Math", "Math", "Science", "English"]
})
print("\nDataFrame 2 (df_scores)：\n", df_scores) 

# 使用 merge 函式合併 (Merging Using pd.merge) 
# 預設執行內連接 (Inner Join)，只保留兩個 DataFrame 中都存在的 StudentID 
df_merged_inner = pd.merge(df_students, df_scores, on="StudentID", how="inner") 
print("\n使用 pd.merge() 內部連接 (Inner Join) 的結果：\n",df_merged_inner) 

# 左連接 (Left Join): 以左側 DataFrame (df_students) 為主 
# 保留 df_students 的所有記錄，並嘗試匹配 df_scores 的數據 
df_merged_left = pd.merge(df_students, df_scores, on="StudentID", how="left") 
print("\n使用 pd.merge() 左連接 (Left Join) 的結果：\n", df_merged_left) 

# 右連接 (Right Join): 以右側 DataFrame (df_scores) 為主 
# 保留 df_scores 的所有記錄，並嘗試匹配 df_students 的數據 
df_merged_right = pd.merge(df_students, df_scores, on="StudentID", how="right") 
print("\n使用 pd.merge() 右連接 (Rignt Join) 的結果：\n", df_merged_right) 

# 6. 資料篩選與排序 (Data Filtering and Sorting) 
print("\n--- 資料篩選與排序 (Filtering and Sorting) ---") 
# 使用一個乾淨的 DataFrame 進行後續操作 

df_process = pd.DataFrame({
    "StudentID": [1, 2, 3, 4, 5], 
    "Score": [95, 80, 70, 99, 65], 
    "City": ["NY", "LD", "PA", "NY", "LD"] 
}) 
print("用於篩選和排序的 DataFrame:\n", df_process) 

# 步驟一：資料篩選 (Step 1: Data Filtering) 
# 篩選出 Score 大於等於 90 的記錄 (使用布林遮罩 Boolean Masking) 
df_filtered = df_process[df_process["Score"] >= 90] 
print("\n分數 >= 90 的篩選結果:\n", df_filtered) 

# 步驟二：資料排序 (Step 2: Data Sorting) 
# 按照 Score 欄位進行降序 (Descending) 排列 
df_sorted = df_process.sort_values(by="Score", ascending=False) 
print("\n按照分數降序排列的結果:\n", df_sorted) 

# 7. 分組聚合 (Grouping and Aggregation) 
print("\n--- 分組聚合 (Grouping and Aggregation) ---") 

# 步驟一：使用 groupby() 進行分組 
# 按 City 欄位分組，並計算每個城市分數 (Score) 的平均數 (mean) 
df_grouped = df_process.groupby("City")["Score"].mean() 
print("按城市分組並計算平均分數：\n", df_grouped) 

# 步驟二：同時計算多個統計量 
# 按 City 分組，並同時計算分數的總和 (sum) 和計數 (count) 
df_multi_agg = df_process.groupby("City")["Score"].agg(["sum", "count"]) 
print("\n按城市計算總和與計數：\n", df_multi_agg)

# 8. 樞紐分析表 (Pivot Table) 
print("\n--- 樞紐分析表 (Pivot Table) ---") 
# 建立一個包含多個欄位類型的 DataFrame 
df_pivot_data = pd.DataFrame({
    "Region": ["East", "West", "East", "West", "East"], 
    "Product": ["A", "A", "B", "B", "A"], 
    "Sales": [100, 150, 200, 120, 180], 
    "Count": [10, 5, 8, 4, 9], 
}) 
print("用於樞紐分析的 DataFrame：\n", df_pivot_data) 

# 使用 pivot_table() 進行分析 
# index='Region': 將 Region 作為表格的列標籤 (新的索引) 
# columns='Product': 將 Product 作為表格的行標籤 (新的欄位) 
# values='Sales': 針對 Sales 欄位進行聚合運算 
# aggfunc='mean': 指定聚合方式為平均數 (mean)
pivot_result = pd.pivot_table(df_pivot_data,
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="mean")
print("\n樞紐分析表結果 (按區域和產品計算平均銷售額):\n", pivot_result) 

