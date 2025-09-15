# 接收使用者輸入的年齡
# input() 函數會將使用者的輸入當作字串，因此需要用 int() 將其轉換為整數
age = int(input("請輸入您的年齡："))

# 條件判斷的開始
if age >= 18:
    print("您是成年人。")
elif age >= 13:
    print("您是青少年。")
else:
    print("您是兒童。")

print("判斷完成。")