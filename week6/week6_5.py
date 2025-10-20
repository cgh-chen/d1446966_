# 費波那契數列 (for 迴圈)
n = int(input("請輸入要產生幾項："))

a, b = 0, 1  # 前兩項
for i in range(n):
    print(b, end=" ")
    a, b = b, a + b
