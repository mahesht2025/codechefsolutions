n=int(input("Enter the size of list :"))
a=[]
for i in range(n):
    b=int(input("enter number :"))
    a.append(b)
a.sort()
for i in range(n):
    print("The sorting order :",a[i])