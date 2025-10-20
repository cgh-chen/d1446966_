# 讓使用者輸入月份數字
num = int(input("請輸入月份數字 (1~12)："))

# 使用 if-elif 判斷輸出對應月份
if num == 1:
    print("January")
elif num == 2:
    print("February")
elif num == 3:
    print("March")
elif num == 4:
    print("April")
elif num == 5:
    print("May")
elif num == 6:
    print("June")
elif num == 7:
    print("July")
elif num == 8:
    print("August")
elif num == 9:
    print("September")
elif num == 10:
    print("October")
elif num == 11:
    print("November")
elif num == 12:
    print("December")
else:
    print("輸入錯誤，請輸入 1~12 的數字")
