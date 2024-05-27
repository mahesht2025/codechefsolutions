#Better Deal
inte = int(input("Enter the test cases Number :"))
for i in range(inte):
    a,b=map(int,input().split())
    a = 100-(100*a)/100
    b = 200 - (100 * b)/100
    if a < b:
        print("First")
    else:
        print("Second")