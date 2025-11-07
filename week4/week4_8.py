a, b = map(int, input("Enter 2 number: ").split())
n = min(a, b)
m = max(a, b)
total = 0
for i in range(n, m + 1):
    total += i
print(total)