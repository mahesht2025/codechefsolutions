T=int(input("Enter no for test :"))
for i in range(T):
    X,Y=map(int,input("Enter intial value and give space in final value :").split())
    if X>Y:
        print(X-Y)
    else:
        print(Y-X)