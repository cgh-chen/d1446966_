# 設定樹的高度與第二層要印幾層
height = 8        # 第一層的高度（上面那層有 8 行）
second_part = 3   # 第二層只印出下面的 3 層

# 設定顏色：紅色與重置
RED = "\033[31m"   # 紅色（讓頂部那顆星變紅）
RESET = "\033[0m"  # 重置顏色

# ===== 第一層樹身 =====
for i in range(1, height + 1):          # 從第 1 層印到第 8 層
    spaces = " " * (height - i)         # 左邊的空格數（讓星星置中）
    if i == 1:                          # 如果是第一層
        stars = RED + "*" + RESET       # 讓最上面那顆星變紅
    else:
        stars = "*" * (2 * i - 1)       # 其他層印出奇數顆星星
    print(spaces + stars)               # 印出空格 + 星星

# ===== 第二層樹身（只印下面三層） =====
for i in range(height - second_part + 1, height + 1):  # 印出第 6~8 層
    spaces = " " * (height - i)         # 左邊的空格數
    stars = "*" * (2 * i - 1)           # 星星數
    print(spaces + stars)               # 印出樹的第二層（對齊中間）

# ===== 樹幹部分 =====
for j in range(3):                      # 樹幹有 3 行
    print(" " * (height - 2) + "***")   # 每行印出 3 顆星，置中
