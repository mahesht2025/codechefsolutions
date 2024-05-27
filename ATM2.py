T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = ""
    for i in range(N):
        if K >= A[i]:
            K -= A[i]
            result += "1"
        else:
            result += "0"
    print(result)
