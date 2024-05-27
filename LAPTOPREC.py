t = int(input())
for i in range(0,t):
    a = int(input())
    b = list(map(int,input().split()))
    count_arr = [0]*(11)
    for num in b:
        count_arr[num] += 1
    max_count = max(count_arr)
    if(count_arr.count(max_count) == 1):
        print(count_arr.index(max_count))
    else:
        print("CONFUSED")