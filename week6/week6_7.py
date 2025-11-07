scores = [50, 90, 70, 100]        # 建立一個分數清單
scores.sort()                     # 使用 sort() 將清單內容「由小到大」排序
print("排序後:", scores)           # 印出排序後的結果 → [50, 70, 90, 100]

print("是否還有90分?", 90 in scores)  # 使用 in 運算子檢查清單中是否包含 90，結果會是 True
