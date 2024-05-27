for T in range(int(input())):
    
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    best = 0
    for i in range(N):
        best = max(best, A[i]*20 - B[i]*10)
    
    print(best)