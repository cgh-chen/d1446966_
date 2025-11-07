tasks = []                        # 建立一個空清單，用來存放待辦事項
tasks.append("寫作業")             # 使用 append() 在清單最後加入一個項目 "寫作業"
tasks.append("洗衣服")             # 再加入另一個項目 "洗衣服"
print(tasks)                      # 印出目前清單內容 → ['寫作業', '洗衣服']

tasks.remove("寫作業")             # 使用 remove() 把清單中第一次出現的 "寫作業" 移除
print(tasks)                      # 印出移除後的清單 → ['洗衣服']
