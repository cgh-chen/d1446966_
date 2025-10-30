# 外層 for 迴圈控制「被乘數」（1～9）
for i in range(1, 10):
    # 內層 for 迴圈控制「乘數」（1～9）
    for j in range(1, 10):
        # 印出 i * j 的結果，並用 tab 間隔，不換行
        print(i * j, end="\t")
    # 內層迴圈跑完後換行，準備印下一列
    print()

# 迴圈結束後印出提示訊息
print("Done!!")
