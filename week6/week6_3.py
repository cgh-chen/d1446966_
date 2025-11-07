scores = (85, 90, 75)           # 建立一個「tuple（元組）」保存三個分數，tuple 是不可修改的資料型態
scores_list = list(scores)      # 使用 list() 把 tuple 轉換成「list（清單）」，清單是可修改的
scores_list[0] = 95             # 修改清單中第 1 個元素（索引 0 的位置）為 95
print(scores_list)              # 輸出修改後的清單，印出 [95, 90, 75]
