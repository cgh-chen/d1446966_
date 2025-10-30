a, b = map(int, input("Enter 2 number: ").split())
# 讓使用者輸入兩個數字，用空白分隔，例如：10 20
# input() → 取得使用者輸入的字串，例如 "10 20"
# split() → 把字串以空白切割成 ["10", "20"]
# map(int, ...) → 將每個項目轉成整數
if b < a:       # 若第二個數字 b 比第一個數字 a 小，就交換它們
    c = a       #a, b = b, a
    a = b
    b = c
total = 0
for i in range(a, b+1):
    total += i
print(total)