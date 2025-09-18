print("選擇轉換類型：")
print("1:公里->英里")
print("２:英里->公里")
print("３:攝氏->華氏")
print("４:華氏->攝氏")
print("５:公斤->磅")
print("６:磅->公斤")
a= int(input("請輸入選項 （1-6):"))
n= float(input("請輸入數值："))
if a == 1:
    print("結果：", n*0.6214)
if a == 2:
    print("結果：", n*0.6214)
if a == 3:
    print("結果：", n*9/5+32)
if a == 4:
    print("結果：", (n-32)*5/9)
if a == 5:
    print("結果：", n*2.204)
if a == 6:
    print("結果：", n/2.204)