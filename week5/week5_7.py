a, b = map(int, input("Enter 2 number: ").split())
if b < a:
    c = a       #a, b = b, a
    a = b
    b = c
total = 0
for i in range(a, b+1):
    total += i
print(total)