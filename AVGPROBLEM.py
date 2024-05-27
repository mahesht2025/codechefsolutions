#Greater Average
r=int(input("Enter the test case range :"))
for i in range(r):
    a,b,c =map(int,input().split())
    d= a+b
    s= d/2
    if s > c:
        print("YES")
    else:
        print("NO")