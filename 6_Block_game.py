#block game code is like the palindrome
n=int(input("Enter the value :"))
temp=n
rev=0
while n>0:
    dg=n%10
    rev=(rev*10)+dg
    n=n//10

if(temp==rev):
    print("win")
else:
    print("loose")