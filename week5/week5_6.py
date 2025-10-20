a, b = map(int, input("Enter 2 number: ").split())
total = 0
for i in range(a, b+1):
    total += i
print(total)