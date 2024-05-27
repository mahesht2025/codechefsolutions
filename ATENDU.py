for i in range(int(input())):
    T = 120
    d_t_n = int(input())
    b = input()
    count=0
    for j in b:
        if j=="1":
            count+=1
    if count + (T - d_t_n) >=90:
        print("YES")
    else:
        print("NO")
  