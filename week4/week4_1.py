# 讓使用者輸入月份數字
num = int(input("請輸入月份數字 (1~12)："))

# 使用 match-case 判斷月份-把 num 的值和每個 case 比對
match num:
    case 1: month = "January"
    case 2: month = "February"
    case 3: month = "March"
    case 4: month = "April"
    case 5: month = "May"
    case 6: month = "June"
    case 7: month = "July"
    case 8: month = "August"
    case 9: month = "September"
    case 10: month = "October"
    case 11: month = "November"
    case 12: month = "December"
    case _:
        month = "輸入錯誤，請輸入 1~12 的數字"

# 輸出結果
print("對應月份為：", month)
        