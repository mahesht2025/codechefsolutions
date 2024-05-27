t=int(input())
for i in range(t):
    s = input()
    Hole_let=['A','B','D','O','P','Q','R']
    hole_cot=0
    for j in s:
        if j in Hole_let:
            if j=='B':
                hole_cot +=2
            else:
                hole_cot +=1
    
    print(hole_cot)            