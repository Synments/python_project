import matplotlib.pyplot as plt 
import numpy as np 
# --- 新增的中文修正代碼 START ---  
import matplotlib.font_manager as fm 
import seaborn as sns 


# --- 新增的美學設定代碼 START --- 
# 設置 Seaborn 主題，影響所有後續的 Matplotlib/Seaborn 圖表 
# 常用的主題有 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks' 
sns.set_theme(style="darkgrid") 

# 也可以使用 Matplotlib 的風格 
# plt.style.use('ggplot') 
# --- 新增的美學設定代碼 END ---

# 選擇一個常見的中文字型 
# 若在系統中 'Microsoft JhengHei' 無效，請嘗試 'SimHei' 或 'Yuanti' 
font_path = "Microsoft JhengHei" 
myfont = fm.FontProperties(fname=font_path) 

# 步驟一：設定中文字型 
# 為了讓 Matplotlib 知道要使用什麼字型，需要更新它的預設參數 
plt.rcParams['font.sans-serif'] = [font_path] 

# 步驟二：解決負號顯示問題 (在某些字型中，負號可能顯示為方框)  plt.rcParams['axes.unicode_minus'] = False 
# --- 新增的中文修正代碼 END --- 

# 1. 準備數據：產生一條正弦曲線數據 
x = np.linspace(0, 10, 100)     # 在 0 到 10 之間產生 100 個均勻分佈的點 
y = np.sin(x) 

# 2. 繪製圖表：使用 plot() 函式繪製折線圖 
plt.figure(figsize=(8, 4))    # 設定圖表大小 (可選) 
plt.plot(x, y) 

# 3. 添加標籤和標題 
plt.title("正弦曲線 (Size Wave)") 
plt.xlabel("X 軸數值") 
plt.ylabel("Y 軸 (sin(x))") 

# 4. 顯示圖表 
plt.show() 

# 5. 繪製散佈圖 (Scatter Plot) 
print("\n--- 繪製散佈圖 (Scatter Plot) ---") 
# 產生一組新的數據 
np.random.seed(42)    # 設定隨機種子，確保每次結果一樣 
x_scatter = np.random.rand(50) * 10 
y_scatter = 2 * x_scatter + np.random.randn(50) * 5 

plt.figure(figsize=(8, 4)) 
plt.scatter(x_scatter, y_scatter, color="green", alpha=0.6)    # alpha 設定透明度 
plt.title("X 與 Y 的關係 (散佈圖)", fontproperties=plt.rcParams["font.sans-serif"][0]) 
plt.xlabel("自變數 X", fontproperties=plt.rcParams["font.sans-serif"][0]) 
plt.ylabel("因變數 Y", fontproperties=plt.rcParams["font.sans-serif"][0]) 
plt.show() 

# 6. 繪製長條圖 (Bar Chart) 
print("\n--- 繪製長條圖 (Bar Chart) ---") 
# 類別數據 
categories = ["蘋果", "香蕉", "橘子", "葡萄"] 
values = [15, 20, 10, 30] 

plt.figure(figsize=(8, 4)) 
plt.bar(categories, values, color=['red', 'yellow', 'orange', 'purple']) 
plt.title("水果銷售數量", fontproperties=plt.rcParams['font.sans-serif'][0]) 
plt.xlabel("水果種類", fontproperties=plt.rcParams['font.sans-serif'][0]) 
plt.ylabel("銷售數量", fontproperties=plt.rcParams['font.sans-serif'][0]) 
plt.show() 

import seaborn as sns 

# 7. Seaborn 分佈圖 (Distribution Plot) 
print("\n--- Seaborn 分佈圖 (Distribution Plot) ---") 
# 產生一組新的數據 (模擬年齡數據) 
np.random.seed(123) 
data_dist = np.random.normal(loc=40, scale=10, size=200) # 平均值 40，標準值 10 

plt.figure(figsize=(8,4)) 
# 使用 histplot 繪製直方圖 (Histogram)，這是分佈圖最常見的形式 
sns.histplot(data_dist, kde=True)    # kde=True 表示同時繪製核密度估計曲線 

plt.title("年齡分佈圖", fontproperties=plt.rcParams['font.sans-serif'][0]) 
plt.xlabel("年齡", fontproperties=plt.rcParams['font.sans-serif'][0]) 
plt.ylabel("頻率/密度", fontproperties=plt.rcParams['font.sans-serif'][0]) 
plt.show() 

import pandas as pd

# 8. Seaborn 盒鬚圖 (Box Plot) 
print("\n--- Seaborn 盒鬚圖 (Box Plot) ---") 
# 建立一個模擬不同組別分數的 DataFrame 
df_boxplot = pd.DataFrame({ 
    "Group": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    "Score": np.concatenate([
        np.random.normal(70, 5, 20),    # Group A 平均 70 
        np.random.normal(85, 8, 20),    # Group B 平均 85 
        np.random.normal(75, 12, 20)    # Group C 平均 75 
    ]) 
}) 

plt.figure(figsize=(8, 5)) 
# 用 x 指定類別，y 指定數值 
sns.boxplot(x="Group", y="Score", data=df_boxplot) 
plt.title("不同組別的分數分布 (盒鬚圖)", fontproperties=plt.rcParams["font.sans-serif"][0])
plt.show() 

# 9. Seaborn 熱力圖 (Heatmap) 
print("\n--- Seaborn 熱力圖 (Heatmap) ---") 
# 計算 df_boxplot 數據的相關性矩陣 
correlation_matrix = df_boxplot.corr(numeric_only=True) 

plt.figure(figsize=(6, 5)) 
# 用 annot=True 在圖上顯示數值 
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Score 相關性熱力圖", fontproperties=plt.rcParams["font.sans-serif"][0]) 
plt.show()



