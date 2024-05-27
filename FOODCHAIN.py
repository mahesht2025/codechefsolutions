from math import floor

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = 1
    while a >= b:
        a = floor(a / b)
        c += 1
    print(c)