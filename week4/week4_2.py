# 讓使用者輸入月份數字
num = int(input("請輸入月份數字 (1~12)："))

# 使用 match-case 判斷月份
match num:
    case 12|1|2: season = "Winter"
    case 3|4|5: season = "Spring"
    case 6|7|8: season = "Summer"
    case 9|10|11: season = "Autumn"

    case _:
        season = "輸入錯誤，請輸入 1~12 的數字"

# 輸出結果
print("對應季節為：", season)