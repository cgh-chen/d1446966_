# 建立一個串列 (list)，裡面存放 6 個名字
lst = ["Jack", "Mary", "John", "Tom", "Alice", "Bob"]

# 使用 for 迴圈，讓 i 從 0 跑到 5（共 6 次）
for i in range(0, 6):
    print(lst[i], end="\t")     # 依序印出第 i 個名字，用 tab 間隔，不換行
    
    # 每印出第 3 個 (也就是第 3、6、9...) 名字時換行
    if (i + 1) % 3 == 0:        # 因為索引從 0 開始，所以要用 (i+1)
        print()                 # 換行

# 迴圈結束後印出提示訊息
print("Done!!")