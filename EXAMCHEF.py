t=int(input())

for i in range(t):
    
    x,y,z=map(int,input().split())
    
    s=x*y
    
    per=(z/s)*100 
    
    if per>50:
        print('yes')
        
    else:
        print('no')