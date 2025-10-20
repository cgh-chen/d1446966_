lst = ["Jack","Mary","John","Tom","Alice","Bob"]
for i in range(0, 6) :
    print( lst[i], end="\t")
    if (i+1) % 3 == 0:
        print()
print("Done!!")