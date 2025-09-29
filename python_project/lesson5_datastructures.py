# 使用中括號 [] 定義，元素之間用逗號 , 分隔
my_list = ["apple", "banana", "cherry"]
print("原始列表:", my_list)

# 列表是可變的，我們可以新增元素
my_list.append("orange")
print("新增元素後:", my_list)

# --- 2. 元組 (Tuple) ---
# 使用小括號 () 定義
my_tuple = ("apple", "banana", "cherry")
print("\n原始元組:", my_tuple)

# 元組是不可變的，如果嘗試新增元素會出錯
# my_tuple.append("orange") # 這一行會報錯

# --- 3. 字典 (Dictionary) ---
# 使用大括號 {} 定義，以「鍵:值」的方式儲存
my_dict = {
    "name": "小明",
    "age": 25,
    "city": "台北"
}
print("\n原始字典:", my_dict)

# 透過鍵來存取值
print("小明的年齡是:", my_dict["age"])

# 字典是可變的，我們可以修改值
my_dict["age"] = 26
print("修改年齡後:", my_dict["age"])

# --- 4. 集合 (Set) ---
# 使用大括號 {} 定義，但只包含單一元素
my_set = {"apple", "banana", "cherry", "apple"}
print("\n原始集合:", my_set)
# 集合會自動去除重複的元素，所以結果只會有三個

# 集合是可變的
my_set.add("orange")
print("新增元素後:", my_set)