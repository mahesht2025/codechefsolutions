t = int(input())
for i in range(0,t):
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    for j in range(N):
        if(A[j] == 2):
            count += 1
    if(count % 8 == 0):
        print("YES")
    else:
        print("NO")