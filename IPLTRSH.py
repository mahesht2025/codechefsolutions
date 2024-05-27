#Ipl Ticket Rush
m = int(input("Enter the number :"))
for i in range(m):
    p,q = map(int, input().split())
    if p > q:
        print(p - q)
    else:
        print(0)