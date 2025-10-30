height = 8        # 第一層的高度
second_part = 3   # 第二層印出幾層（只要下面三層）

RED = "\033[31m"
RESET = "\033[0m"

# 第一層
for i in range(1, height + 1):
    spaces = " " * (height - i )
    if i ==1:
        stars = RED + "*" + RESET
    else:
        stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 第二層（要對齊中間）
for i in range(height - second_part + 1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 樹幹（三行）
for j in range(3):
    print(" " * (height - 2) + "***")
